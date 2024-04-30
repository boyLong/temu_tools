# -*- coding: utf-8 -*-

import secrets
import time
import random
import asyncio
import re
import json
import hashlib
import hmac
from common.logger import logger
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
from common.verify_captcha import VerifyCaptcha
from common.encrypt_tools import AsyncAnti, get_nano,hash_o
from common.device_generation import DeviceGeneration
from common.request import AsyncRequest
from common.config import get_dr, get_gif_url
from common.redis_handler import redis_Handler


def encrypt(text, pubkey):
    public_key = f"""-----BEGIN PUBLIC KEY-----
    {pubkey}
    -----END PUBLIC KEY-----"""
    pub_key = RSA.importKey(public_key)
    cipher = PKCS1_cipher.new(pub_key)
    rsa_text = cipher.encrypt(text.encode("utf-8)")).hex()  # 加密并转为b64编码
    return rsa_text

def get_username():
    return f"{get_id(random.randint(10,20))}@gmail.com"


def get_password():
    return 'temu_shop_123123'


def get_id(e=21):
    chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    return "".join(secrets.choice(chars) for _ in range(e))


class TemuLogin:
    def __init__(
        self,
        headers=None,
    ):
        self.session = AsyncRequest(proxy=True, headers=headers)
        self.device = DeviceGeneration(self.session.get_headers())
        self._session_id = get_id(10)
        self.page_id = f"10013_{int(time.time()*1000)}_{get_id(10)}"
        self.__event = {}
        self.__metrics_counter__ = 0
        self.__server_time = {}
        self.location = "https://www.temu.com"
        self.enter_time = time.time()

    async def index(self,href):
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

    def get_event(self,name):
        count = self.__event.get(name,1)
        self.__event[name] = count + 1
        return count

    async def gif(self, event_list):
        logger.info("gif日志提交")
        region = self.session.get_cookie("region", "211")
        currency = self.session.get_cookie("currency", "USD")
        language = self.session.get_cookie("language", "en")
        bg_ud = self.session.get_cookie("_bee")
        nano = await self.get_nano()
        width = self.device.screen[0]
        height = self.device.screen[1]
        cookie = (f'api_uid={self.session.get_cookie("api_uid")}; _bee={self.session.get_cookie("_bee")};'
                  f' njrpl={self.session.get_cookie("njrpl")}; dilx={self.session.get_cookie("dilx")}; hfsc={self.session.get_cookie("hfsc")}')
        event_req = []
        for event in event_list:
            event_count = self.get_event(event["op"])
            req_time = str(int(time.time() * 1000))
            dcf = hash_o(f"{req_time}{event['op']}{event_count}")
            data = {
                "page_sn": "10013",
                "page_id": self.page_id,
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
                "cookie": cookie
            }
            event_req.append(self.session.post(get_gif_url(region),
                                               headers=headers,
                                               data=data))
        await asyncio.gather(*event_req)

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
            self.server_time(),
            self.session.get("https://www.temu.com/api/phantom/dm/wl/cg"),
            self.session.get("https://www.temu.com/api/phantom/xg/pfb/a3"),
            self.session.get("https://www.temu.com/api/phantom/xg/pfb/b"),
            self.session.post("https://www.temu.com/api/phantom/xg/pfb/a4", json=a4),
            self.session.get("https://www.temu.com/api/phantom/xg/pfb/l1")
        ])

    async def start(self):
        logger.info("访问首页")
        await self.index(href="https://www.temu.com/login.html?login_scene=8")
        self.enter_time = int(time.time()*1000)
        logger.info("访问a4")
        await self.a4()
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

        ]
        await self.session.get('https://www.temu.com/api/adx/cm/ttc?scene=1&type=0')
        await self.gif(event_list)
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

        return await self.register()

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
            vc = VerifyCaptcha(self.session.get_headers(), self.session)
            res = await vc.start()
            self.session.update_headers({
                'referer': self.location,
            })
            return res
        return response
    async def register(self):

        url = "https://www.temu.com/api/bg/sigerus/auth/login_name/is_registered"
        login_name = get_username()

        data = {
            "login_app_id": 203,
            "login_name": login_name,
            "support_mobile": True,
            "components_version": "0.8.0",
            "login_scene": 8
        }

        resp = await self.session.post(url, anti={"event":True},  verify=self.verify, json=data)
        if not resp.json()["success"]:
            logger.info("注册被风控")
            return
        logger.info(f'{login_name}账号可以注册')
        data = {"login_app_id": 203, "login_name": login_name}

        resp = await self.session.post(
            "https://www.temu.com/api/bg/sigerus/auth/pub_key/request",
            anti={"event":True,"element":"submit-button"},
            json=data,
        )

        pub_info = resp.json()["result"]
        password = get_password()
        l = hmac.new(
            pub_info["salt"].encode("utf-8"), password.encode("utf-8"), hashlib.sha256
        ).hexdigest()
        info = ":".join(
            [l, str(pub_info["server_time"]), pub_info["nonce"], pub_info["salt"]]
        )
        region = self.session.get_cookie("region")

        data = {
            "frontend_dr": get_dr(region),
            "login_type": 1,
            "login_app_id": 203,
            "login_scene": 8,
            "sign": pub_info["sign"],
            "key_version": 57,
            "email": login_name,
            "password": encrypt(info, pub_info["pub_key"]),
            "is_login": False,
            "stay_signed_in": False,
            "login_source": 0,
            "password_level": 4,
            "components_version": "0.9.8",
        }
        resp = await self.session.post("https://www.temu.com/api/bg/sigerus/auth/login?is_back=1",
                          anti={
                              "event":True,
                                "element": "submit-button"
                            },
                          json=data
                      )
        result = resp.json()
        if resp.status_code == 200 and result["success"] and result["error_code"] == 1000000:
            logger.info(f'{login_name}登录成功')
            login_env = {
                "hit": "0",
                "login_scene": "602",
                "op": "event",
                "sub_op": "login",
                "login_style": "0",
                "login_result": "success",
                "login_app_id": "203",
                "login_type": "1",
            }
            await self.gif([login_env])

            await self.session.get("https://www.temu.com/api/adx/cm/ttc?scene=1&type=1")
            res = await self.account_risk_test()
            if res:
                return {
                    "headers": self.session.get_headers(),
                    "account": login_name,
                    "password": password,
                    "proxy": self.session.proxies,
                }
            else:
                logger.info(f'{login_name}账号风控验证失败')
        else:
            logger.info(f'{login_name}登录失败')
        raise Exception("登录失败")

    async def account_risk_test(self):
        logger.info(f'开始验证账号风控')
        self.location =  f"https://www.temu.com/?refer_page_name=login&refer_page_id={self.page_id}&refer_page_sn=10013&_x_sessn_id={self._session_id}"
        self.session.update_headers({
            "referer": self.location,
        })
        url = 'https://www.temu.com/api/poppy/v1/opt_list?scene=opt_list_all'
        data = {"scene": "opt_list_all", "list_id": get_id(6)}

        resp = await self.session.post(url, anti={"event": True}, verify=self.verify, json=data)
        if resp.json()["success"]:
            logger.info(f'账号风控验证成功')
            return True
        else:
            raise Exception(f"风控验证失败,{resp.text}")

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
        "cookie": "timezone=Asia%2FShanghai; region=211; language=en; currency=USD; webp=1"
    }



    t = TemuLogin(headers=headers  )

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(t.start())

#     '''
# select a.shop_url from tmp.tmp_ods_tokopedia_sold_list_20240415_shop2 a left join tmp.tmp_ods_tokopedia_sold_list_20240415_shop b on a.shop_id=b.shop_id where b.shop_id is null group by a.shop_url
#
#     '''