import json

from common.verify_captcha import VerifyCaptcha
from common.encrypt_tools import get_random
from fastapi import FastAPI
from pydantic import BaseModel
from TemuLogin import TemuLogin
from TemuList import TemuList
from common.proxy import get_proxy
app = FastAPI()


class HeaderItem(BaseModel):
    headers: dict


@app.post("/captcha")
async def identity(item: HeaderItem):
    try:
        headers = item.headers
        user = f"user-databurning-sessid-{get_random(8)}-sesstime-20-keep-true"
        proxy = f'http://{user}:databurning@43.128.74.58:30111'
        proxy = 'http://look1234-zone-custom-region-hk:look1234@47.236.40.83:8088'
        verification = VerifyCaptcha(headers=headers,proxy=proxy)
        res = await verification.start()
        return {"code": 200, "data": res}
    except Exception as e:
        return {"code": 500, "data": str(e)}


@app.get("/ck")
async def ck(cookie_str: str ="timezone=Asia%2FShanghai; region=210; language=en; currency=GBP; webp=1"):
    try:
        async def get_cookie():
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
                "cookie": cookie_str
            }
            tl = TemuList(headers=headers,proxy=get_proxy())
            res = await tl.start()
            if res:
                return {"code": 200, "data": res}
            else:
                return {"code": 500, "data": "设备激活失败"}
        res = await get_cookie()
        return res
    except Exception as e:
        return {"code": 500, "data": str(e)}


@app.get("/login_ck")
async def login(cookie_str: str  = "timezone=Asia%2FShanghai; region=211; language=en; currency=USD; webp=1"):
    try:
        async def get_cookie():
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
                "cookie": cookie_str
            }


            tl = TemuLogin(headers=headers,proxy=get_proxy())
            res = await tl.start()
            if res:
                return {"code": 200, "data": res}
            else:
                return {"code": 500, "data": ""}
        res = await get_cookie()
        return res
    except Exception as e:
        return {"code": 500, "data": str(e)}

