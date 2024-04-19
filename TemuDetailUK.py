# -*- coding: utf-8 -*-
import re
import uuid
from urllib.parse import quote_plus
import secrets
import time
import random
import json
import requests
from common.logger import logger

from common.verify_captcha import VerifyCaptcha
from common.encrypt_tools import AsyncAnti, get_nano,hash_o
from common.device_generation import DeviceGeneration
from common.request import AsyncRequest


def get_username():
    return f"{get_id(random.randint(10,20))}@gmail.com"


def get_password():
    return 'temu_shop_123123'


def get_id(e=21):
    chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    return "".join(secrets.choice(chars) for _ in range(e))


class TemuDetail:
    def __init__(
        self,
        href="https://www.temu.com/plus-size-mens-shock-absorption-blade-type-shoes-breathable-lace-up-non-slip-shoes-for-jogging-walking-g-601099523731529.html",
        proxy=None,
        headers=None,
    ):
        self.anti = None
        self.session = AsyncRequest(proxy=proxy, headers=headers)
        self.device = DeviceGeneration(self.session.get_headers())
        self._session_id = get_id(10)
        self.__event = {}
        self.__metrics_counter__ = 0
        self.country = "US"
        self.__location = href
        goods_id = re.findall(f"g-(\d+)\.html", self.__location) or ['601099523731529']
        self.goods_id = goods_id[0]
        self.__url = {
            "US": {
                "gif": "https://us.thtk.temu.com/c/th.gif"
            }
        }
        self.__server_time = {}

    async def index(self, href):
        resp = await self.session.get(href)

        self.session.update_headers({
            "referer": href,
        })
        await self.get_nano()
        self.session.anti = AsyncAnti(headers=self.session.get_headers(),
                                      lt_c=[230, 9, 217, 13],
                                      gt_c=[167, 184, 169, 116],
                                      _=[
                                          "T",
                                          "*",
                                          "ì",
                                          "ª"
                                      ])

        self.location = href
        self.device.reload(resp.text)

    async def get_nano(self):
        self.session.anti = AsyncAnti(headers=self.session.get_headers(),
                             lt_c=[230, 9, 217, 13],
                             gt_c=[167, 184, 169, 116],
                             _=[
                                "T",
                                "*",
                                "ì",
                                "ª"
                            ])
        if self.session.get_cookie("_nano_fp"):
            return self.session.get_cookie("_nano_fp")
        nano = await get_nano()
        self.session.update_cookie({"_nano_fp": nano})
        return nano

    def get_event(self,name):
        count = self.__event.get(name,1)
        self.__event[name] = count + 1
        return count

    async def gif(self, event_list=None):
        region = self.session.get_cookie("region", "211")
        currency = self.session.get_cookie("currency", "USD")
        language = self.session.get_cookie("language", "en")
        bg_ud = self.session.get_cookie("_bee")
        nano = await self.get_nano()
        page_id = f"10032_{int(time.time()*1000)}_{get_id(10)}"
        width = self.device.screen[0]
        height = self.device.screen[1]
        req_event = []
        if event_list is None:
            event_list = [
                {
                    "goods_id": str(self.goods_id),
                    "main_goods_id": str(self.goods_id),
                    "page_sn": "10032",
                    "page_url": self.__location,
                    "refer_url": "",
                    "op": "pv",
                    "event": "page_show",
                },
                {
                    "goods_id": str(self.goods_id),
                    "main_goods_id": str(self.goods_id),
                    "page_sn": "10032",
                    "page_el_sn": "225383",
                    "is_show": "0",
                    "ndisp_rsn": "1",
                    "op": "impr",
                },
                {
                    "goods_id": str(self.goods_id),
                    "main_goods_id": str(self.goods_id),
                    "page_sn": "10032",
                    "is_back": "1",
                    "op": "impr",
                    "page_el_sn": "205915",
                    "goods_added_status": "0",
                    "is_sold_out": "1",
                }
                ]
        if self.session.get_cookie("_bee"):

            cookie = (f'api_uid={self.session.get_cookie("api_uid")}; _bee={self.session.get_cookie("_bee")};'
               f' njrpl={self.session.get_cookie("njrpl")}; dilx={self.session.get_cookie("dilx")}; hfsc={self.session.get_cookie("hfsc")}')
        else:
            cookie = f'api_uid={self.session.get_cookie("api_uid")}'
        for event in event_list:
            event_count = self.get_event(event["op"])
            req_time = str(time.time() * 1000)
            dcf = hash_o(f"{req_time}{event}{event_count}")
            data = {
                "page_sn": "10013",
                "page_id": page_id,
                "cli_timezone": "Asia/Shanghai",
                "cli_region": region,
                "cli_currency": currency,
                "cli_language": language,
                "_x_sessn_id": self._session_id,
                "time": req_time,
                "log_id":  f"{req_time}{get_id(16)}",
                "user_id": "",
                "uin": "",
                "app_id": "",
                "screen_width": height,
                "screen_height": width,
                "dpr": "1",
                "app_version": "",
                "platform": "browser",
                "plat_type": "pc",
                "cookie_fp": nano,
                "storage_fp": nano,
                "dcf": f".{event_count}.{dcf}",
                "bg_id": bg_ud,
                "os_language": self.device.languages[0],
                "_ck_h_sequ": str(self.__metrics_counter__),
                "support_beacon": "1"
            }
            self.__metrics_counter__ += 1

            data.update(event)
            headers = {
                'accept': '*/*',
                'content-type': 'text/plain;charset=UTF-8',
                'origin': 'https://www.temu.com',
                'referer': 'https://www.temu.com/',
                "cookie": cookie

            }
            req_event.append(self.session.post(self.__url.get(self.country).get('gif'),
                                               headers=headers,
                                               data=data))
        await asyncio.gather(*req_event)

    async def server_time(self):
        UpdateServerTime = int(time.time() * 1000)
        server_time = await self.session.get("https://www.temu.com/api/server/_stm")

        self.__server_time = {
            "ServerTime": server_time.json()["server_time"],
            "UpdateServerTime": UpdateServerTime,
            "UpdateFirstServerTime":  UpdateServerTime - random.randint(50, 120)
        }
        self.session.up_server_time(self.__server_time)

    async def a4(self):
        await self.get_nano()
        await self.server_time()

        await self.session.get( "https://www.temu.com/api/phantom/dm/wl/cg")
        await self.session.get( "https://www.temu.com/api/phantom/xg/pfb/a3")
        await self.session.get( "https://www.temu.com/api/phantom/xg/pfb/b")
        a4 = await self.device.a4()
        await self.session.post("https://www.temu.com/api/phantom/xg/pfb/a4", json=a4)
        await self.session.get( "https://www.temu.com/api/phantom/xg/pfb/l1")

    async def start(self):
        await self.index(self.__location)
        await self.gif(
        event_list = [
                {
                    "goods_id": str(self.goods_id),
                    "main_goods_id": str(self.goods_id),
                    "page_sn": "10032",
                    "page_url": self.__location,
                    "refer_url": "",
                    "op": "pv",
                    "event": "page_show",
                },
                {
                    "goods_id": str(self.goods_id),
                    "main_goods_id": str(self.goods_id),
                    "page_sn": "10032",
                    "page_el_sn": "225383",
                    "is_show": "0",
                    "ndisp_rsn": "1",
                    "op": "impr",
                },
                {
                    "goods_id": str(self.goods_id),
                    "main_goods_id": str(self.goods_id),
                    "page_sn": "10032",
                    "is_back": "1",
                    "op": "impr",
                    "page_el_sn": "205915",
                    "goods_added_status": "0",
                    "is_sold_out": "1",
                }
                ])

        await self.a4()
        self.anti.up_server_time(self.__server_time)

        logger.info(f'开始验证')
        url = 'https://www.temu.com/api/poppy/v1/title_bar_list?scene=home_title_bar_list'
        data = {"scene":"home_title_bar_list","offset":0,"pageSize":0,"pageSn":10032,"listId":uuid.uuid4().hex}
        await self.session.post(url, json=data,verify=self.verify)

        return self.session.get_headers()

    async def verify(self, response):

        if response.status_code == 200 and response.json().get("error_code") == 54001:
            verify_auth_token = response.json()["verify_auth_token"]
            logger.info(f'接口出现验证码,开始验证 token:{verify_auth_token}')

            self.session.update_headers({
                "verifyauthtoken": verify_auth_token
            })
            self.session.update_cookie({
                "verifyAuthToken": verify_auth_token
            })

            self.session.update_headers({
                'referer': f'https://www.temu.com/uk/bgn_verification.html?VerifyAuthToken={verify_auth_token}&from='
                           f'{quote_plus(self.__location)}&type=iframe&iframeMsgId={get_id(21)}'
            })

            vc = VerifyCaptcha(self.session.get_headers(), self.session, )
            res = await vc.start()
            self.session.update_headers({
                'referer': self.__location,
            })
            return res
        return True


if __name__ == '__main__':
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        'referer': "https://www.temu.com",
        'pragma': 'no-cache',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
    }
    import asyncio
    t = TemuDetail(href="https://www.temu.com/plus-size-feather-print-ruched-tank-top-casual-square-neck-sleeveless-top-for-summer-womens-plus-size-clothing-g-601099543413804.html?is_back=1",headers=headers)

    import asyncio
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(t.start())

#     '''
# select a.shop_url from tmp.tmp_ods_tokopedia_sold_list_20240415_shop2 a left join tmp.tmp_ods_tokopedia_sold_list_20240415_shop b on a.shop_id=b.shop_id where b.shop_id is null group by a.shop_url
#
#     '''