# -*- coding: utf-8 -*-

import secrets
import time
import random
import asyncio
import re
import json
import hashlib
import hmac
import uuid

from common.logger import logger
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
from common.verify_captcha import VerifyCaptcha
from common.encrypt_tools import AsyncAnti, get_nano,hash_o,get_random
from common.device_generation import DeviceGeneration
from common.request import AsyncRequest
from common.config import get_dr, get_gif_url,host


class TemuDetail:
    def __init__(
            self,
            detail_url="https://www.temu.com/uk/solid-lace-splicing-notched-neck-top-casual-eyelet-single-breasted-top-for-spring-summer-womens-clothing-g-601099542555117.html",
            headers=None,
            gif=True,
            login=True,

    ):
        self.anti = None
        self.session = AsyncRequest(proxy=False, headers=headers)
        self.device = DeviceGeneration(self.session.get_headers())
        self._session_id = get_random(10)
        self.page_id = f"10005_{int(time.time() * 1000)}_{get_random(10)}"
        self.__event = {}
        self.__metrics_counter__ = 0
        self.location = detail_url
        self.pagePath = detail_url.replace("https://www.temu.com", '')
        self.__server_time = {}
        self.need_gif=gif
        self.need_login=login
        self.login_name = ""
        self.region_short_name = "UK"
        self.password = ''

    async def get_nano(self):
        if self.session.get_cookie("_nano_fp"):
            return self.session.get_cookie("_nano_fp")
        nano = await get_nano()
        self.session.update_cookie({"_nano_fp": nano})
        return nano

    async def index(self,href):
        resp = await self.session.get(href)
        self.session.update_headers({
            "referer": href,
        })
        self.pagePath = href.replace("https://www.temu.com",'')

        self.session.pagePath =self.pagePath
        self.session.location = href
        self.session.page_id =  self.page_id
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

    async def server_time(self):
        logger.info("更新时间")
        UpdateServerTime = int(time.time() * 1000)
        server_time = await self.session.get("https://www.temu.com/api/server/_stm", api=True)
        self.__server_time = {
            "ServerTime": server_time.json()["server_time"],
            "UpdateServerTime": UpdateServerTime,
            "UpdateFirstServerTime":  UpdateServerTime - random.randint(50, 120)
        }
        self.session.up_server_time(self.__server_time)

    async def start(self):
        await self.index(self.location)
        await self.server_time()
        await self.get_nano()
        good_id = re.findall("g-(\d+)", self.location)

        data = {
            "goods_id": str(good_id[0]),
            "_oak_query_app_only": 1,
            "_oak_query_used_wish": 1,
            "_oak_show_leaf_category_low_price_tag": 1,
            "_oak_show_sale_price_suffix": 1,
            "_oak_stage": 4,
            "_oak_share_url": self.location.replace("https://www.temu.com",'')
        }
        resp = await self.session.post("https://www.temu.com/uk/api/oak/integration/render",
                                        anti={"event": False},
                                        api=True,
                                        json=data)

        if resp.status_code == 403 and resp.json()["error_code"] == 40001:
            print("登录")
            return

        print(resp.json())


if __name__ == '__main__':
    a = TemuDetail(headers={
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
        "cookie": "timezone=Asia%2FShanghai; currency=GBP; language=en; region=210; webp=1"
    })
    asyncio.run(a.start())