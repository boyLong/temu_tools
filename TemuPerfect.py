# -*- coding: utf-8 -*-
import re
import asyncio
from urllib.parse import quote_plus, urlparse, parse_qs, urlencode
import secrets
import time
import random
import json
import hmac
import hashlib
from common.logger import logger
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
from common.verify_captcha import VerifyCaptcha
from common.encrypt_tools import AsyncAnti, get_nano, hash_o,get_random
from common.device_generation import DeviceGeneration
from common.request import AsyncRequest
from common.config import get_gif_url, get_dr


def encrypt(text, pubkey):
    public_key = f"""-----BEGIN PUBLIC KEY-----
    {pubkey}
    -----END PUBLIC KEY-----"""
    pub_key = RSA.importKey(public_key)
    cipher = PKCS1_cipher.new(pub_key)
    rsa_text = cipher.encrypt(text.encode("utf-8)")).hex()  # 加密并转为b64编码
    return rsa_text


def get_username():
    return f"{get_id(random.randint(10, 20))}@gmail.com"


def get_password():
    return 'temu_shop_123123'


def get_id(e=21):
    chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    return "".join(secrets.choice(chars) for _ in range(e))


class TemuPerfect:
    def __init__(
            self,
            href="https://www.temu.com/",
            headers=None,
            detail=False,
            gif=True,
            login=True,

    ):
        self.anti = None
        self.session = AsyncRequest(proxy=True, headers=headers)
        self.device = DeviceGeneration(self.session.get_headers())
        self._session_id = get_id(10)
        self.page_id = f"10005_{int(time.time() * 1000)}_{get_id(10)}"
        self.__event = {}
        self.__metrics_counter__ = 0
        self.__location = href
        self.__server_time = {}
        self.detail=detail
        self.need_gif=gif
        self.need_login=login
        self.login_name = ""
        self.password = ''


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

    async def start(self):
        resp = await self.index(self.__location)
        text = resp.text
        try:
            raw_data = re.findall("window\.rawData=(.*?\});", text)[0]
            raw_data = json.loads(raw_data)
            self.home_page_list_id = raw_data['store']['pageListId']
            self.goods_list_id = raw_data['store']['recGoodsListId']
        except:
            if 'forReturnSubTitle' not in text:
                raise Exception('获取首页raw_data失败, 设备权重过低,不在继续')
            raw_data = {}

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
        if raw_data:
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
        else:
            logger.info("raw_data为空逻辑走注册")
            if self.need_login:
                res = await self.register()
                if res:
                    if self.detail:
                        res = await self.check_detail()
                        if not res:
                            raise Exception("详情验证失败了")
                    return {
                        "headers": self.session.get_headers(),
                        "account": self.login_name,
                        "password": self.password,
                        "proxy": self.session.proxies
                    }
                else:
                    raise Exception('注册失败')
            else:
                raise Exception("设备权重低但不需要登录")

        await self.gif(event_list)
        logger.info(f'开始验证')
        await self.session.get('https://www.temu.com/api/adx/cm/ttc?scene=1&type=0')
        resp = await self.session.post("https://www.temu.com/api/poppy/v1/opt?scene=opt_floating_layer_rec",anti={"event": False},
                                        verify=self.verify,
                                        json = {"scene":"opt_floating_layer_rec",
                                               "listId":get_id(6),
                                               "pageListId":raw_data['store']['layoutData']["commonData"]["pageListId"],
                                               "optId":-13,
                                               "optType":1,"offset":0,"pageSize":5}
                                       )
        if resp.status_code != 200 or not resp.json().get("success"):
            if self.need_login:
                if resp.status_code == 403 and resp.json().get("error_code") == 40001:
                    res = await self.register()
                    if res:
                        if self.detail:

                            res = await self.check_detail()
                            if not res:
                                raise Exception("详情验证失败了")
                        return {
                            "headers": self.session.get_headers(),
                            "account": self.login_name,
                            "password": self.password,
                            "proxy": self.session.proxies,
                            "href": self.__location
                        }
                    else:
                        raise Exception('注册失败')
            else:
                raise Exception('验证失败,设备权重过低,不在继续')
            raise Exception(f'获取opt_list失败,不在继续,{resp.text}')

        if self.detail:
            res = await self.check_detail()
            if not res:
                raise Exception("详情验证失败了")
        # 不需要详情
        return {
            "headers": self.session.get_headers(),
            "account": self.login_name,
            "password": get_password(),
            "proxy": self.session.proxies,
            "href": self.__location
        }



    async def check_detail(self,):
        url = 'https://www.temu.com/api/alexa/homepage/goods_list'
        params = (
            ('extend_fields', '{}'),
            ('offset', '0'),
            ('count', '120'),
            ('list_id', self.goods_list_id),
            ('opt_id', '25'),
            ('listId', self.goods_list_id),
            ('scene', 'home'),
            ('page_list_id', self.home_page_list_id),
        )
        resp = await self.session.get(url, anti={"event": False}, params=params, verify=self.verify)
        res_data = resp.json()
        seo_link_url = res_data.get('result')["home_goods_list"][0]["data"]["seo_link_url"]
        info = urlparse(seo_link_url)
        query = parse_qs(info.query)
        path = info.path
        new_query = {
        }
        for k, v in query.items():
            new_query[k] = v[0]
        new_query.update({
            "refer_page_sn":"10005",
            "refer_page_el_sn": "200024",
            "refer_page_name": "home",
            "refer_page_id": self.page_id,
            "_x_sessn_id": self._session_id

        })
        logger.info(f"校验商品接口")
        href = "https://www.temu.com"+path+"?"+urlencode(new_query)

        html = await self.index(href=href)
        try:

            raw_data = re.findall("window\.rawData=(.*?\});", html.text)[0]
            raw_data = json.loads(raw_data)
            if raw_data["store"].get("error"):
                logger.info(f'校验商品接口出现验证吗')
                if raw_data["store"]["error"]["errorCode"] == 54001:
                    verify_auth_token = raw_data["store"]["error"]["errorCode"]
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
                        "referer": self.__location,
                    })
                    if res:
                        return True
                    else:
                        raise Exception('校验商品接口验证码失败')
                else:
                    raise Exception(f'校验商品风控失败->{raw_data["store"]["error"]["errorCode"]}')
            else:
                if raw_data["store"].get('goods',{}).get("sideSalesTip",''):
                    return True
                else:
                    raise Exception('校验商品出现风控了')
        except:
            raise Exception('校验商品接口失败')


    async def register(self):
        href = ("https://www.temu.com/login.html?from=https%3A%2F%2Fwww.temu.com%2F&login_scene="
                           f"2&refer_page_name=home&refer_page_id={self.page_id}&"
                           f"refer_page_sn=10005&_x_sessn_id={self._session_id}")
        await self.index(href)

        self.__metrics_counter__ = 0
        envent = [
            {
                "refer_page_name": "home",
                "refer_page_id": self.page_id,
                "refer_page_sn": "10005",
                "page_url": self.__location,
                "refer_url": "https://www.temu.com/",
                "op": "pv",
                "event": "page_show",
            },
            {
                "refer_page_name": "home",
                "refer_page_id": self.page_id,
                "refer_page_sn": "10005",
                "page_el_sn": "225383",
                "is_show": "0",
                "ndisp_rsn": "1",
                "op": "impr",
            }
        ]

        logger.info(f'开始注册')
        await asyncio.gather(*[self.server_time(),self.a4(), self.gif(event_list=envent), self.gif([
            {
                "login_scene": "2",
                "page_el_sn": "200070",
                "op": "click",
            }, {
                "login_scene": "2",
                "page_el_sn": "200070",
                "op": "click",
            }])])

        url = "https://www.temu.com/api/bg/sigerus/auth/login_name/is_registered"
        self.login_name = get_username()
        self.password = get_password()
        login_name = self.login_name
        data = {
            "login_app_id": 203,
            "login_name": login_name,
            "support_mobile": True,
            "components_version": "0.8.0",
            "login_scene": 2
        }
        resp = await self.session.post(url, anti={"event": True}, verify=self.verify, json=data)
        if not resp.json()["success"]:
            raise Exception(f"注册被风控 {resp.text}")
        logger.info(f'{login_name}账号可以注册')
        data = {"login_app_id": 203, "login_name": login_name}

        resp = await self.session.post(
            "https://www.temu.com/api/bg/sigerus/auth/pub_key/request",
            anti={"event": True, "element": "submit-button"},
            json=data,
        )
        pub_info = resp.json()["result"]
        password = self.password
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
            "login_scene": 2,
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
                                           "event": True,
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

                return res
            else:
                raise Exception(f'登录成功,但是没通过校验')
        else:
            logger.info(f'{login_name}登录失败')
    async def account_risk_test(self):
        logger.info(f'开始验证账号风控')
        url = (f"https://www.temu.com/?refer_page_name=login&refer_page_id={self.page_id}&"
               f"refer_page_sn=10013&_x_sessn_id={self._session_id}")
        resp = await self.index(url)
        text = resp.text
        try:
            raw_data = re.findall("window\.rawData=(.*?\});", text)[0]
            raw_data = json.loads(raw_data)
            self.home_page_list_id = raw_data['store']['pageListId']
            self.goods_list_id = raw_data['store']['recGoodsListId']
        except:
            raise Exception('登录后获取首页raw_data失败, 不在继续')
        await self.a4()
        resp = await self.session.post("https://www.temu.com/api/poppy/v1/opt?scene=opt_floating_layer_rec",anti={"event": False},
                                        verify=self.verify,
                                        json = {"scene":"opt_floating_layer_rec",
                                               "listId":get_id(6),
                                               "pageListId":raw_data['store']['layoutData']["commonData"]["pageListId"],
                                               "optId":-13,
                                               "optType":1,"offset":0,"pageSize":5}
                                       )

        if resp.json()["success"]:
            logger.info(f'账号风控验证成功')
            return True
        else:
            raise Exception(f"风控验证失败,{resp.text}")

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

    t = TemuPerfect(href="https://www.temu.com/", headers=headers,
             detail=False,login=True
                   )

    async def test():


        r = await t.start()
        print(r)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(test())

#     '''
# select a.shop_url from tmp.tmp_ods_tokopedia_sold_list_20240415_shop2 a left join tmp.tmp_ods_tokopedia_sold_list_20240415_shop b on a.shop_id=b.shop_id where b.shop_id is null group by a.shop_url
#
#     '''
