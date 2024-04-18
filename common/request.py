import asyncio
import random
from retrying import retry
import requests_go
import aiohttp
from common.config import ja3_configs
from common.logger import logger

class Request:

    def __init__(self, proxy=None, headers=None):
        self.__ja3_config = random.choice(ja3_configs)
        self.tls_config = requests_go.tls_config.to_tls_config(self.__ja3_config)
        self.tls_config.ja3 = requests_go.tls_config.JA3Random(self.tls_config.ja3)
        self.session = requests_go.session()
        self.session.verify = False
        self.headers = headers
        self.anti = None
        if proxy is not None:
            self.session.proxies = {"http":proxy, "https": proxy}

    def headers(self, headers=None):
        if headers is not None:
            headers = {
                "user-agent": self.__ja3_config.get("user_agent"),
            }
        return headers
    @retry(stop_max_attempt_number=1)
    def get(self, *args,**kwargs):
        kwargs["tls_config"]=self.tls_config
        return self.session.get(verify=False,*args,**kwargs)

    def get_cookie(self):
        return self.session.cookies.get_dict()

    def get_ua(self):
        return self.__ja3_config.get("user_agent")

    @retry(stop_max_attempt_number=1)
    def post(self, *args, **kwargs):
        kwargs["tls_config"] = self.tls_config
        return self.session.post(*args, **kwargs)


class AsyncRequest:
    def __init__(self, proxy=None, headers=None):
        self.__ja3_config = random.choice(ja3_configs)
        self.tls_config = requests_go.tls_config.to_tls_config(self.__ja3_config)
        self.tls_config.ja3 = requests_go.tls_config.JA3Random(self.tls_config.ja3)
        self.session = requests_go.async_session()
        self.user_agent = self.__ja3_config.get("user_agent")
        self.anti = None
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
            self.session.headers.update(headers)
        else:
            self.user_agent = self.__ja3_config["user_agent"]

    def up_server_time(self, server_time=None):
        self.anti.up_server_time(server_time)
    def update_cookie(self, cookie):
        if isinstance(cookie, dict):
            self.session.cookies.update(cookie)
            return
        elif isinstance(cookie, str):
            cookie_dict = {}
            for c in cookie.split("; "):
                k, v = c.split("=")[0], "".join(c.split("=")[1:])
                cookie_dict[k] = v
            self.session.cookies.update(cookie_dict)

    @retry(stop_max_attempt_number=2)
    async def get(self, *args,**kwargs):
        url = kwargs.get("url")
        if url:
            logger.info(f"get: {url}")
        else:
            logger.info(f"get: {args[0]}")
        # kwargs["tls_config"] = self.tls_config
        if self.proxies:
            kwargs["proxies"] = self.proxies
        return await self.session.get(verify=False, *args,**kwargs)

    @retry(stop_max_attempt_number=5)
    async def post(self, *args, **kwargs):
        # kwargs["tls_config"] = self.tls_config

        url = kwargs.get("url")
        if url:
            logger.info(f"post: {url}")
        else:
            logger.info(f"post: {args[0]}")
        if self.proxies:
            kwargs["proxies"] = self.proxies
        anti = kwargs.pop("anti", {})
        if anti:
            headers = kwargs.get("headers", {})
            anti_content = await self.anti.get_anti(**anti)
            headers["anti-content"] = anti_content
            kwargs["headers"] = headers

        verify = kwargs.pop("verify", None)
        resp = await self.session.post(verify=False, *args,**kwargs)
        if verify:
            verify_res = await verify(resp)
            if verify_res:
                if anti:
                    kwargs["anti"] = anti
                resp = await self.post(*args, **kwargs)

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


class AsyncRequestTest:
    def __init__(self, proxy=None, headers=None):
        self.__ja3_config = random.choice(ja3_configs)

        self.session = aiohttp.ClientSession()
        self.user_agent = self.__ja3_config.get("user_agent")
        self.anti = None
        self.proxy = proxy
        if headers:
            self.user_agent = headers.get("User-Agent") or headers.get("user-agent")
            if not self.user_agent:
                self.user_agent = self.__ja3_config["user_agent"]
                headers["User-Agent"] = self.user_agent
            cookies = headers.get("Cookie") or headers.get("cookie")
            self.update_cookie(cookies)
            self.session.headers.update(headers)
        else:
            self.user_agent = self.__ja3_config["user_agent"]

    def up_server_time(self, server_time=None):
        self.anti.up_server_time(server_time)
    def update_cookie(self, cookie):
        if isinstance(cookie, dict):
            self.session.cookie_jar.update_cookies(cookie)
            return
        elif isinstance(cookie, str):
            cookie_dict = {}
            for c in cookie.split("; "):
                k, v = c.split("=")[0], "".join(c.split("=")[1:])
                cookie_dict[k] = v
            self.session.cookie_jar.update_cookies(cookie_dict)

    @retry(stop_max_attempt_number=2)
    async def get(self, *args,**kwargs):
        return await self.session.get(verify=False,proxy=self.proxy, *args,**kwargs)

    @retry(stop_max_attempt_number=2)
    async def post(self, *args, **kwargs):
        anti = kwargs.pop("anti", {})
        if anti:
            headers = kwargs.get("headers", {})
            anti_content = await self.anti.get_anti(**anti)
            headers["anti-content"] = anti_content
            kwargs["headers"] = headers

        verify = kwargs.pop("verify", None)
        resp = await self.session.post(verify=False, *args,**kwargs)
        if verify:
            verify_res = await verify(resp)
            if verify_res:
                if anti:
                    kwargs["anti"] = anti
                resp = await self.post(*args, **kwargs)

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
