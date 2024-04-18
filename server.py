from common.verify_captcha import VerifyCaptcha
from common.encrypt_tools import get_random
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class HeaderItem(BaseModel):
    headers: dict

@app.post("/captcha")
async def identity(item: HeaderItem):
    try:
        headers = item.headers
        user = f"user-databurning-sessid-{get_random(8)}-sesstime-20-keep-true"
        proxy = f'http://{user}:databurning@43.128.74.58:30111'
        verification = VerifyCaptcha(headers=headers,proxy=proxy)
        res = await verification.start()
        return {"code": 200, "data": res}
    except Exception as e:
        return {"code": 500, "data": str(e)}