# coding:utf-8

from urllib import parse
null = None
import time

import random
from verify.track.cBezier import bezierTrajectory
from common.encrypt_tools import AsyncAnti, captcha_encrypt,hash_o, cookie_to_json,get_random
from common.logger import logger
from verify.PDCaptch import PDCaptcha
from verify.doubleCaptch import DoubleCaptcha
from verify.click_captch import ClickCaptcha
from verify.slide_captch import SlideCaptcha
from tenacity import retry, stop_after_attempt, after_log
import logging
from common.Request import Request
from common.logger import retry_loger
verify_count = {
    "count": 0,
    "success": 0,
    "error": 0,
    "error_ide": 0,
}

bt = bezierTrajectory()


class VerifyCaptcha(object):
    def __init__(self, headers, cookie=None, session=None, proxy=True, ):
        self.headers = headers.copy()
        self.refer = {}
        cookie = cookie or headers.get("cookie") or headers.get("Cookie")
        if not isinstance(cookie, dict):
            cookie = cookie_to_json(cookie)

        self.VerifyAuthToken = (headers.get("Verifyauthtoken") or headers.get("verifyauthtoken")
                                or cookie.get("verifyauthtoken"))
        if not self.VerifyAuthToken:
            raise "没有VerifyCaptcha"
        self.session = session or Request(proxy=proxy, headers=self.headers)

        referer = headers.get("referer", headers.get("Referer", ''))
        if 'bgn_verification' not in referer:
            self.session.update_headers({"referer": f"https://www.temu.com/bgn_verification.html?Verif"
                                                   f"yAuthToken={self.VerifyAuthToken}&from={parse.quote_plus(referer)}"})
        self.img_info = {}
        self.page_sn = "10017"
        self.page_id = f"10017_{int(time.time()*1000)}_{get_random(10)}"
        self.session.set_anti('verify',AsyncAnti(self.session.get_headers(),
                             lt_c=[169, 166, 24, 25],
                             gt_c=[186, 127, 72, 47],
                             _=[132, 169, 150, 34]))


    async def get_init(self):
        url = "https://www.temu.com/api/phantom/vc_pre_ck"
        data = {
            "sdk_type": 1,
            "client_time": int(time.time() * 1000),
            "verify_auth_token": self.VerifyAuthToken,
        }

        resp = await self.session.post(url=url, json=data, anti={
            "key": "verify"
        })

        return resp.json()

    async def gif(self):
        referer = self.session.get_headers().get("referer", 'https://www.temu.com')
        referer_info = parse.parse_qs(referer)

        env_list = [
            {
                "page_sn": self.page_sn,
                "page_id": self.page_id,
                "page_url": self.headers.get("referer"),
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
        ]
        if referer_info.get("refer_page_sn"):
            for env in env_list:
                env.update({"refer_page_sn": referer_info["refer_page_sn"][0]})
        if referer_info.get("refer_page_name"):
            for env in env_list:
                env.update({"refer_page_name": referer_info["refer_page_name"][0]})
        if referer_info.get("refer_page_id"):
            for env in env_list:
                env.update({"refer_page_id": referer_info["refer_page_id"][0]})
        await self.session.gif(env_list)


    @retry(stop=stop_after_attempt(20), reraise=True,
           after=retry_loger)
    async def start(self):
        logger.info(f"验证码识别开始,token->{self.VerifyAuthToken}")
        # await self.session.get(self.headers.get("referer"))
        await self.gif()
        init_info = await self.get_init()
        if not init_info["success"]:
            return False
        captcha = await self.get_captcha(init_info)
        if captcha["type"] == 23:
            logger.info("滑动验证码开始滑动")
            sc = SlideCaptcha(init_info, self.VerifyAuthToken, session=self.session)
            res = await sc.slide_captcha(captcha)
            return res

        elif captcha["type"] == 11:
            logger.info("点选验证码开始")

            cc = ClickCaptcha(init_info, self.VerifyAuthToken, session=self.session,)
            res = await cc.verify(captcha)
        elif captcha["type"] == 41:
            logger.info("拼图验证码开始滑动")

            pd = PDCaptcha(init_info,self.VerifyAuthToken, session=self.session)
            res = await pd.verify(captcha)
        elif captcha["type"] == 12:
            logger.info("双图验证码开始滑动")
            dc = DoubleCaptcha(init_info,self.VerifyAuthToken, session=self.session)
            res = await dc.verify(captcha)
        elif captcha['type'] == 25:
            logger.info("滑动椭圆验证码开始滑动")
            return False
        else:
            raise Exception(f"验证码返回不对.{captcha}")
        if res:
            logger.info(f"验证识别通过")
            return True
        raise Exception("验证失败")

    async def get_captcha(self, init_info):
        logger.info("开始获取验证吗")
        screen = {"w": 1980, "h": 1080}
        data = {
            "v": "a",
            "ts": init_info["server_time"],
            "t0": int(time.time() * 1000),
            "tp": 1,
            "ua": self.headers.get("user-agent") or self.headers.get("User-Agent"),
            "rf": self.headers.get("Referer") or self.headers.get("referer"),
            "hl": "000000000001010",
            "sc": screen,
            "ihs": 1,
            "platform": 1,
        }
        captcha_collect = await captcha_encrypt(data, init_info)

        response = await self.session.post(
            "https://www.temu.com/api/phantom/obtain_captcha",
            json={
                "verify_auth_token": self.VerifyAuthToken,
                "captcha_collect": captcha_collect["data"],
                "salt": init_info["salt"],
                "reverse": False,
                "encrypt_version": 1,
            },
            anti={
              "key": "verify"
            }
        )

        return response.json()


if __name__ == '__main__':

    vc = VerifyCaptcha(

        headers={
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'zh-CN,zh;q=0.9',
            'anti-content': '0aqWfqlv0jTaF992_8uJfJysVaM8-3rj3kI5GG4iwT5_izIeOV22Y83i-KK-HHPLQZTu69ZrVLQX5kQtZkEstgUuEgaryyorR7ioTsyG1zRYVJpmZwsJvzkUhle5IUEFRH4F8OcoJ12QLYfL5_5a1CuqQTX_3iGvhZsH5JDjntmcAvFb9BLnnlw64HzbHrm4tuKVzZdgszlZQogvnJkkFAbRDRW041FjlGPo881xqcXEHMCCfRa1Z6g4GcenLB7ayeQX55BII4uHZoe_lHhenv3BrLsfBsfk8qqXNH5FSsQkg84P6ontPDPhL259azGu9Mn22yoVmLQ3y9Z40Vi1HzcsOFDn5pFVRq8kkAJ3VsSmwK8DXyc3O4DQj1GkvEzfCVfug4D1nlRPKQOgJZifJ48CGjbrVWlgiRhN5y6fxzIlChE1YDhxpsEphrjo3yJnJtRYy7XCkiRQrEMaDGUgHPCmV1JmJESJsISZzeRTxxrplRNJQBSjiw6ZtDe4Pp1-5Pt',
            'cache-control': 'no-cache',
            'content-type': 'application/json;charset=UTF-8',
            'cookie': 'language=en; region=211; language=zh-Hans; currency=USD; api_uid=Cm0EX2aaRqIohQBLjHDeAg==; timezone=Asia%2FShanghai; webp=1; _nano_fp=XpmxXpXJn5EjnpdYnT_lJX4yNeHfxzZT4bwql1Fh; _bee=xCPjyk0lIP2Wq7eiTV0paKZypBKzSapm; njrpl=xCPjyk0lIP2Wq7eiTV0paKZypBKzSapm; dilx=P4i38O01nkPw1rU98JVWh; hfsc=L3yIeYo47zj/05DMcQ==; verifyAuthToken=TbByplp3v9qqoU1_ERhuqQea04513e2934ca729; _ttc=3.M4myHQKXz6Qj.1752922675',
            'origin': 'https://www.temu.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.temu.com/bgn_verification.html?VerifyAuthToken=TbByplp3v9qqoU1_ERhuqQea04513e2934ca729&from=https%3A%2F%2Fwww.temu.com%2Flogin.html%3Flogin_scene%3D8%26from%3Dhttps%3A%2F%2Fwww.temu.com%2Fbest-of-asia-by--m-634418213975418.html&type=iframe&iframeMsgId=6pfpuuqp4q9g703c5mcxo',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'verifyauthtoken': 'TbByplp3v9qqoU1_ERhuqQea04513e2934ca729',
        },
        proxy=False
    )
    import asyncio
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(vc.start())
