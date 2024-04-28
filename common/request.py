import asyncio
import random
import requests_go
from common.proxy import get_proxy
from common.config import ja3_configs
from common.logger import logger
import stamina
import json
from requests_go.tls_client.exceptions import TLSClientExeption,RequestException
from requests.exceptions import (
    ConnectionError,
    ConnectTimeout,
    InvalidHeader,
    InvalidProxyURL,
    InvalidSchema,
    InvalidURL,
    ProxyError,
    ReadTimeout,
    RetryError,
    SSLError,

)

retry_on = (Exception,
            ConnectionError,
            ConnectTimeout,
            InvalidHeader,
            InvalidProxyURL,
            InvalidSchema,
            InvalidURL,
            ProxyError,
            ReadTimeout,
            RetryError,
            SSLError,
            json.decoder.JSONDecodeError,
            TLSClientExeption,
            RequestException

            )

class AsyncRequest:
    def __init__(self, proxy=True, headers=None, if_ja3=True,timeout=10):
        self.__ja3_config = random.choice(ja3_configs)
        self.timeout = timeout
        self.if_ja3 = if_ja3
        self.tls_config = requests_go.tls_config.to_tls_config(self.__ja3_config)
        self.tls_config.ja3 = requests_go.tls_config.JA3Random(self.tls_config.ja3)
        self.session = requests_go.async_session()
        self.user_agent = self.__ja3_config.get("user_agent")
        self.anti = None
        if proxy:
            self.proxies = get_proxy()
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
        logger.info(proxy)

    def up_server_time(self, server_time=None):
        self.anti.up_server_time(server_time)

    def update_cookie(self, cookie):
        if not cookie:
            return
        if isinstance(cookie, dict):
            self.session.cookies.update(cookie)
            return
        elif isinstance(cookie, str):
            cookie_dict = {}
            for c in cookie.split("; "):
                k, v = c.split("=")[0], "".join(c.split("=")[1:])
                cookie_dict[k] = v
            self.session.cookies.update(cookie_dict)

    @stamina.retry(on=retry_on, attempts=3, timeout=30)
    async def get(self, *args,**kwargs):
        if self.if_ja3:
            kwargs["tls_config"] = self.tls_config
        url = kwargs.get("url") or args[0]
        logger.info(f"get: {url}")
        if self.proxies:
            kwargs["proxies"] = self.proxies
        anti = kwargs.pop("anti", {})
        if anti:
            if anti is True:
                anti = {}
            headers = kwargs.get("headers", {})
            anti_content = await self.anti.get_anti(**anti)
            headers["anti-content"] = anti_content
            kwargs["headers"] = headers
        verify = kwargs.pop("verify", None)
        retry_count = 1
        while retry_count < 5:
            try:
                resp = await self.session.get(verify=False,timeout=self.timeout, *args,**kwargs)
                break
            except Exception as e:
                logger.error(f"get error: {e}")
                self.proxies = get_proxy()
                kwargs["proxies"] = self.proxies
                retry_count += 1
        else:
            raise Exception(f"get failed: {url} proxy{self.proxies}")

        if verify:
            verify_res = await verify(resp)
            if isinstance(verify_res, requests_go.Response):
                return verify_res
            elif verify_res is True:
                if anti:
                    kwargs["anti"] = anti
                resp = await self.post(*args, **kwargs)
            else:
                raise Exception(f"verify failed:")
        return resp

    @stamina.retry(on=retry_on, attempts=3, timeout=30)
    async def post(self, *args, **kwargs):
        if self.if_ja3:
            kwargs["tls_config"] = self.tls_config
        url = kwargs.get("url") or args[0]
        logger.info(f"post: {url}")
        if self.proxies:
            kwargs["proxies"] = self.proxies
        anti = kwargs.pop("anti", {})
        if anti:
            if anti is True:
                anti = {}
            headers = kwargs.get("headers", {})
            anti_content = await self.anti.get_anti(**anti)
            headers["anti-content"] = anti_content
            kwargs["headers"] = headers

        verify = kwargs.pop("verify", None)
        retry_count = 1
        while retry_count < 5:
            try:
                resp = await self.session.post(verify=False,timeout=self.timeout, *args,**kwargs)
                break
            except Exception as e:
                self.proxies = get_proxy()
                kwargs["proxies"] = self.proxies
                retry_count += 1
        else:
            raise Exception(f"post failed: {url}")

        if verify:
            verify_res = await verify(resp)
            if isinstance(verify_res, requests_go.Response):
                return verify_res
            elif verify_res is True:
                if anti:
                    kwargs["anti"] = anti
                resp = await self.post(*args, **kwargs)
                return resp
            else:
                raise Exception(f"verify failed:")

        return resp

    def get_cookie(self, name=None, default=""):
        if name:
            return self.session.cookies.get(name, default)
        return self.session.cookies.get_dict()

    def get_ua(self):
        return self.user_agent

    def get_headers(self):
        headers = self.session.headers.copy()
        headers["Cookie"] = "; ".join([f"{k}={v}" for k,v in self.get_cookie().items()])
        return headers

    def update_headers(self, headers):
        if isinstance(headers, dict):
            self.session.headers.update(headers)
            if self.anti:
                self.anti.headers.update(headers)


class Request(object):
    def __init__(self, proxy=None, headers=None, if_ja3=True):
        self.__ja3_config = random.choice(ja3_configs)
        self.if_ja3 = if_ja3
        self.tls_config = requests_go.tls_config.to_tls_config(self.__ja3_config)
        self.tls_config.ja3 = requests_go.tls_config.JA3Random(self.tls_config.ja3)
        self.user_agent = self.__ja3_config.get("user_agent")
        self.session = requests_go.Session()
        self.anti = None
        self.cookies = {}
        if proxy:
            self.proxies = {"http": proxy, "https": proxy}
        else:
            self.proxies = None
        if headers:
            self.user_agent = headers.get("User-Agent") or headers.get("user-agent")
            if not self.user_agent:
                self.user_agent = self.__ja3_config["user_agent"]
                headers["User-Agent"] = self.user_agent
            cookies = headers.pop("Cookie", '') or headers.pop("cookie", '')
            self.update_cookie(cookies)
        else:
            self.user_agent = self.__ja3_config["user_agent"]

    def update_cookie(self, cookies):
        self.cookies.update(cookies)




if __name__ == '__main__':
    pass
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
        }
    r = AsyncRequest(headers=headers,)
    async def main():
        # res = await r.get("https://tls.peet.ws/api/all",headers={"anti":"123"})
        print(r.get_ua())
    asyncio.run(main())
