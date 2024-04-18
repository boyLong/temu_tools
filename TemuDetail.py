# -*- coding: utf-8 -*-

import secrets
import time
import random
import json
import requests
from common.logger import logger

from common.verify_captcha import VerifyCaptcha
from common.encrypt_tools import Anti, get_nano,hash_o
from common.device_generation import DeviceGeneration
from common.request import AsyncRequest


def get_username():
    return f"{get_id(random.randint(10,20))}@gmail.com"


def get_password():
    return 'temu_shop_123123'


def get_id(e=21):
    chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    return "".join(secrets.choice(chars) for _ in range(e))


class TemuBase:
    def __init__(
        self,
        href="",
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
        self.__url = {
            "US": {
                "gif": "https://us.thtk.temu.com/c/th.gif"
            }
        }
        self.__server_time = {}

    async def index(self):
        resp = await self.session.get(self.__location)
        self.session.session.headers.update({
            "Referer": self.__location,
        })
        self.device.reload(resp.text)

    async def get_nano(self):
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
        self.session.headers
        region = self.session.get_cookie("region", "211")
        currency = self.session.get_cookie("currency", "USD")
        language = self.session.get_cookie("language", "en")
        bg_ud = self.session.get_cookie("_bee")
        nano = await self.get_nano()
        page_id = f"10005_{int(time.time()*1000)}_{get_id(10)}"
        width = self.device.screen[0]
        height = self.device.screen[1]
        req_event = []
        if event_list is None:
            event_list = [
            {
                "page_url": "https://www.temu.com/login.html?login_scene=8",
                "refer_url": "",
                "op": "pv",
                "event": "page_show",
            },
            {
                "page_el_sn": "225383",
                "is_show": "0",
                "ndisp_rsn": "1",
                "op": "impr",
            },
            {
                "page_el_sn": "200370",
                "op": "impr",
            },
            {
                "page_el_sn": "200369",
                "op": "impr",
            },
            {
                "page_el_sn": "203251",
                "op": "impr",
            },
            {
                "login_scene": "8",
                "page_el_sn": "201249",
                "op": "impr",
            },
            {
                "login_scene": "8",
                "page_el_sn": "200070",
                "op": "impr",
            },
            {
                "login_scene": "8",
                "page_el_sn": "200070",
                "op": "impr",
            },
            {
                "login_scene": "8",
                "page_el_sn": "200072",
                "op": "impr",
            },
            {
                "login_scene": "8",
                "page_el_sn": "200067",
                "op": "impr",
            },
            {
                "login_scene": "8",
                "page_el_sn": "200073",
                "op": "impr",
            },
            {
                "login_scene": "8",
                "page_el_sn": "200074",
                "op": "impr",
            },
            {
                "page_el_sn": "200075",
                "op": "impr",
            },
            {
                "page_el_sn": "225673",
                "op": "impr",
            },
            {
                "page_el_sn": "225674",
                "op": "impr",
            },
            {
                "page_el_sn": "225672",
                "op": "impr",
            },
            {
                "login_scene": "8",
                "page_el_sn": "203448",
                "op": "impr",
                "has_red_point": "1",
            },
            {
                "login_scene": "8",
                "page_el_sn": "213223",
                "op": "impr",
            }


        ]
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
                "log_id":   f"{req_time}{get_id(16)}",
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

            }
            req_event.append(self.session.post(self.__url.get(self.country).get('gif'),
                                               headers=headers,
                                               data=data))
        await asyncio.gather(*req_event)

    def server_time(self):
        UpdateServerTime = int(time.time() * 1000)
        self.__server_time = {
            "ServerTime": int(time.time() * 1000 - random.randint(150, 200)),
            "UpdateServerTime":  UpdateServerTime,
            "UpdateFirstServerTime":  UpdateServerTime - random.randint(50, 120)
        }

    async def a4(self):
        await self.get_nano()
        self.server_time()
        await self.session.get( "https://www.temu.com/api/phantom/dm/wl/cg")
        await self.session.get( "https://www.temu.com/api/phantom/xg/pfb/a3")
        await self.session.get( "https://www.temu.com/api/phantom/xg/pfb/b")
        a4 = await self.device.a4()
        resp = await self.session.post("https://www.temu.com/api/phantom/xg/pfb/a4", json=a4)
        await self.session.get( "https://www.temu.com/api/phantom/xg/pfb/l1")
        await self.gif()
        'https://www.temu.com/api/adx/cm/ttc?scene=1&type=0'

    async def start(self):
        await self.index()
        await self.a4()
        self.anti = Anti(headers=self.session.get_headers(),
                         lt_c=[230, 9, 217, 13],
                         gt_c=[167, 184, 169, 116],
                         _=[
                            "T",
                            "*",
                            "ì",
                            "ª"
                        ])
        self.anti.up_server_time(self.__server_time)

        logger.info(f'开始注册')
        await self.gif([
            {
                "login_scene": "8",
                "page_el_sn": "200070",
                "op": "click",
            }, {
                "login_scene": "8",
                "page_el_sn": "200070",
                "op": "click",
        }])
        await self.register()

    def verify(self, response):

        if response.status_code == 200 and response.json().get("error_code") == 54001:
            logger.info(f'接口出现验证码,开始验证')
            VerifyCaptcha()
        return

    async def register(self):
        url = "https://www.temu.com/api/bg/sigerus/auth/login_name/is_registered"
        login_name = get_username()

        data = {
            "login_app_id": 203,
            "login_name": login_name,
            "support_mobile": True,
            "components_version": "0.8.0",
        }
        anti = self.anti.get_anti(event=True)
        headers["anti-content"] = anti
        resp = await self.session.post(url, headers=headers, verify=self.verify,json=data)



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
    t = TemuBase(href="https://www.temu.com/plus-size-feather-print-ruched-tank-top-casual-square-neck-sleeveless-top-for-summer-womens-plus-size-clothing-g-601099543413804.html?is_back=1",headers=headers)

    import asyncio
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(t.start())

#     '''
# select a.shop_url from tmp.tmp_ods_tokopedia_sold_list_20240415_shop2 a left join tmp.tmp_ods_tokopedia_sold_list_20240415_shop b on a.shop_id=b.shop_id where b.shop_id is null group by a.shop_url
#
#     '''