from common.request import AsyncRequest


import asyncio

from common.request import AsyncRequest
from common.encrypt_tools import AsyncAnti

async def test():
    headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, zstd', 'accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive', 'accept-language': 'zh-CN,zh;q=0.9', 'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        'referer': 'https://www.temu.com/uk/ka-xuan-household-products-m-634418211295175.html?refer_page_name=login&refer_page_id=10013_1714390935000_4qvxrnv8rr&refer_page_sn=10013&_x_sessn_id=6j463ebnxu',
        'pragma': 'no-cache', 'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin',
        'verifyauthtoken': 'WvDxavb3vvEfsNPpPbiwZw9a6a263697aad557e',
        'Cookie': 'timezone=Asia%2FShanghai; region=210; language=en; currency=GBP; webp=1; _nano_fp=Xpman0XbX0Uql0TbXo_z17Hnd~ZYq7dtFYevaVA2; verifyAuthToken=WvDxavb3vvEfsNPpPbiwZw9a6a263697aad557e; api_uid=CnDgj2Yvh5i7QgBnErwXAg==; __cf_bm=ePwEvLOAk9nA.JTVr9VAx5o3rly3p_TuhUVHWULHFw0-1714390936-1.0.1.1-SVhxtFUoha1TcI42GYk7TbE0aVCauXSEW5l5JLKVgczjPnixkF0Bykhq__rquoTs94BejHgUjlyzugVzq24vvA; _bee=2ejhVw1vW5uVeyQhp7kgZxSM0H3sdaoV; njrpl=2ejhVw1vW5uVeyQhp7kgZxSM0H3sdaoV; dilx=ODDjqVdpRoQy2BkAfPz16; hfsc=L3yLfIo56Tf815/MfA==; _device_tag=CgI2WRIIWG9MU3RkbnkaMLxmd0yxorZ4edGyleWSY/BN8a29dsZp8I5dhVTraNPAk64ZYogVSw6JgFF0lRzKnjAC; AccessToken=WBTGSP6I4AV2JEGABFR7XWRB3COREDVNZN7RTUS2EAOS4SZIRQYQ0110d28cd0be; user_uin=BAH7WXHGG4P5A2OLOCLP4HWSPCO73MI5KTBDXIBP; isLogin=1714390986666'}


    ar = AsyncRequest(headers=headers,proxy=False)
    ar.anti = AsyncAnti(headers=ar.get_headers(),
                                      lt_c=[71, 97, 12, 171],
                                      gt_c=[217, 54, 250, 195],
                                      _=[
                                            "ã",
                                            "#",
                                            "\u0010",
                                            "È"
                                        ])
    a = await ar.anti.get_anti(event=True)
    data = {"mall_id": 634418211295175, "main_goods_ids": ["601099516773562"], "filter_items": "3:1", "page_number": 1,
     "page_size": 60, "list_id": "g5n9ida1n2b5evpm583h4", "scene_code": "mall_rule", "page_sn": 10040,
     "page_el_sn": 201265, "source": 10018, "fill_to_tab_id": -1,
     "anti_content":a }


    response = await ar.post('https://www.temu.com/api/bg/circle/c/mall/newGoodsList',
                       anti={
                         "event":True
                       },
                        json=data)

    print(response.text)

if __name__ == '__main__':

    asyncio.run(test())
