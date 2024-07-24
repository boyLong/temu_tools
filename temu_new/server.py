import json
from common.encrypt_tools import get_random
from common.device_generation import DeviceGeneration
from fastapi import FastAPI
from pydantic import BaseModel
from temu_login import LoginSpider
from temu_shop import ShopSpider
from verify.verify import VerifyCaptcha
from temu_login_shop import ShopLoginSpider


app = FastAPI()


class loginItem(BaseModel):
    headers: dict
    username: str
    password: str
    shop_url: str =' '


class shopItem(BaseModel):
    headers: dict
    shop_url: str

class headersItem(BaseModel):
    headers: dict


@app.post("/login", summary="传入初始化cookie, 登录或者注册")
async def ck(login: loginItem):
    try:
        async def get_cookie():
            login_spider = LoginSpider(
                headers=login.headers,
                username=login.username,
                password=login.password,
                proxy=True
            )
            res = await login_spider.start()
            if res:
                return {"code": 200, "data": res}
            else:
                return {"code": 500, "data": "登录失败"}
        res = await get_cookie()
        return res
    except Exception as e:
        return {"code": 500, "data": str(e)}


@app.post("/shop", summary="传入初始化cookie, 登录或者注册")
async def ck(shop: shopItem):
    try:
        async def get_cookie():
            shop_spider = ShopSpider(
                headers=shop.headers,
                shop_url=shop.shop_url,
                proxy=True
            )
            res = await shop_spider.start()
            if res:
                return {"code": 200, "data": res}
            else:
                return {"code": 500, "data": "设备激活失败"}
        res = await get_cookie()
        return res
    except Exception as e:
        return {"code": 500, "data": str(e)}


@app.post("/verify", summary="传入headers, 过验证码")
async def vf(item: headersItem):
    try:
        vc = VerifyCaptcha(
            headers=item.headers,
            proxy=True
        )
        res = await vc.start()
        return {"code": 200, "data": res}
    except Exception as e:
        return {"code": 500, "data": str(e)}


@app.post("/login_shop", summary="传入headers, 过验证码")
async def vf(item: loginItem):
    try:

        vc = ShopLoginSpider(
            headers=item.headers,
            proxy=True,
            username=item.username,
            password=item.password,
            shop_url=item.shop_url or "https://www.temu.com/-tech-m-634418211480526.html",
        )
        res = await vc.start()
        return {"code": 200, "data": res}
    except Exception as e:
        return {"code": 500, "data": str(e)}



if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=30200)

