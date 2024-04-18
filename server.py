from common.verify_captcha import VerifyCaptcha
import asyncio
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class HeaderItem(BaseModel):
    headers: dict

@app.post("/captcha")
async def identity(item: HeaderItem):
    try:
        headers = item.headers
        verification = VerifyCaptcha(headers=headers)
        res = await verification.start()
        return {"code": 200, "data": res}
    except Exception as e:
        return {"code": 500, "data": str(e)}