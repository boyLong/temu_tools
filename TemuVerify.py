from common.verify_captcha import VerifyCaptcha
import asyncio
from fastapi import FastAPI

from pydantic import BaseModel
app = FastAPI()


class HeaderItem(BaseModel):
    headers: dict

@app.post("/identity")
async def identity(item: HeaderItem):
    # try:
    headers = item.headers



    verification = VerifyCaptcha(headers=headers)
    res =verification.start()
    return {"code": 200, "data": res}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
#            'Accept-Encoding': 'gzip, deflate, br, zstd',
#            'accept': 'application/json, text/plain, */*', 'Connection': 'keep-alive', 'accept-language': 'zh-CN,zh;q=0.9', 'cache-control': 'no-cache', 'content-type': 'application/json;charset=UTF-8', 'referer': 'https://www.temu.com/?refer_page_name=login&refer_page_id=10005_1713365052382_nyv38i6kl5&refer_page_sn=10013&_x_sessn_id=ftbgfhqcuq', 'pragma': 'no-cache', 'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'verifyauthtoken': 'DJ8s2AgpHZibh-tlOggmUQ5b5399e88c88ede23', 'Cookie': '_nano_fp=XpmaXqXjnp9ynpTxXT_HMmeaobXxHUMgFMFr46VM; currency=USD; language=en; region=211; timezone=Asia%2FShanghai; verifyAuthToken=DJ8s2AgpHZibh-tlOggmUQ5b5399e88c88ede23; webp=1; __cf_bm=CIYJeUfYS6gda1FW5jT9.l1l2nvL0LF5n0.7j78OXDs-1713365109-1.0.1.1-hAd0V5K5N3zsX6Sk7WOUzN7kxTJEYZ86.j6k4XCgGUJ2pJN9saOSaUKRr2OFW3DuItQ3bfwW4nOraxIaUJLIGA; _bee=Eosk1Pzp4ovUaL2jcBp2lZtzwvfYlapo; api_uid=CmyaqmYf4Dy+TwDkLH3LAg==; dilx=SieB4kR0SchwAX69WHKH7; hfsc=L3yLe4o27D7925fMeg==; njrpl=Eosk1Pzp4ovUaL2jcBp2lZtzwvfYlapo; AccessToken=EE6T2HI7OPCMZIZGTBVNRNXKKSDVVXHOG4OYHUGYEZGL3GERPK4Q0110d3cf6a29; _device_tag=CgI2WRIIWG9MU3RkbnkaMDh0Sb7sWUROc6upJFxRHVp6xTQq0DNjHVPjBqkQ5FGXk64ZYogVSw6JgFF0lRzKnjAC; isLogin=1713365076721; user_uin=BBLC2NWV3IQDFHGYAPCW4E4GIT4UBGMS4OHRNYFA; _ttc=3.vIyavpAgRfbO.1744901065'}
#
# verification = VerifyCaptcha(headers=headers)
#
# '''
#
# [{"uaid":"BBFRZRNHTXDZ4XBQGE3GFJYXT3B3BQX552KOKSIJ6MIZI","email_id":"1027227397511888568323851","email_des":"asd***xzc@gmail.com","login_type":"MAIL","avatar":"https://avatar-us.kwcdn.com/avatar/avatar/default/7d96f863-b4c1-43d6-8f03-ebd1c4e23e25.png","nick_name":"as***zc","dr":"us","_x_verify_type":2,"remember":false}]
#
# '''
# asyncio.run(verification.start())
#
# '''
#
#
# headers = {
#     'accept': 'application/json, text/plain, */*',
#     'accept-language': 'zh-CN,zh;q=0.9',
#     'cache-control': 'no-cache',
#     'content-type': 'application/json;charset=UTF-8',
#     'cookie': 'region=211; language=en; currency=USD; api_uid=Cm0wDGYf4+ke/AEdLGzIAg==; __cf_bm=n5PXBDVF7ZAucv7zVm7SE8NaQ.JyIs2htRdtZ_evURs-1713365993-1.0.1.1-mec4e2niwNllri85DPMvRKqjQk6ygLNSSS_fKGg7jMsXXYcIvkPkkj8IgEASKcOrwsvtNQwCNveeqhFZFvZprw; timezone=Asia%2FShanghai; webp=1; _nano_fp=XpmaXqXjnpUbnqPbnC_oVLM57ObC2o6nE6T7tkm1; _bee=tP52RJckb14vJ5fUBRQJLtl8yXvQKapd; njrpl=tP52RJckb14vJ5fUBRQJLtl8yXvQKapd; dilx=ZC_JK5x_mOJNINIjIp3oz; hfsc=L3yLe4o27Dfx25/KcA==; _device_tag=CgI2WRIIWG9MU3RkbnkaMNKyUdmZNc4OeUweqEqNu6PZWZkXFvIYlpPoR9r4Yovmk64ZYogVSw6JgFF0lRzKnjAC; AccessToken=BFO5HRAARTJWZ2CCICJTT7KVZJ7ZFHJJHRJFPVK62FHD3JAXYRVQ0110d36989c1; user_uin=BAGZX77XLUDDNP4BENYOUVHAT6JLOC3SLRU2HZSK; isLogin=1713366012332; _ttc=3.NPIUGxpH97Si.1744902013; _u_pa=%7B%22nrpt_211%22%3A0%7D',
#     'origin': 'https://www.temu.com',
#     'pragma': 'no-cache',
#     'referer': 'https://www.temu.com/?refer_page_name=home&refer_page_id=10005_1713365997626_kxnkgjmb1n&refer_page_sn=10005&_x_sessn_id=52wfko3kxa',
#     'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
#     'verifyauthtoken': '8vspCpkK5xkscnyxmhrOeg4a5dd49d0ce679bfe',
# }
#
# '''