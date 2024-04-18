# import re
#
# from common.encrypt_tools import  AsyncAnti
# from common.request import AsyncRequest
#
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'accept': 'application/json, text/plain, */*', 'Connection': 'keep-alive', 'accept-language': 'zh-CN,zh;q=0.9', 'cache-control': 'no-cache', 'content-type': 'application/json;charset=UTF-8', 'referer': 'https://www.temu.com/?refer_page_name=login&refer_page_id=10005_1713362060163_6y64realhr&refer_page_sn=10013&_x_sessn_id=s3tx814o6r', 'pragma': 'no-cache', 'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'verifyauthtoken': 'SLAvEmhhHgx36PUfZezmXg28a19710456315c2f', 'Cookie': '_nano_fp=XpmaXqXjX59jXqXbno_GfT4YlqRQ7u7JA7xwAbLm; currency=USD; language=en; region=211; timezone=Asia%2FShanghai; webp=1; __cf_bm=7.qJQgv5GCTOmpvFiGv5VgJt2kzl7r5eNws24.GZqZI-1713362138-1.0.1.1-XOyT_dk9hwHJ5JACeNq_7_I0EaUsUstnxpZzKm9gOVHejxfFU5mM8_y.eQn9cIv3QTK4HYdYnEIyU0SZ8Duf0Q; _bee=wo1eecebbit2S1s3b3Jmy3YANOMqPap8; api_uid=Cm0wDGYf1I2deAB6KgJWAg==; dilx=teU_KfSQCGvBp6CKlhhFT; hfsc=L3yLe4o26z7/15DMeQ==; njrpl=wo1eecebbit2S1s3b3Jmy3YANOMqPap8; AccessToken=2ORDXNN6LSVVWG4TONUUPE7YO5SZ4UR2KSJVMXKMJFB3UD75T43Q0110d3847c26; _device_tag=CgI2WRIIWG9MU3RkbnkaMKLiTPwhnvkkAi0kMT6/TO06YHAqNfHEwpgXfg3TiN+xk64ZYogVSw6JgFF0lRzKnjAC; isLogin=1713362095166; user_uin=BBCD4MH4U4AQAWOQVQMCWZGJQX5NSVZAQ3VVCMVC; _ttc=3.9zJ7HQrpqzsE.1744898082'}
#
#
#
# async def shop_test():
#     sesssion = AsyncRequest(proxy="http://127.0.0.1:8888", headers=None)
#     sesssion.anti = AsyncAnti(headers)
#     data = {
#         "mall_id": 634418213464489,
#         "filter_items": "2:0",
#         "page_number": 1,
#         "page_size": 60,
#         "list_id": "fpmttvnls6mppoj7uan9g",
#         "scene_code": "mall_rule",
#         "page_sn": 10040,
#         "page_el_sn": 201265,
#         "source": 10018,
#         "fill_to_tab_id": -1,
#         "anti_content": ""
#     }
#     referer = headers.get("referer")
#     x = re.findall("_x_sessn_id=(.*?)($|&)", referer)[0][0]
#     refer_page_id = re.findall("refer_page_id=(.*?)($|&)",referer)[0][0]
#     print(x,refer_page_id)
#     referer = ("https://www.temu.com/to-be-like-m-634418213464489.html?refer_page_el_sn=201825&refer_page_name="
#                f"home&refer_page_id={refer_page_id}&refer_page_sn=10005&_x_sessn_id={x}&filter_items=2%3A0")
#     sesssion.update_headers({
#         "referer": referer
#     })
#     resp = await sesssion.post("https://www.temu.com/api/bg/circle/c/mall/newGoodsList",
#                                anti={
#                                  "event":True
#                                },
#                                json=data,)
#     print(resp.text)
# import asyncio
# asyncio.run(shop_test())
#


import requests
headers =  {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'anti-content': '0aqAfqnUDjhyy9Ex-XLXGgYvDmdKwt8rJxJa14t_l11pWl2k0gyYwP3N_zR8luYMdcmXt4XpPZvIvHvH_XzaCm-aCEUsMEzyC1fVTBirapSAWpNiGbrz1zZW7W7z1xdQMOZ--veBS1fcpB_oVxlHHB4s7YXwL6ZX5nZfutMI8LvvzlcbU9-GtcuihORHqvk4ykGqJwoQZzMfRpXNjq6lZ3VDHTH0YQqksxPdDhI8mlnQAObcJaDt5AWnLIRNmBhRNjup9UZ0ZEzwn_2M1y528B41dmxHmMYuDJJExnR4suNvzVbtDhqndapytTB2ndGMUzqMPsM9d0TC9uCti5U94xOHCNkAeLq4YeHm8v_r25E2Ov8XRV86SldfoqmHsgZibgWDy-eZ_xHonH2GNfxzQ9aU7zjFbcouxvmeDUaruBSFTk0iVHeZuCiEKjw8vbXUKmpKYiRRialiavaJMRA-QXHbVMpeqPHF23hH7_V83CT3sIPPKEn67pJFAc6WMEgWAOqbM7ViQ0HmnCNrqoDUjKOmRRpicrMF8RYI37WHS8ZBsT1rtSa',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    'cookie': 'region=210; language=en; currency=GBP; api_uid=CnD0C2Yg9M0jBQBbHRLxAg==; timezone=Asia%2FShanghai; _nano_fp=XpmaXqTqnpCjX5dJlT_K~odmh8DeLcwKv_kUg7Zf; _bee=DmahSfCRsFGVFK3DD1ohgxnRFi5QJaoR; njrpl=DmahSfCRsFGVFK3DD1ohgxnRFi5QJaoR; dilx=I5iZ2GMpxNvMrPLPIYedF; hfsc=L3yLe40z7Db+0ZXOeg==; verifyAuthToken=IZZCHJmJve5rYl_Rj4IG4Q99875784e8de293e4',
    'origin': 'https://www.temu.com',
    'pragma': 'no-cache',
    'referer': 'https://www.temu.com/bgn_verification.html?VerifyAuthToken=IZZCHJmJve5rYl_Rj4IG4Q99875784e8de293e4&from=https%3A%2F%2Fwww.temu.com%2Fuk%2Fundine-smart-home-m-634418212426071.html%3Frefer_page_el_sn%3D201825%26refer_page_name%3Dhome%26refer_page_id%3D10005_1713435875332_jqtdssrrfg%26refer_page_sn%3D10005&_x_sessn_id=blcb4dl28o&refer_page_name=mall&refer_page_id=10040_1713435950578_2la17zr4t8&refer_page_sn=10040',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'verifyauthtoken': 'IZZCHJmJve5rYl_Rj4IG4Q99875784e8de293e4',
}
# res = requests.post("http://127.0.0.1:20001/captcha",
#               json={"headers": headers})

res = requests.post("http://172.24.16.124:20001/captcha",
              json={"headers": headers})
print(res.text)