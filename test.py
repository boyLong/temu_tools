from common.request import AsyncRequest


import asyncio

from common.request import AsyncRequest
from common.encrypt_tools import AsyncAnti

async def test():

    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    'cookie': 'region=211; language=en; currency=USD; api_uid=Cm14m2YqNi1Z9gBpvyhlAg==; timezone=Asia%2FShanghai; webp=1; _nano_fp=Xpman09YX5TxX5TYno_O2_xYvdJAvh7~r36utb24; _bee=V3hBJmUlTKjtMaNK6uC6RrhaJAPp3apc; njrpl=V3hBJmUlTKjtMaNK6uC6RrhaJAPp3apc; dilx=kCp0W0_O~VvWF2dztTwF_; hfsc=L3yLfIk06zr60JbEfg==; _ttc=3.YwMAJ2zJVHMN.1745578437; verifyAuthToken=h-KaDxVoSFZOAZDeecWPSQe911551c6cec1f45d; goods=goods_hfgsj9; __cf_bm=h0lWwSqIIl_mbjIO4CPHaPGNrQVj1rWDsAkqAE26V6U-1714043504-1.0.1.1-G6lk8egj9.ZubWCVPTjuhwnU.cjb.lmEqoGhAMZmAgY5F88vuyO3ckJ8TgYatti14TY3tlp2HjmGTSobmAf77Q',
    'origin': 'https://www.temu.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.temu.com/jiameng-pets-m-222447459331.html?goods_id=601099516773562&_x_sessn_id=ks912b07b1&refer_page_name=goods&refer_page_id=10032_1714042728373_x9goa985b4&refer_page_sn=10032&filter_items=1%3A1',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'verifyauthtoken': 'h-KaDxVoSFZOAZDeecWPSQe911551c6cec1f45d',
}

    headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, zstd', 'accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive', 'accept-language': 'zh-CN,zh;q=0.9', 'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        'referer': 'https://www.temu.com/jiameng-pets-m-222447459331.html?_x_sessn_id=1131ghfar4&refer_page_name=home&refer_page_sn=10005',
        'pragma': 'no-cache', 'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin',
        'verifyauthtoken': '_xj765jhYzGek-KFSzF7yQ3b3e74cad82758b01',
        'Cookie': 'timezone=Asia%2FShanghai; currency=USD; language=en; region=211; webp=1; _nano_fp=Xpman09Yn0gqlpXonT_G2V8RTDSA7_ZxwVWa5DtA; verifyAuthToken=_xj765jhYzGek-KFSzF7yQ3b3e74cad82758b01; api_uid=CmyaqmYqPOohQwBnwUu4Ag==; __cf_bm=GTl1tAR5ZI26G2gap6jI7hWvYv97l0hNaxmD3VkGZDQ-1714044138-1.0.1.1-AwREXQ94SaKQwjJf9BBW8COA1R3beZSL2gIqxVFbVi5v0udNv7hwJcCXAI8VFLvFWjRffiS_gKlfIAcFF5eUjQ; _bee=JxvccLV0gWb1At5qcat2g7Nt4mm8vapk; njrpl=JxvccLV0gWb1At5qcat2g7Nt4mm8vapk; dilx=RTdtJeEWHI2RYbjG7WDC_; hfsc=L3yLfIk07T/90pbEeA==; _ttc=3.C7rMR3LZr0RT.1745580159'}
    headers =  {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, zstd",
        "accept": "application/json, text/plain, */*",
        "Connection": "keep-alive",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "content-type": "application/json;charset=UTF-8",
        "referer": "https://www.temu.com/jiameng-pets-m-222447459331.html?_x_sessn_id=lziax6paba&refer_page_name=home&refer_page_sn=10005",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "verifyauthtoken": "WbxruoQtIC1v3NI2pJmZ7Qa84bfc761eb1909eb",
        "cookie": "timezone=Asia/Shanghai; currency=USD; language=en; region=211; webp=1; _nano_fp=Xpman09yXqPjnqdxXC_2rIgikmTUMTlwAmEJoOCw; verifyAuthToken=WbxruoQtIC1v3NI2pJmZ7Qa84bfc761eb1909eb; api_uid=CmyaqmYqYJE0VABvx94XAg==; __cf_bm=zVgAc9wbIdZ326Tsqg2sjwA3FBOrZvTSek2QDzOV3Is-1714053265-1.0.1.1-Ofci.E2rP.jldFdFhnY6d6mL3iZHrNiCJeMYI9hby603Y7wRDVVA1MZvBVDHYBNiOuyZVLGjXP1OMtAFfVCSkQ; _bee=TfLCZdeOhx7vyd1GuoMLnITroidbOapi; njrpl=TfLCZdeOhx7vyd1GuoMLnITroidbOapi; dilx=hCp9ygAuIvzQ7Hvn8b9zE; hfsc=L3yLfIk16jz+2pDNeQ==; _ttc=3.ueX45yx6fLPk.1745589276"
    }
    ar = AsyncRequest(headers=headers,proxy=None)
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
    data = {"mall_id": 222447459331, "main_goods_ids": ["601099516773562"], "filter_items": "3:1", "page_number": 1,
     "page_size": 60, "list_id": "g5n9ida1n2b5evpm583h4", "scene_code": "mall_rule", "page_sn": 10040,
     "page_el_sn": 201265, "source": 10018, "fill_to_tab_id": -1,
     "anti_content":a }


    response = await ar.post('https://www.temu.com/api/bg/circle/c/mall/newGoodsList',
                       anti={
                         "event":True
                       },
                        json=data)
    response = await ar.get('https://www.temu.com/1pc-sofa-slipcover-pet-dog-friendly-sofa-cover-fuzzy-non-slip-sofa-slipcover-breathable-sofa-slipcover-for-bedroom-office-living-room-decor-home-decor-g-601099522176120.html?_x_sessn_id=lziax6paba&refer_page_name=home&refer_page_sn=10005',
              )
    print(response.text)

if __name__ == '__main__':

    asyncio.run(test())




