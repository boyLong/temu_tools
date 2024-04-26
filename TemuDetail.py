# -*- coding: utf-8 -*-
import re
import asyncio
from urllib.parse import quote_plus, urlparse, parse_qs, urlencode
import secrets
import time
import random
import json
import requests
from common.logger import logger

from common.verify_captcha import VerifyCaptcha
from common.encrypt_tools import AsyncAnti, get_nano, hash_o,get_random
from common.device_generation import DeviceGeneration
from common.request import AsyncRequest
from common.config import get_gif_url, get_dr

def get_username():
    return f"{get_id(random.randint(10, 20))}@gmail.com"


def get_password():
    return 'temu_shop_123123'


def get_id(e=21):
    chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    return "".join(secrets.choice(chars) for _ in range(e))


class TemuDetail:
    def __init__(
            self,
            href="https://www.temu.com/",
            # proxy='http://look1234-zone-custom-region-hk:look1234@47.236.40.83:8088',
            proxy=None,
            headers=None,
    ):
        self.anti = None
        self.session = AsyncRequest(proxy=proxy, headers=headers)
        self.device = DeviceGeneration(self.session.get_headers())
        self._session_id = get_id(10)
        self.page_id = f"10005_{int(time.time() * 1000)}_{get_id(10)}"

        self.__event = {}
        self.__metrics_counter__ = 0
        self.__location = href


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
        return resp.text

    async def get_nano(self):
        if self.session.get_cookie("_nano_fp"):
            return self.session.get_cookie("_nano_fp")
        nano = await get_nano()
        self.session.update_cookie({"_nano_fp": nano})
        return nano

    def get_event(self, name):
        count = self.__event.get(name, 1)
        self.__event[name] = count + 1
        return count

    async def gif(self, event_list=None):
        region = self.session.get_cookie("region", "211")
        currency = self.session.get_cookie("currency", "USD")
        language = self.session.get_cookie("language", "en")
        bg_ud = self.session.get_cookie("_bee")
        nano = await self.get_nano()
        width = self.device.screen[0]
        height = self.device.screen[1]
        req_event = []

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
                "page_sn": "10005",
                "page_id": self.page_id,
                "cli_timezone": "Asia/Shanghai",
                "cli_region": region,
                "cli_currency": currency,
                "cli_language": language,
                "_x_sessn_id": self._session_id,
                "time": req_time,
                "log_id": f"{req_time}{get_id(16)}",
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
            req_event.append(self.session.post(get_gif_url(region),
                                               headers=headers,
                                               data=data))
        await asyncio.gather(*req_event)
    async def server_time(self):
        UpdateServerTime = int(time.time() * 1000)
        server_time = await self.session.get("https://www.temu.com/api/server/_stm")

        self.__server_time = {
            "ServerTime": server_time.json()["server_time"],
            "UpdateServerTime": UpdateServerTime,
            "UpdateFirstServerTime": UpdateServerTime - random.randint(50, 120)
        }
        self.session.up_server_time(self.__server_time)

    async def a4(self):
        await self.get_nano()
        await self.server_time()

        await asyncio.gather(*[self.session.get("https://www.temu.com/api/phantom/dm/wl/cg"),
            self.session.get("https://www.temu.com/api/phantom/xg/pfb/a3"),
            self.session.get("https://www.temu.com/api/phantom/xg/pfb/b")])

        a4 = await self.device.a4()
        await self.session.post("https://www.temu.com/api/phantom/xg/pfb/a4", json=a4)
        await self.session.get("https://www.temu.com/api/phantom/xg/pfb/l1")

    async def front_err(self):
        pass
    async def start(self):


        text = await self.index(self.__location)
        try:
            raw_data = re.findall("window\.rawData=(.*?\});", text)[0]
            raw_data = json.loads(raw_data)
            pageListId = raw_data['store']['pageListId']
            self.home_page_list_id = raw_data['store']['pageListId']
        except:
            raise Exception('获取首页raw_data失败, 设备权重过低,不在继续')
        await self.a4()
        await self.gif(
            event_list=[
                {
                    "page_url": "https://www.temu.com/",
                    "refer_url": "https://www.google.com/",
                    "op": "pv",
                    "event": "page_show",
                },
                {
                    "hit": "0",
                    "page_el_sn": "225383",
                    "is_show": "0",
                    "ndisp_rsn": "1",
                    "op": "impr",
                },
                {
                    "hit": "0",
                    "page_el_sn": "228053",
                    "promo_atmos": "0",
                    "op": "impr",
                },
                {
                    "hit": "0",
                    "page_el_sn": "200370",
                    "op": "impr",
                }
            ])

        event_list = []
        for i in raw_data["store"]["layoutData"]["headerData"]["titleBarList"]:
            event_list.append(
                {
                    "page_el_sn": i["pageElSn"],
                    "p_rec":i["pRec"],
                    "source": i["landingSource"],
                    "tab_id": i["id"],
                    "op": "impr",
                }
            )
        await self.gif(event_list)

        logger.info(f'开始验证')
        await self.session.get('https://www.temu.com/api/adx/cm/ttc?scene=1&type=0')
        url = 'https://www.temu.com/api/alexa/homepage/goods_list'
        list_id = raw_data['store']['recGoodsListId']
        params = (
            ('extend_fields', '{}'),
            ('offset', '0'),
            ('count', '120'),
            ('list_id', list_id),
            ('opt_id', '25'),
            ('listId', list_id),
            ('scene', 'home'),
            ('page_list_id', pageListId),
        )
        resp = await self.session.get(url, anti={"event": False}, params=params, verify=self.verify)


        res_data = resp.json()
        if not res_data.get('success') or res_data.get('error_code') != 1000000:
            raise Exception('获取home_goods_list失败,不在继续')

        resp = await self.session.post("https://www.temu.com/api/poppy/v1/opt_list?scene=opt_list_all",
                                       anti={"event": False},
                                       verify=self.verify,
                                        json={"scene":"opt_list_all","list_id":get_id(6)})
        if resp.status_code != 200 or not resp.json().get("success"):
            raise Exception('获取opt_list失败,不在继续')


        logger.info(f"选择一部分商品进行gif提交")
        idx = 1
        env_list = []
        for good in res_data.get('result')["home_goods_list"][:5]:
            good_data = good["data"]
            env_list.append({
                    "hit": "0",
                    "login_scene": "202",
                    "p_rec": json.dumps(good_data["p_rec"],separators=(',', ':')),
                    "idx": str(idx),
                    "g_idx": str(idx),
                    "op": "impr",
                    "page_el_sn": "200024",
                    "show_currency": good_data["p_rec"]["show_currency"],
                    "show_price":  good_data["p_rec"]["show_price"],
                    "show_sales": good_data["p_rec"]["show_sales"],
                    "show_skc": "0",
                    "tag_list": "just bought",
                    "goods_id": good_data["p_rec"]["g"],
                    "page_list_id":pageListId,
            })

        await self.gif(event_list=env_list)
        return self.session.get_headers()
        logger.info("校验sku接口")
        spec_ids = ''
        good_id = '601099518641848'
        for good in res_data.get('result')["home_goods_list"]:
            if good["data"].get("sold_quantity_percent"):
                spec_ids = good["data"].get("spec_ids", '')
                good_id = good["data"].get("goods_id")
                break
        data = {"page_sn": 10005, "_oak_sku_count": 1, "_oak_show_sale_price_suffix": 1,
         "_oak_show_leaf_category_low_price_tag": "1", "_oak_stage": len(spec_ids.split(",")), "single_sku_ignore_panel": 0,
         "goods_id": good_id, "_oak_spec_ids": spec_ids, "_oak_page_source": 102,
         "request_type": 0}
        resp = await self.session.post("https://www.temu.com/api/oak/integration/sku",
                                anti={
                                    "event":True,
                                },verify=self.verify,json=data)
        if resp.status_code == 200 and resp.json()["success"]:
            logger.info(f'skuheaders激活成功')


            print(self.session.get_headers())
        else:
            print(resp.json())
        # return self.session.get_headers()

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

            url_info = urlparse(self.__location)
            query = parse_qs(url_info.query)
            new_query = {}

            for k, v in query.items():
                new_query[k] = v[0] if v else ''
            new_query["_x_sessn_id"] = self._session_id
            new_query["refer_page_name"] = "bgn_verification"
            new_query["refer_page_id"] = self.page_id
            new_query["refer_page_sn"] = "10005"

            self.__location = url_info._replace(query=urlencode(new_query)).geturl()
            self.session.update_headers({
                'referer': self.__location,
            })
            return res
        return response


if __name__ == '__main__':
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        'referer': "https://www.google.com/",
        'pragma': 'no-cache',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        "cookie": "timezone=Asia%2FShanghai; currency=USD; language=en; region=211; webp=1"

    }
    user = f"user-databurning-sessid-{get_random(8)}-sesstime-20-keep-true"
    proxy = f'http://{user}:databurning@43.128.74.58:30111'
    t = TemuDetail(href="https://www.temu.com/", headers=headers,
                   proxy=None)



    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(t.start())

#     '''
# select a.shop_url from tmp.tmp_ods_tokopedia_sold_list_20240415_shop2 a left join tmp.tmp_ods_tokopedia_sold_list_20240415_shop b on a.shop_id=b.shop_id where b.shop_id is null group by a.shop_url
#
#     '''
