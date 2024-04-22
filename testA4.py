# # # # # import re
# # # # #
# # # # # from common.encrypt_tools import  AsyncAnti
# # # # # from common.request import AsyncRequest
# # # # #
# # # # # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'accept': 'application/json, text/plain, */*', 'Connection': 'keep-alive', 'accept-language': 'zh-CN,zh;q=0.9', 'cache-control': 'no-cache', 'content-type': 'application/json;charset=UTF-8', 'referer': 'https://www.temu.com/?refer_page_name=login&refer_page_id=10005_1713362060163_6y64realhr&refer_page_sn=10013&_x_sessn_id=s3tx814o6r', 'pragma': 'no-cache', 'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'verifyauthtoken': 'SLAvEmhhHgx36PUfZezmXg28a19710456315c2f', 'Cookie': '_nano_fp=XpmaXqXjX59jXqXbno_GfT4YlqRQ7u7JA7xwAbLm; currency=USD; language=en; region=211; timezone=Asia%2FShanghai; webp=1; __cf_bm=7.qJQgv5GCTOmpvFiGv5VgJt2kzl7r5eNws24.GZqZI-1713362138-1.0.1.1-XOyT_dk9hwHJ5JACeNq_7_I0EaUsUstnxpZzKm9gOVHejxfFU5mM8_y.eQn9cIv3QTK4HYdYnEIyU0SZ8Duf0Q; _bee=wo1eecebbit2S1s3b3Jmy3YANOMqPap8; api_uid=Cm0wDGYf1I2deAB6KgJWAg==; dilx=teU_KfSQCGvBp6CKlhhFT; hfsc=L3yLe4o26z7/15DMeQ==; njrpl=wo1eecebbit2S1s3b3Jmy3YANOMqPap8; AccessToken=2ORDXNN6LSVVWG4TONUUPE7YO5SZ4UR2KSJVMXKMJFB3UD75T43Q0110d3847c26; _device_tag=CgI2WRIIWG9MU3RkbnkaMKLiTPwhnvkkAi0kMT6/TO06YHAqNfHEwpgXfg3TiN+xk64ZYogVSw6JgFF0lRzKnjAC; isLogin=1713362095166; user_uin=BBCD4MH4U4AQAWOQVQMCWZGJQX5NSVZAQ3VVCMVC; _ttc=3.9zJ7HQrpqzsE.1744898082'}
# # # # #
# # # # #
# # # # #
# # # # # async def shop_test():
# # # # #     sesssion = AsyncRequest(proxy="http://127.0.0.1:8888", headers=None)
# # # # #     sesssion.anti = AsyncAnti(headers)
# # # # #     data = {
# # # # #         "mall_id": 634418213464489,
# # # # #         "filter_items": "2:0",
# # # # #         "page_number": 1,
# # # # #         "page_size": 60,
# # # # #         "list_id": "fpmttvnls6mppoj7uan9g",
# # # # #         "scene_code": "mall_rule",
# # # # #         "page_sn": 10040,
# # # # #         "page_el_sn": 201265,
# # # # #         "source": 10018,
# # # # #         "fill_to_tab_id": -1,
# # # # #         "anti_content": ""
# # # # #     }
# # # # #     referer = headers.get("referer")
# # # # #     x = re.findall("_x_sessn_id=(.*?)($|&)", referer)[0][0]
# # # # #     refer_page_id = re.findall("refer_page_id=(.*?)($|&)",referer)[0][0]
# # # # #     print(x,refer_page_id)
# # # # #     referer = ("https://www.temu.com/to-be-like-m-634418213464489.html?refer_page_el_sn=201825&refer_page_name="
# # # # #                f"home&refer_page_id={refer_page_id}&refer_page_sn=10005&_x_sessn_id={x}&filter_items=2%3A0")
# # # # #     sesssion.update_headers({
# # # # #         "referer": referer
# # # # #     })
# # # # #     resp = await sesssion.post("https://www.temu.com/api/bg/circle/c/mall/newGoodsList",
# # # # #                                anti={
# # # # #                                  "event":True
# # # # #                                },
# # # # #                                json=data,)
# # # # #     print(resp.text)
# # # # # import asyncio
# # # # # asyncio.run(shop_test())
# # # # #
# # # #
# # # #
# # # # import requests
# # # # headers =  {
# # # #     'accept': 'application/json, text/plain, */*',
# # # #     'accept-language': 'zh-CN,zh;q=0.9',
# # # #     'anti-content': '0aqAfqnUDjhyy9Ex-XLXGgYvDmdKwt8rJxJa14t_l11pWl2k0gyYwP3N_zR8luYMdcmXt4XpPZvIvHvH_XzaCm-aCEUsMEzyC1fVTBirapSAWpNiGbrz1zZW7W7z1xdQMOZ--veBS1fcpB_oVxlHHB4s7YXwL6ZX5nZfutMI8LvvzlcbU9-GtcuihORHqvk4ykGqJwoQZzMfRpXNjq6lZ3VDHTH0YQqksxPdDhI8mlnQAObcJaDt5AWnLIRNmBhRNjup9UZ0ZEzwn_2M1y528B41dmxHmMYuDJJExnR4suNvzVbtDhqndapytTB2ndGMUzqMPsM9d0TC9uCti5U94xOHCNkAeLq4YeHm8v_r25E2Ov8XRV86SldfoqmHsgZibgWDy-eZ_xHonH2GNfxzQ9aU7zjFbcouxvmeDUaruBSFTk0iVHeZuCiEKjw8vbXUKmpKYiRRialiavaJMRA-QXHbVMpeqPHF23hH7_V83CT3sIPPKEn67pJFAc6WMEgWAOqbM7ViQ0HmnCNrqoDUjKOmRRpicrMF8RYI37WHS8ZBsT1rtSa',
# # # #     'cache-control': 'no-cache',
# # # #     'content-type': 'application/json;charset=UTF-8',
# # # #     'cookie': 'region=210; language=en; currency=GBP; api_uid=CnD0C2Yg9M0jBQBbHRLxAg==; timezone=Asia%2FShanghai; _nano_fp=XpmaXqTqnpCjX5dJlT_K~odmh8DeLcwKv_kUg7Zf; _bee=DmahSfCRsFGVFK3DD1ohgxnRFi5QJaoR; njrpl=DmahSfCRsFGVFK3DD1ohgxnRFi5QJaoR; dilx=I5iZ2GMpxNvMrPLPIYedF; hfsc=L3yLe40z7Db+0ZXOeg==; verifyAuthToken=IZZCHJmJve5rYl_Rj4IG4Q99875784e8de293e4',
# # # #     'origin': 'https://www.temu.com',
# # # #     'pragma': 'no-cache',
# # # #     'referer': 'https://www.temu.com/bgn_verification.html?VerifyAuthToken=IZZCHJmJve5rYl_Rj4IG4Q99875784e8de293e4&from=https%3A%2F%2Fwww.temu.com%2Fuk%2Fundine-smart-home-m-634418212426071.html%3Frefer_page_el_sn%3D201825%26refer_page_name%3Dhome%26refer_page_id%3D10005_1713435875332_jqtdssrrfg%26refer_page_sn%3D10005&_x_sessn_id=blcb4dl28o&refer_page_name=mall&refer_page_id=10040_1713435950578_2la17zr4t8&refer_page_sn=10040',
# # # #     'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
# # # #     'sec-ch-ua-mobile': '?0',
# # # #     'sec-ch-ua-platform': '"Windows"',
# # # #     'sec-fetch-dest': 'empty',
# # # #     'sec-fetch-mode': 'cors',
# # # #     'sec-fetch-site': 'same-origin',
# # # #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
# # # #     'verifyauthtoken': 'IZZCHJmJve5rYl_Rj4IG4Q99875784e8de293e4',
# # # # }
# # # # # res = requests.post("http://127.0.0.1:20001/captcha",
# # # # #               json={"headers": headers})
# # # #
# # # # res = requests.post("http://172.24.16.124:20001/captcha",
# # # #               json={"headers": headers})
# # # # print(res.text)
# # #
# # # import httpx
# # # import stamina
# # # import asyncio
# # #
# # #
# # #
# # #
# # # @stamina.retry(on=Exception, attempts=3)
# # # async def t():
# # #     http = httpx.AsyncClient()
# # #     # await http.request('GET', 'https://httpbin.org1')
# # #     await http.get("https://httpbin.org/ip")
# # # asyncio.run(t())
# #
# # # import requests
# # #
# # # resp= requests.get("https://www.etsy.com",proxies={
# # #     "http": "http://look1234-zone-custom-region-hk:look1234@47.236.40.83:8088",
# # #     "https": "http://look1234-zone-custom-region-hk:look1234@47.236.40.83:8088"
# # # })
# # #
# # # print(resp.text)
# # import requests
# #
# # res = requests.get(url="https://www.temu.com/plus-size-feather-print-ruched-tank-top-casual-square-neck-sleeveless-top-for-summer-womens-plus-size-clothing-g-601099543413804.html?is_back=",
# #             verify=False,
# #              headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36', 'Accept-Encoding': 'gzip, deflate, zstd', 'accept': 'application/json, text/plain, */*', 'Connection': 'keep-alive', 'accept-language': 'zh-CN,zh;q=0.9', 'cache-control': 'no-cache', 'content-type': 'application/json;charset=UTF-8', 'referer': 'https://www.temu.com/?_x_sessn_id=9zatv32d3f&refer_page_name=bgn_verification&refer_page_sn=10005', 'pragma': 'no-cache', 'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'verifyauthtoken': '9tPpQAH0TvaVBjXoK56gPwf9363298bb2877d44', 'Cookie': 'region=210; language=en; currency=GBP; api_uid=CnBsdWYiTDlSpQD4Q1bxAg==; _bee=o7udr5Hm5UfCjLrLFpyMxPCpJ4oKDaoD; njrpl=o7udr5Hm5UfCjLrLFpyMxPCpJ4oKDaoD; dilx=AFz5IGYP2QAewuWhaSjaK; hfsc=L3yLe4wy6jn/1p7KeQ==; _nano_fp=XpmaXqdxXqm8n5TanT_Me555oQwkd3HUVPsw3XJz; verifyAuthToken=9tPpQAH0TvaVBjXoK56gPwf9363298bb2877d44'}
# # )
# #
# # print(res.text)
#
# import tkinter as tk
# from tkinter import ttk
# from tkinter import scrolledtext
#
# def select_path():
#     # TODO: 实现选择路径按钮的功能
#     pass
#
# def process_data():
#     # TODO: 实现确定按钮的功能
#     pass
#
# root = tk.Tk()
# root.title("界面示例")
#
# # 创建条形码输入框
# barcode_entry = ttk.Entry(root)
# barcode_entry.pack(pady=10)
#
# # 创建路径输入框和选择路径按钮的容器
# path_container = ttk.Frame(root)
# path_container.pack(pady=10)
#
# # 创建路径输入框
# path_entry = ttk.Entry(path_container)
# path_entry.grid(row=0, column=0)
#
# # 创建选择路径按钮
# select_path_button = ttk.Button(path_container, text="选择路径", command=select_path)
# select_path_button.grid(row=0, column=1, padx=10)
#
# # 创建滑动文本框
# scroll_text = scrolledtext.ScrolledText(root, width=30, height=10)
# scroll_text.pack(pady=10)
#
# # 创建确定按钮
# confirm_button = ttk.Button(root, text="确定", command=process_data)
# confirm_button.pack(pady=10)
#
# root.mainloop()
import asyncio

