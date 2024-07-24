import json
import re
import time
import asyncio
from asyncio import WindowsSelectorEventLoopPolicy
asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())
from common.encrypt_tools import get_random,password_encrypt,AsyncAnti,get_email
from common.logger import logger
from common.config import get_dr
from common.account_manage import get_account_info
from spider import Spider


from common.redis_handler import redis_client


class LoginSpider(Spider):

    def __init__(self,headers, proxy, username=None, password=None):
        super(LoginSpider, self).__init__(headers,proxy)
        self.username = username or f"{get_random(10)}@qq.com"
        self.password = password or username
        self.page_sn = '10013'
        self.page_name = 'login'
        self.page_id = f'10013_{int(time.time()*1000)}_{get_random(10)}'
        self.referer = headers.get("referer") or headers.get("Referer") or ''
        aa = AsyncAnti(self.session.get_headers(),
                       lt_c=[169, 166, 24, 25],
                       gt_c=[186, 127, 72, 47],
                       _=[132, 169, 150, 34])

        self.session.set_anti('login', aa)

    async def get_account(self):
        username, password = await get_account_info()
        self.username = username
        self.password = password

    async def registered(self):
        e = [
            {
                "page_sn": self.page_sn,
                "page_id": self.page_id,
                "login_scene": "8",
                "page_el_sn": "200296",
                "op": "click",
            },
            {
                "page_sn": self.page_sn,
                "page_id": self.page_id,
                "login_scene": "8",
                "page_el_sn": "200072",
                "login_phone_or_email": "2",
                "op": "click",
            }
        ]
        await self.session.gif(e)
        url = 'https://www.temu.com/api/bg/sigerus/auth/login_name/is_registered'
        data = {"login_app_id": 203,
                "login_name": self.username,
                "login_scene": 8,
                "support_mobile": False,
                "components_version": "0.9.11"}

        resp = await self.session.post(url=url, json=data,
                                       anti={
                                           "event": True,
                                           "key": "login",
                                           "element": "submit-button"
                                       },
                                       check=self.check_verify
                                       )
        data = resp.json()
        if data.get("error_code") and data["success"]:
            return True
        else:
            return False

    async def index(self,url):
        resp = await self.session.get(url)
        self.device.reload(text=resp.text)
        # self.device.reload(headers=self.session.get_headers())
        await asyncio.gather(*[self.get_nano(), self.server_time()])
        self.session.update_headers({
            "referer": url
        })
        env_list = [
            {
                "page_sn": self.page_sn,
                "page_id": self.page_id,
                "page_url": url,
                "refer_url": "",
                "op": "pv",
                "event": "page_show",
            },
            {
                "page_sn": self.page_sn,
                "page_id": self.page_id,
                "page_el_sn": "225383",
                "is_show": "0",
                "ndisp_rsn": "1",
                "op": "impr",
            },
            {
                "page_sn": self.page_sn,
                "page_id": self.page_id,
                "login_scene": "8",
                "page_el_sn": "201249",
                "op": "impr",
            },
            {
                "page_sn": self.page_sn,
                "page_id": self.page_id,
                "login_scene": "8",
                "page_el_sn": "200070",
                "op": "impr",
            }
        ]
        await self.session.gif(env_list)

    async def login(self):
        await self.index("https://www.temu.com/login.html?login_scene=8")
        await self.a4()

        is_registered = await self.registered()

        if not is_registered:

            raise Exception("无法注册")

        data = {"login_app_id": 203, "login_name": self.username}

        resp = await self.session.post(
            "https://www.temu.com/api/bg/sigerus/auth/pub_key/request",
            anti={
                  "event": True,
                  "key": "login",
                  "element": "submit-button"
            },
            json=data,
        )
        pub_info = resp.json()["result"]
        region = self.session.get_cookie("region")
        enc_password = password_encrypt(pub_info, self.password)
        data = {
            "frontend_dr": get_dr(region),
            "login_type": 1,
            "login_app_id": 203,
            "login_scene": 8,
            "sign": pub_info["sign"],
            "key_version": pub_info["key_version"],
            "email": self.username,
            "password": enc_password,
            "is_login": False,
            "stay_signed_in": False,
            "login_source": 0,
            "password_level": 4,
            "components_version": "0.9.11",
        }
        resp = await self.session.post("https://www.temu.com/api/bg/sigerus/auth/login", anti={
            "event": True,
            "key": "login",
            "element": "submit-button"
        },json=data, check=self.check_verify)
        res_data = resp.json()
        logger.info("登录请求成功,检测结果")
        if res_data.get("error_code") == 54016:
            logger.info("登录需要邮箱验证码")
            verify_res = await self.obtain_captcha(res_data["verify_auth_token"])
            if verify_res:
                logger.info("邮箱验证成功开始二次登录")
                "https://www.temu.com/api/bg/sigerus/auth/verify_risk_login"
                data = {
                    "login_type": 1,
                    "login_app_id": 203,
                    "login_scene": 8,
                    "sign": pub_info["sign"],
                    "key_version": 57,
                    "email": self.username,
                    "password": enc_password,
                    "is_login": True,
                    "stay_signed_in": False,
                    "login_source": 0,
                    "verify_auth_token": res_data["verify_auth_token"]
                }
                resp = await self.session.post("https://www.temu.com/api/bg/sigerus/auth/verify_risk_login", anti={
                    "event": True,
                    "key": "login",
                }, json=data)
                res_data = resp.json()
                if res_data.get("error_code") == 1000000:
                    logger.info("登录成功")

                    return True
        elif res_data.get("error_code") == 1000000:

            return True
        else:
            print(res_data)
        return False

    async def obtain_captcha(self, verify_auth_token):
        anti = await self.session.get_anti({
            "key": "login",
            "event": True,
        })
        data = {"captcha_collect": "", "verify_auth_token": verify_auth_token,
                "anti_content": anti}
        timestamp = time.time()
        resp = await self.session.post("https://www.temu.com/api/phantom/obtain_captcha", json=data, headers={
            "referer": "https://www.temu.com/bgn_login_verification.html?"
                       f"VerifyAuthToken={verify_auth_token}&from=%2F&type=iframe&skipRiskLogin=1"
        })
        res_data = resp.json()

        if res_data.get("code") == 0:
            logger.info("开始获取邮箱验证码")
            email_info = await get_email(self.username,self.password, timestamp)
            email_code = self.parse_email_code(email_info)
            anti = await self.session.get_anti({
                "key": "login",
                "event": True,
            })
            data = {"verify_code": str(email_code), "verify_auth_token": verify_auth_token,
                    "anti_content": anti}

            resp = await self.session.post("https://www.temu.com/api/phantom/user_verify", json=data, headers={
                "referer": "https://www.temu.com/bgn_login_verification.html?"
                           f"VerifyAuthToken={verify_auth_token}&from=%2F&type=iframe&skipRiskLogin=1"
            })
            res_data = resp.json()
            if res_data.get("code") == 0:
                return True
        raise Exception("邮箱验证失败")

    async def start(self):

        login_status = await self.login()
        await self.a4()
        if not login_status:
            return False

        self.session.update_headers({
            "referer": f"https://www.temu.com/login.html?refer_page_name=login&"
                       f"refer_page_id={self.page_id}&refer_page_sn={self.page_sn}&_x_sessn_id={self.session._session_id}"
        })
        print(self.session.get_cookie_full())
        print(json.dumps(dict(self.session.get_headers()), indent=2))
        # await redis_client.sadd("temu_account", f"{self.username}---{self.password}")
        return dict(self.session.get_headers())


if __name__ == '__main__':
    s = LoginSpider(
        headers = {
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'upgrade-insecure-requests': '1',
            'cookie': 'region=211; language=en; currency=USD; timezone=Asia%2FShanghai; webp=1',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'service-worker-navigation-preload': '2',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'zh-CN,zh;q=0.9',
            'priority': 'u=0, i',
        },
        username="hs2214@burning.icu",
        password="temu_data@123123",
        proxy=True
    )
    asyncio.run(s.start())
