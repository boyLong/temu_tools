import uuid
from common.CRequest import CRequest
from common.Request import Request
from verify.verify import VerifyCaptcha
from common.encrypt_tools import AsyncAnti,get_nano,cookie_to_str
from common.device_generation import DeviceGeneration
import random
import asyncio
import re
import time
from urllib.parse import quote_plus


class Spider(object):

    def __init__(self,headers=None, proxy=True, session=None):
        headers.pop("Host", None)
        headers.pop("host", None)




        self.session = session or CRequest(headers=headers,proxy=proxy)
        # self.session.set_anti(AsyncAnti(self.session.get_headers(),
        #                                 lt_c=[169, 166, 24, 25],
        #                                 gt_c=[186, 127, 72, 47],
        #                                 _=[132, 169, 150, 34]))
        self.device = DeviceGeneration(self.session.get_headers(),)
        self.page_name = ""
        self.page_id = ""
        self.page_sn = ""

    async def check_verify(self, resp):
        referer = self.session.get_headers().get('Referer', 'https://www.temu.com')
        verify_auth_token = resp.json().get("verify_auth_token")
        self.session.update_headers({
            "verifyauthtoken": verify_auth_token,
            "referer": f"https://www.temu.com/bgn_verification.html?VerifyAuthToken={verify_auth_token}&from="
                       f"{quote_plus(referer)}&refer_page_name={self.page_name}&refer_page_id={self.page_id}"
                       f"&refer_page_sn={self.page_sn}&_x_sessn_id={self.session._session_id}",

        })
        self.session.update_cookie({
            "verifyAuthToken": resp.json().get("verify_auth_token"),
        })
        vc = VerifyCaptcha(
            headers=self.session.get_headers(),
            session=self.session,
        )

        res = await vc.start()
        if "?" in referer:
            self.session.update_headers(
                {"referer": referer}
            )
        else:
            self.session.update_headers({
                "referer":  f'{referer}?_x_sessn_id={self.session._session_id}&refer_page_name=bgn_verification&'
                            f'refer_page_id={vc.page_id}&refer_page_sn={vc.page_sn}',
            })
        return res


    async def get_nano(self):
        if self.session.get_cookie("_nano_fp"):
            return self.session.get_cookie("_nano_fp")
        nano = await get_nano()
        self.session.update_cookie({"_nano_fp": nano})
        return nano

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

        await asyncio.gather(*[self.session.get("https://www.temu.com/api/phantom/dm/wl/cg"),
            self.session.get("https://www.temu.com/api/phantom/xg/pfb/a3"),
            self.session.get("https://www.temu.com/api/phantom/xg/pfb/b")])

        a4 = await self.device.a4()
        await self.session.post("https://www.temu.com/api/phantom/xg/pfb/a4", json=a4)
        await self.session.get("https://www.temu.com/us-zh-Hans/api/adx/cm/ttc?scene=1&type=0")

    def parse_email_code(self, email_info):
        email_code = re.findall('\d{6}', email_info["subject"])
        return email_code[0]

    async def home_good(self,):
        listid = uuid.uuid4().hex
        params = (
            ('extend_fields', '{}'),
            ('offset', '0'),
            ('count', '120'),
            ('list_id', listid),
            ('listId', listid),
            ('scene', 'home'),
            ('page_list_id', uuid.uuid4().hex),
        )
        url = 'https://www.temu.com/api/alexa/homepage/goods_list'
        resp = await self.session.get(url, params=params)

    async def start(self):
        await self.a4()
        cookie = self.session.get_cookie_full()
        await self.home_good()
        print(cookie)


if __name__ == '__main__':

    s = Spider(
        headers = {
            'Host': 'www.temu.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'service-worker-navigation-preload': '2',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'zh-CN,zh;q=0.9',
            'priority': 'u=0, i',
        },
    )

    asyncio.run(s.start())