import re
import time
import json
from common.encrypt_tools import get_random,password_encrypt,AsyncAnti
from common.config import get_dr
from common.account_manage import get_account_info
from spider import Spider
import asyncio


class ShopSpider(Spider):

    def __init__(self,headers,proxy, shop_url):
        super(ShopSpider, self).__init__(headers,proxy)
        self.shop_url = shop_url

        mall_id = re.findall("-(\d+)\.", self.shop_url)
        if mall_id:
            self.mall_id = int(mall_id[0])
        else:
            self.mall_id = ''
        self.page_sn="10040"
        self.page_name='mall'
        self.page_id=f"10040_{int(time.time()*1000)}_{get_random(10)}"
        self.anti = AsyncAnti(self.session.get_headers(),
                  lt_c=[111, 225, 254, 180],
                  gt_c=[252, 195, 171, 91],
                  _=[134, 80, 158, 30])
        self.session.set_anti("shop", self.anti)

    async def index(self,url):
        await self.session.get(url,api=False)
        self.session.update_headers({
            "referer": url
        })
        env_list = [
            {
                "mall_id": self.mall_id,
                "page_sn": self.page_sn,
                "page_id": self.page_id,
                "page_url": url,
                "refer_url": "",
                "op": "pv",
                "event": "page_show",
            },
            {
                "mall_id": self.mall_id,
                "page_sn": self.page_sn,
                "page_id": self.page_id,
                "page_el_sn": "225383",
                "is_show": "0",
                "ndisp_rsn": "1",
                "op": "impr",
            },
            {
                "mall_id": self.mall_id,
                "page_sn": self.page_sn,
                "page_id": self.page_id,
                "page_el_sn": "213742",
                "op": "impr",
            },
            {
                "mall_id": self.mall_id,
                "page_sn": self.page_sn,
                "page_id": self.page_id,
                "page_el_sn": "201268",
                "op": "impr",
                "is_fav": "false",
            },
            {
                "mall_id": self.mall_id,
                "page_sn": self.page_sn,
                "page_id": self.page_id,
                "page_el_sn": "201269",
                "op": "impr",
            },
            {
                "mall_id": self.mall_id,
                "page_sn": self.page_sn,
                "page_id": self.page_id,
                "page_el_sn": "204398",
                "op": "impr",
            },
            {
                "mall_id": self.mall_id,
                "page_sn": self.page_sn,
                "page_id": self.page_id,
                "page_el_sn": "206581",
                "op": "impr",
            },

        ]
        await self.session.gif(env_list)

    async def start(self):
        await self.index(self.shop_url)
        url = 'https://www.temu.com/us-zh-Hans/api/bg/circle/c/mall/mallInfoWithGoodsList'
        data = {
            "mallId": self.mall_id,
            "mall_id": self.mall_id,
            "filter_items": "",
            "page_number": 1,
            "page_size": 60,
            "list_id": get_random(21),
            "scene_code": "mall_rule",
            "page_sn": 10040,
            "page_el_sn": 201265,
            "source": 10018,
            "anti_content": ""
        }
        response = await self.session.post(url,
                                         json=data, check=self.check_verify,
                                         anti={"event": False, 'key':"shop"},
                                        )

        # print(response.text)
        print(json.dumps(dict(self.session.get_headers()), indent=2))
        # print(self.session.get_cookie())
        print(self.session.get_cookie_full())
        if response.json().get("errorCode") == 1000000:
            return self.session.get_headers()
        else:
            print(response.text)
            raise Exception("cookie校验失败")


if __name__ == '__main__':
    s = ShopSpider(
        {
            "pragma": "no-cache",
            "cache-control": "no-cache",
            "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "upgrade-insecure-requests": "1",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "service-worker-navigation-preload": "2",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "navigate",
            "sec-fetch-user": "?1",
            "sec-fetch-dest": "document",
            "accept-language": "zh-CN,zh;q=0.9",
            "priority": "u=0, i",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42 Config/92.2.1891.92",
            "verifyauthtoken": "HPbmVur6QN3JNFj3RytlJg3b18760e5972b566a",
            "referer": "https://www.temu.com/login.html?refer_page_name=login&refer_page_id=10013_1721725568839_nnp9fervge&refer_page_sn=10013&_x_sessn_id=ufreknt2sp",
            "cookie": "_nano_fp=XpmxXpmxnpd8X0djnC_1uGRitt6y1g8EFfg_~iw~; currency=USD; language=en; region=211; timezone=Asia%2FShanghai; verifyAuthToken=HPbmVur6QN3JNFj3RytlJg3b18760e5972b566a; webp=1; AccessToken=KEHGD6FUAOPXJ4KJYJVRLRBIS5AD2XKM2LY7GAJ5MLETTOLG3I5A0110d3c3de9d; __cf_bm=a2NUQrSr5FGfCA6rlGKOm37.5YKnJFZ1WMkO3u9cvpw-1721725565-1.0.1.1-OR7xermS74ubEsUCVsf1Ygikn2bZtPoaLdc9i5fgMSN0gBQe984RtE9_q7blMpsCb2prUoErA07.fCrviQjWEg; _bee=nIxhtAQXZIUgJMQH1OqN4IbvnuzUzaph; _device_tag=CgI2WRIIWG9MU3RkbnkaMJylR6VkgUPiCgS5sOPocMh8hcJtyW7NIx3H92JDMR52k64ZYogVSw6JgFF0lRzKnjAC; api_uid=Cm1sL2afcn05mwBGEHrJAg==; dilx=OayFTOqJJOf4Iz6cZIrDw; hfsc=L3yIeY4y7Dv+2pHNfQ==; isLogin=1721725600471; njrpl=nIxhtAQXZIUgJMQH1OqN4IbvnuzUzaph; user_uin=BDNPASQAXFL3VFDZBR7OHDVEFOEICMYHBM5FEWNU; _ttc=3.A9gPXDtJOXUo.1753261570"
        }
        ,
            proxy=False,
            shop_url="https://www.temu.com/d-o-y-o-local-m-634418216666955.html?refer_page_name=login&refer_page_id=10013_1721725568839_nnp9fervge&refer_page_sn=10013&_x_sessn_id=ufreknt2sp"
    )
    asyncio.get_event_loop().run_until_complete(s.start())