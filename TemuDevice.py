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


class TemuDevice:

    def __init__(
        self,
        headers=None,
        need_gif=True,
    ):
        self.session = AsyncRequest(proxy=True, headers=headers)
        self.device = DeviceGeneration(self.session.get_headers())
        self._session_id = get_random(10)
        self.page_id = f"10013_{int(time.time()*1000)}_{get_random(10)}"
        self.__event = {}
        self.__metrics_counter__ = 0
        self.__server_time = {}
        self.location = "https://www.temu.com"
        self.enter_time = time.time()
        self.need_gif = need_gif

    async def get_nano(self):
        if self.session.get_cookie("_nano_fp"):
            return self.session.get_cookie("_nano_fp")
        nano = await get_nano()
        self.session.update_cookie({"_nano_fp": nano})
        return nano

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
        self.__location = href
        self.device.reload(resp.text)
        return resp
    async def server_time(self):
        logger.info("更新时间")
        UpdateServerTime = int(time.time() * 1000)
        server_time = await self.session.get("https://www.temu.com/api/server/_stm")
        self.__server_time = {
            "ServerTime": server_time.json()["server_time"],
            "UpdateServerTime": UpdateServerTime,
            "UpdateFirstServerTime":  UpdateServerTime - random.randint(50, 120)
        }
        self.session.up_server_time(self.__server_time)
        logger.info("更新完成")

    async def a4(self):
        a4 = await self.device.a4()
        await asyncio.gather(*[
            self.get_nano(), self.server_time(),
            self.session.get("https://www.temu.com/api/phantom/dm/wl/cg"),
            self.session.get("https://www.temu.com/api/phantom/xg/pfb/a3"),
            self.session.get("https://www.temu.com/api/phantom/xg/pfb/b"),
            self.session.post("https://www.temu.com/api/phantom/xg/pfb/a4", json=a4),
            self.session.get("https://www.temu.com/api/phantom/xg/pfb/l1")
            ],
        )

    def get_event(self, name):
        count = self.__event.get(name, 1)
        self.__event[name] = count + 1
        return count

    async def gif(self, event_list=None):
        if not self.need_gif:
            return
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
                "log_id": f"{req_time}{get_random(16)}",
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

    async def start(self):
        resp = await self.index("https://www.temu.com/")
        self.session.update_headers({
            'referer': f"https://www.temu.com/?refer_page_name=home&refer_page_id={self.page_id}&refer_page_sn=10013&_x_sessn_id={self._session_id}",
        })
        try:
            raw_data = re.findall("window\.rawData=(.*?\});", resp.text)[0]
            raw_data = json.loads(raw_data)
            self.home_page_list_id = raw_data['store']['pageListId']
            self.goods_list_id = raw_data['store']['recGoodsListId']
        except:
            raise Exception('当前ip得登录')
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
        await self.session.get('https://www.temu.com/api/adx/cm/ttc?scene=1&type=0')
        resp = await self.session.post("https://www.temu.com/api/poppy/v1/opt?scene=opt_floating_layer_rec",
                                       anti={"event": False},
                                       json={"scene": "opt_floating_layer_rec",
                                             "listId": get_random(6),
                                             "pageListId": raw_data['store']['layoutData']["commonData"]["pageListId"],
                                             "optId": -13,
                                             "optType": 1, "offset": 0, "pageSize": 5}
                                       )
        if resp.json().get("error_code") == 54001:

            return {
                "headers": self.session.get_headers(),
                "verify_auth_token":resp.json()["verify_auth_token"]
            }
        print(resp.text)

if __name__ == '__main__':
    a = TemuDevice({
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
    },need_gif=False)
    asyncio.run(a.start())
