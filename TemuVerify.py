from common.verify_captcha import VerifyCaptcha
import asyncio
# from fastapi import FastAPI
#
# from pydantic import BaseModel
# app = FastAPI()
#
#
# class HeaderItem(BaseModel):
#     headers: dict
#
# @app.post("/identity")
# async def identity(item: HeaderItem):
#     # try:
#     headers = item.headers
#
#
#
#     verification = VerifyCaptcha(headers=headers)
#     res =verification.start()
#     return {"code": 200, "data": res}
#
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36', 'Accept-Encoding': 'gzip, deflate, zstd', 'accept': 'application/json, text/plain, */*', 'Connection': 'keep-alive', 'accept-language': 'zh-CN,zh;q=0.9', 'cache-control': 'no-cache', 'content-type': 'application/json;charset=UTF-8', 'referer': 'https://www.temu.com/?refer_page_name=home&refer_page_id=10013_1714400282430_g7qlq5gq2i&refer_page_sn=10013&_x_sessn_id=x4mmkav2nz', 'pragma': 'no-cache', 'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'verifyauthtoken': 'XJy7z9gKwI_5Vik3KvwgkA2a5d158b1cd9680ca', 'Cookie': 'timezone=Asia%2FShanghai; currency=USD; language=en; region=211; webp=1; _nano_fp=Xpman0ToX0PJnpTYX9_47QyMt62bsowu45_ZPSnh; verifyAuthToken=XJy7z9gKwI_5Vik3KvwgkA2a5d158b1cd9680ca; api_uid=CmyaqmYvrBsMbgBUOQZWAg==; __cf_bm=5Gguvhd0V1Wh91o8Rkh5r9YJPGK4QzsgM6X9RbhGBdM-1714400283-1.0.1.1-m0gL9.wwTSLsBiN6krMOf5gB11oLBU2pJG9rqrlWPRBJlekNE1lAbZOChCnAd2FOuYIXe8nr.0gqE01NJJFeXw; _bee=xwLAscNNT7slgyHEA5lMI2Mz8cXdpapi; njrpl=xwLAscNNT7slgyHEA5lMI2Mz8cXdpapi; dilx=3rl4pAPec~pGceiAlWhQH; hfsc=L3yLfI0w6Tzw1JTNcA==; _ttc=3.3un09pjIFk4f.1745936290'}


verification = VerifyCaptcha(headers=headers )

#
# '''
#
# [{"uaid":"BBFRZRNHTXDZ4XBQGE3GFJYXT3B3BQX552KOKSIJ6MIZI","email_id":"1027227397511888568323851","email_des":"asd***xzc@gmail.com","login_type":"MAIL","avatar":"https://avatar-us.kwcdn.com/avatar/avatar/default/7d96f863-b4c1-43d6-8f03-ebd1c4e23e25.png","nick_name":"as***zc","dr":"us","_x_verify_type":2,"remember":false}]
#
# '''
asyncio.run(verification.start())
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
