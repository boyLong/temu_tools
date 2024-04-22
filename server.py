from common.verify_captcha import VerifyCaptcha
from common.encrypt_tools import get_random
from fastapi.concurrency import run_in_threadpool

from fastapi import FastAPI
from pydantic import BaseModel
from TemuLogin import TemuLogin
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

@app.get("/login_ck")
async def login():
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
                "cookie": "timezone=Asia%2FShanghai; currency=USD; language=en; region=211; webp=1"
            }
            user = f"user-databurning-sessid-{get_random(8)}-sesstime-20-keep-true"
            proxy = f'http://{user}:databurning@43.128.74.58:30111'
            tl = TemuLogin(headers=headers,proxy=proxy)
            res = await tl.start()
            if res:
                return {"code": 200, "data": res}
            else:
                return {"code": 500, "data": ""}
        res = await get_cookie()
        return "ok"
    except Exception as e:
        return {"code": 500, "data": str(e)}