from common.device_generation import DeviceGeneration
from common.verify_captcha import VerifyCaptcha

hauk = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    'referer': "https://www.temu.com/uk",
    'pragma': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    "cookie": "timezone=Asia%2FShanghai; currency=GBP; language=en; region=210; webp=1"
}
uk = DeviceGeneration(hauk)

haus = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    'referer': "https://www.temu.com/uk",
    'pragma': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    "cookie": "timezone=Asia%2FShanghai; currency=USD; language=en; region=211; webp=1"
}
us = DeviceGeneration(haus)


async def get_a4_uk():
    print(1)
    r = await uk.a4()
    print(r)
    return r


async def get_a4_us():
    print(1)
    r = await us.a4()
    print(r)
    return r


async def verify(headers=None):
    if headers is None:
        headers = us
    vc = VerifyCaptcha(headers=headers)
    r = await vc.start()
    return r


async def get_verify(headers):
    r = await verify(headers)


import json
from common.encrypt_tools import AsyncAnti, get_nano, hash_o
from curl_cffi import requests


async def get_a4_uk_run(**kwargs):
    r = await get_a4_us()
    url1 = 'https://www.temu.com/api/phantom/xg/pfb/a4'
    res = requests.post(url=url1, headers=hauk, json=r, proxies=get_proxies(), impersonate="chrome110")
    api_uid = res.cookies["api_uid"]
    cookie_bee = res.json()["result"]["a"]
    cookie_dilx = res.json()["result"]["b"]
    cookie_hfsc = res.json()["result"]["g"]
    ua = haus
    ua['cookie'] = f'region=210; language=en; currency=GBP; api_uid={api_uid}; timezone=Asia%2FShanghai; webp=1; _bee={cookie_bee}; njrpl={cookie_bee}; dilx={cookie_dilx}; hfsc={cookie_hfsc}'

    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        # "anti-content":'',
        "content-type": "application/json;charset=UTF-8",
        # "Cookie":'api_uid=CnDe4WXYMgKp7ADM/aOWAg==; region=211; language=en; currency=USD; timezone=Asia%2FShanghai; shipping_city=211; webp=1; _nano_fp=Xpmol0EjnqXblpXqnC_DxxMr3NZ4UnLeJJBcP09A; _bee=DjYbhJN2TacP0uFYjjw8SHHjEG6kCapn; njrpl=DjYbhJN2TacP0uFYjjw8SHHjEG6kCapn; dilx=EIjZApG2tl2xANxd4BvVy; hfsc=L3yKcI827jr40pXOfg==; _ttc=3.00wziajxfFfB.1740203406',
        # "cookie":f'api_uid=CmyQemYgjTFQOADdQPVtAg==; timezone=Asia%2FShanghai; shipping_city=211; webp=1; region=211; language=en; currency=USD;_bee=0WQSTlNk8uOGQK4PWAQcOFI0PqKozapU; njrpl=0WQSTlNk8uOGQK4PWAQcOFI0PqKozapU; dilx=VLlZ5hYp5oAsjBvli0OqX; hfsc=L3yLe40w4D370ZPEeQ==',
        "cookie": f'region=211; language=en; currency=USD; api_uid={api_uid}; timezone=Asia%2FShanghai; webp=1; _bee={cookie_bee}; njrpl={cookie_bee}; dilx={cookie_dilx}; hfsc={cookie_hfsc}',
        "origin": "https://www.temu.com",
        "pragma": "no-cache",
        "referer": "https://www.temu.com",
        "sec-ch-ua": "\"Chromium\";v=\"123\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"123\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    }
    print(json.dumps(ua))
    Content1 = AsyncAnti(headers=headers,
                         lt_c=[230, 9, 217, 13],
                         gt_c=[167, 184, 169, 116],
                         _=[
                             "T",
                             "*",
                             "ì",
                             "ª"
                         ])

    anti = kwargs.pop("anti", {})
    ua['anti-content'] = await Content1.get_anti(**anti)
    uul = 'https://www.temu.com/api/oak/integration/sku?is_back=1'
    data = {"x_sessn_id": "ptlh2ltaln", "_x_sessn_id": "ptlh2ltaln", "page_sn": 10005, "_oak_sku_count": 1,
            "_oak_show_sale_price_suffix": 1, "_oak_show_leaf_category_low_price_tag": "1", "_oak_stage": 4,
            "single_sku_ignore_panel": 0, "goods_id": 601099527341757, "_oak_spec_ids": "", "_oak_page_source": 102,
            "request_type": 0}
    print(json.dumps(ua))
    res = requests.post(url=uul, headers=ua, json=data, proxies=get_proxies(), impersonate="chrome110")
    print(res.text)
    if 'verify_auth_token' in res.json():
        verify_auth_token = res.json()['verify_auth_token']
        headers['verifyauthtoken'] = verify_auth_token
        scv = json.dumps(headers)
        r.sadd("t_token_hea_good_us", scv)
        # r.sadd("t_token_hea_shop_us",scv)
        # r.sadd("t_token_hea_page_us",scv)
    return headers


import random


def get_proxies():
    PROXY = [
        # "http://nxqxchong-zone-custom-region-us:woaini@8.219.85.5:8999" customer-f26bfd-country-US:29a53690
        f"http://look1234-zone:look1234@47.236.40.83:8088",
        f"http://look1234-zone:look1234@47.237.23.117:8088",
        f"http://look1234-zone:look1234@47.237.29.218:8088",

        # "http://look1234-zone:look1234@47.236.40.83:8088",
        # "http://look1234-zone:look1234@47.237.23.117:8088",
        # "http://look1234-zone:look1234@47.237.29.218:8088",
        # "http://baobao123-zone:bao123456@47.236.196.224:8088",
        # "http://customer-f26bfd-country-US:29a53690@8.219.85.5:8088"

    ]
    proxyMeta = random.choice(PROXY)
    proxies_2 = {
        "http": proxyMeta,
        "https": proxyMeta
    }

    return proxies_2


async def get_a4_us_run():
    r = await get_a4_us()
    print(r)


url1 = 'https://www.temu.com/api/phantom/xg/pfb/a4'

if __name__ == '__main__':
    asyncio.run(get_a4_uk_run())
