import asyncio
import random
import time
import requests_go
from common.proxy import get_proxy
from common.config import ja3_configs
from common.logger import logger,retry_loger
import json
from common.encrypt_tools import hash_o,get_random,cookie_to_json
from common.config import host
from tenacity import AsyncRetrying,retry, stop_after_attempt, after_log
from common.device_generation import DeviceGeneration
from common.config import get_gif_url,if_ja3
from curl_cffi.requests import AsyncSession



class Request:
    def __init__(self, proxy=True, headers=None,  timeout=10):

        self.timeout = timeout
        self.if_ja3 = if_ja3
        self._session_id = get_random(10)
        self.__ja3_config = random.choice(ja3_configs)
        # self.__ja3_config = ja3_configs[-1]
        self.tls_config = requests_go.tls_config.to_tls_config(self.__ja3_config)
        self.tls_config.ja3 = requests_go.tls_config.JA3Random(self.tls_config.ja3)
        self.session = requests_go.async_session()
        self.__metrics_counter__ = {}
        self.user_agent = self.__ja3_config.get("user_agent")
        self.anti = None
        self.pagePath = "/"
        self.location = "https://www.temu.com"
        self.page_id = ''
        if proxy:
            self.proxies = get_proxy(3)
        else:
            self.proxies = None
        if headers:
            self.user_agent = headers.get("User-Agent") or headers.get("user-agent")
            if not self.user_agent:
                self.user_agent = self.__ja3_config["user_agent"]
                headers["User-Agent"] = self.user_agent
            cookies = headers.pop("Cookie", '') or headers.pop("cookie", '')
            self.update_cookie(cookies)
            self.session.headers.update(headers)
        else:
            self.user_agent = self.__ja3_config["user_agent"]
        self.device = DeviceGeneration(self.get_headers())
        self.__event = {}
        self.T__anti = {}

    async def pmm_api(self, api, request_time, method, code,res_time,req,resp):
        timestamp = int(time.time() * 1000)
        rand_num = random.randint(100000, 900000)

        data = {
            "version": 0,
            "report_time_ms": timestamp,
            "rand_num": rand_num,
            "crc32": hash_o(f"{timestamp}-{rand_num}"),
            "biz_side": "consumer-platform-fe",
            "app": "100592",
            "common_tags": {
                "uid": "0",
                "osV": "unknown_",
                "pid": self.get_cookie("_bee"),
                "runningAppId": "100592",
                "runningPlatform": "-1",
                "p": "-1",
                "pagePath": self.pagePath
            },
            "datas": [
                {
                    "category": 1,
                    "type": 100,
                    "id_raw_value": api.split("?")[0],
                    "timestamp": request_time,
                    "tags": {
                        "network": "3",
                        "code": code,
                        "method": method,
                        "region": host[str(self.get_cookie("region"))].upper(),
                        "language": "en",
                        "language_locale": "unknown",
                        "currency": self.get_cookie("currency"),
                        "timezone": "Asia/Shanghai"
                    },
                    "lvalues": {
                        "rspT": {
                            "values": [
                                res_time
                            ]
                        },
                        "reqP": {
                            "values": [
                                len(req)
                            ]
                        },
                        "rspP": {
                            "values": [
                                len(resp)
                            ]
                        }
                    },
                    "extras": {
                        "srcPageId": self.page_id,
                        "user_agent": self.user_agent,
                        "app_version": "0",
                        "pageUrl": self.location,
                        "api_uid": self.get_cookie("api_uid"),
                    },
                    "api_ratio": 1
                }
            ]
        }
        url = 'https://us.pftk.temu.com/pmm/api/pmm/api'
        async for attempt in AsyncRetrying(stop=stop_after_attempt(3),reraise=True,after=retry_loger):
            with attempt:
                kwargs={}
                if self.if_ja3:
                    kwargs["tls_config"] = self.tls_config
                if self.proxies:
                    kwargs["proxies"] = self.proxies
                await self.session.post(url, json=data, verify=False,
                                        timeout=self.timeout, **kwargs)

    def get_event(self, event):
        page_event = self.__event.get(event["page_sn"], {})
        count = page_event.get(event['op'], 1)
        page_event[event['op']] = count + 1
        self.__event[event['page_sn']] = {event['op']:count}
        return count

    async def gif(self, event_list=None):
        region = self.get_cookie("region", "211")
        currency = self.get_cookie("currency", "USD")
        language = self.get_cookie("language", "en")
        api_uid = self.get_cookie("api_uid")

        bg_ud = self.get_cookie("_bee")
        nano = self.get_cookie("_nano_fp")
        njrpl = self.get_cookie("njrpl")
        dilx = self.get_cookie("dilx")
        hfsc = self.get_cookie("hfsc")
        width = self.device.screen[0]
        height = self.device.screen[1]
        req_event = []

        if bg_ud:
            gif_cookie = f'api_uid={api_uid}; _bee={bg_ud}; njrpl={njrpl}; dilx={dilx}; hfsc={hfsc}'
        else:
            gif_cookie = f'api_uid={api_uid}'
        for event in event_list:
            event_count = self.get_event(event)
            req_time = int(time.time() * 1000)
            dcf = hash_o(f"{req_time}{event}{event_count}")
            __metrics_counter = self.__metrics_counter__.get(event["page_sn"], 0)
            data = {
                "cli_timezone": "Asia/Shanghai",
                "cli_region": region,
                "cli_currency": currency,
                "cli_language": language,
                "_x_sessn_id": self._session_id,
                "time": req_time,
                "log_id": f"{req_time}{get_random(16)}",
                "user_id": self.get_cookie("user_uin"),
                "uin": self.get_cookie("user_uin"),
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
                "_ck_h_sequ": str(__metrics_counter),
                "support_beacon": "1"
            }
            self.__metrics_counter__[event["page_sn"]] = __metrics_counter + 1

            data.update(event)
            headers = {
                'accept': '*/*',
                'content-type': 'text/plain;charset=UTF-8',
                'origin': 'https://www.temu.com',
                'referer': 'https://www.temu.com/',
                "cookie": gif_cookie

            }
            req_event.append(self.post(get_gif_url(region),
                                               headers=headers,
                                               data=data))

        await asyncio.gather(*req_event)

    def up_server_time(self, server_time=None):

        for anti in self.T__anti.values():
            anti.up_server_time(server_time)

    def update_cookie(self, cookie):
        if not cookie:
            return
        if isinstance(cookie, str):
            cookie = cookie_to_json(cookie)
        self.session.cookies.update(cookie)

    async def get(self, *args,**kwargs):
        if self.if_ja3:
            kwargs["tls_config"] = self.tls_config
        url = kwargs.get("url") or args[0]
        logger.info(f"get: {url}")
        if self.proxies:
            kwargs["proxies"] = self.proxies
        anti = kwargs.pop("anti", {})
        if anti:
            _nano_fp = self.get_cookie("_nano_fp")
            api_uid = self.get_cookie("api_uid")
            anti["_nano_fp"] = _nano_fp
            anti["api_uid"] = api_uid
            anti_content = await self.get_anti(anti)
            headers = kwargs.get("headers", {})
            headers["anti-content"] = anti_content
            kwargs["headers"] = headers
        api = kwargs.pop("api", None)
        check = kwargs.pop("check", None)
        if api:
            request_time = int(time.time() * 1000)
            if kwargs.get("params"):
                req = {"params": kwargs["params"]}
            else:
                req = {}
            async for attempt in AsyncRetrying(stop=stop_after_attempt(3), reraise=True, after=retry_loger):
                with attempt:
                    resp = await self.session.get(verify=False,timeout=self.timeout, *args,**kwargs)
            await self.pmm_api(url, request_time, "GET", resp.status_code,
                               int(time.time()*1000)-request_time
                               ,json.dumps(req,separators=(',', ':')), resp.text)
        else:
            async for attempt in AsyncRetrying(stop=stop_after_attempt(3), reraise=True, after=retry_loger):
                with attempt:
                    resp = await self.session.get(verify=False, timeout=self.timeout, *args, **kwargs)
        if check and resp.json().get("error_code") == 54001:
            result = await check(resp)
            if result:
                logger.info("验证识别通过,重新请求")
                async for attempt in AsyncRetrying(stop=stop_after_attempt(3), reraise=True, after=retry_loger):
                    with attempt:
                        resp = await self.session.get(verify=False, timeout=self.timeout, *args, **kwargs)

        return resp

    # @retry(stop=stop_after_attempt(3),reraise=True, after=retry_loger)
    async def post(self, *args, **kwargs):
        if self.if_ja3:
            kwargs["tls_config"] = self.tls_config
        url = kwargs.get("url") or args[0]
        logger.info(f"post: {url}")
        if self.proxies:
            kwargs["proxies"] = self.proxies
        anti = kwargs.pop("anti", {})
        if anti:
            _nano_fp = self.get_cookie("_nano_fp")
            api_uid = self.get_cookie("api_uid")
            anti["_nano_fp"] = _nano_fp
            anti["api_uid"] = api_uid
            anti_content = await self.get_anti(anti)
            headers = kwargs.get("headers", {})
            headers["anti-content"] = anti_content
            kwargs["headers"] = headers

        api = kwargs.pop("api", None)
        check = kwargs.pop("check", None)

        if api:
            request_time = int(time.time() * 1000)
            req = {
                "params": {
                    "is_back": None,
                    "locale_override": None
                },
                "data": json.dumps(kwargs.get("data") or kwargs.get("json"), separators=(',', ':'))

            }
            async for attempt in AsyncRetrying(stop=stop_after_attempt(3), reraise=True, after=retry_loger):
                with attempt:
                    resp = await self.session.post(verify=False,timeout=self.timeout, *args, **kwargs)

            await self.pmm_api(url, request_time, "POST", resp.status_code,
                               int(time.time() * 1000) - request_time
                               , json.dumps(req, separators=(',', ':')), resp.text)
        else:
            async for attempt in AsyncRetrying(stop=stop_after_attempt(3), reraise=True, after=retry_loger):
                with attempt:
                    resp = await self.session.post(verify=False, timeout=self.timeout, *args, **kwargs)
        if check and resp.json().get("error_code") == 54001:
            result = await check(resp)
            if result:
                logger.info("验证识别通过,重新请求")
                async for attempt in AsyncRetrying(stop=stop_after_attempt(3), reraise=True, after=retry_loger):
                    with attempt:
                        resp = await self.session.post(verify=False, timeout=self.timeout, *args, **kwargs)

        return resp

    def set_anti(self,key, obj):
        self.T__anti[key] = obj

    async def get_anti(self, anti):
        key = anti.pop("key", None)
        T__anti_obj = self.T__anti.get(key)
        if not T__anti_obj:
            raise Exception(f"key->{key},没有设置anti")
        T__anti_obj.up_headers(self.get_headers())
        anti_content = await T__anti_obj.get_anti(**anti)
        anti["key"] = key
        return anti_content



    def get_cookie(self, name=None, default=""):
        if name:
            return self.session.cookies.get(name, default)
        return self.session.cookies.get_dict()

    def get_cookie_full(self):
        c = []
        for i in self.session.cookies:
            if i.domain =='temu.com':
                domain = '.temu.com'
            else:
                domain = i.domain or 'www.temu.com'
            c.append({
                "name": i.name,
                "value": i.value,
                "domain": domain,
            })
        return c

    def get_ua(self):
        return self.user_agent

    def get_headers(self):
        headers = self.session.headers.copy()
        headers["cookie"] = "; ".join([f"{k}={v}" for k,v in self.get_cookie().items()])

        return headers

    def update_headers(self, headers):
        if isinstance(headers, dict):
            self.session.headers.update(headers)
            if self.anti:
                self.anti.headers.update(headers)



if __name__ == '__main__':
    c = CRequest(
        {
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'upgrade-insecure-requests': '1',
            'cookie': 'region=211; language=en; currency=USD; timezone=Asia%2FShanghai; webp=1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'service-worker-navigation-preload': '2',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'zh-CN,zh;q=0.9',
            'priority': 'u=0, i',
        })
