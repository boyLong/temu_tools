from common.request import AsyncRequest


import asyncio

from common.request import AsyncRequest
from common.encrypt_tools import AsyncAnti,get_random

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

    headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, zstd', 'accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive', 'accept-language': 'zh-CN,zh;q=0.9', 'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        'referer': 'https://www.temu.com/costwayshop-m-634418213768139.html?refer_page_name=home&refer_page_id=10013_1714399580461_hri62jrapy&refer_page_sn=10013&_x_sessn_id=9bgfc1ko4l',
        'pragma': 'no-cache', 'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin',
        'verifyauthtoken': 'BnF9PVE4LvqZbM-PJcPkTAe8d91ace3cd9dfa06',
        'Cookie': 'timezone=Asia%2FShanghai; currency=USD; language=en; region=211; webp=1; _nano_fp=Xpman0XblpExnpdbnT_mftmgyOYk6DoIR5nlxu6X; verifyAuthToken=BnF9PVE4LvqZbM-PJcPkTAe8d91ace3cd9dfa06; api_uid=CmwYcmYvqYiMiABpbxKxAg==; __cf_bm=2i3Bm7UQVIaLcX1WEumsywFnAbUsqceJD7gRINIu0qU-1714399624-1.0.1.1-L.535Y_4Ib6LhbvbzCL6wJe1o6kle97B56j4Qw405Xd43f2GlLshaj4TO6iwr5n3tp.Z3xry3xx7b_ydr69Sjg; _bee=xNiuWR8GSDcgleQXTsVBg7hFSJZW2apr; njrpl=xNiuWR8GSDcgleQXTsVBg7hFSJZW2apr; dilx=mj6JbMpOFbosnY5VjYLFE; hfsc=L3yLfIo54Dj625DKfg==; _ttc=3.gffoM8dcS997.1745935632'
    }
    headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, zstd', 'accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive', 'accept-language': 'zh-CN,zh;q=0.9', 'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        'referer': 'https://www.temu.com/costwayshop-m-634418213768139.html?refer_page_el_sn=201825&refer_page_name=bgn_verification&refer_page_id=10017_1714400029023_14ruwjq9d8&refer_page_sn=10017&_x_sessn_id=4bsbs8q06d&filter_items=1%3A1',
        'pragma': 'no-cache', 'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin',
        'verifyauthtoken': 'BnF9PVE4LvqZbM-PJcPkTAe8d91ace3cd9dfa06',
        'Cookie': 'timezone=Asia%2FShanghai; currency=USD; language=en; region=211; webp=1; _nano_fp=Xpman0XblpExnpdbnT_mftmgyOYk6DoIR5nlxu6X; verifyAuthToken=BnF9PVE4LvqZbM-PJcPkTAe8d91ace3cd9dfa06; api_uid=CmwYcmYvqYiMiABpbxKxAg==; __cf_bm=2i3Bm7UQVIaLcX1WEumsywFnAbUsqceJD7gRINIu0qU-1714399624-1.0.1.1-L.535Y_4Ib6LhbvbzCL6wJe1o6kle97B56j4Qw405Xd43f2GlLshaj4TO6iwr5n3tp.Z3xry3xx7b_ydr69Sjg; _bee=xNiuWR8GSDcgleQXTsVBg7hFSJZW2apr; njrpl=xNiuWR8GSDcgleQXTsVBg7hFSJZW2apr; dilx=mj6JbMpOFbosnY5VjYLFE; hfsc=L3yLfIo54Dj625DKfg==; _ttc=3.gffoM8dcS997.1745935632'}
    headers =  {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, zstd', 'accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive', 'accept-language': 'zh-CN,zh;q=0.9', 'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        'referer': 'https://www.temu.com/costwayshop-m-634418213768139.html?refer_page_name=home&refer_page_id=10013_1714400282430_g7qlq5gq2i&refer_page_sn=10013&_x_sessn_id=x4mmkav2nz',
        'pragma': 'no-cache', 'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin',
        'verifyauthtoken': 'XJy7z9gKwI_5Vik3KvwgkA2a5d158b1cd9680ca',
        'Cookie': 'timezone=Asia%2FShanghai; currency=USD; language=en; region=211; webp=1; _nano_fp=Xpman0ToX0PJnpTYX9_47QyMt62bsowu45_ZPSnh; verifyAuthToken=XJy7z9gKwI_5Vik3KvwgkA2a5d158b1cd9680ca; api_uid=CmyaqmYvrBsMbgBUOQZWAg==; __cf_bm=5Gguvhd0V1Wh91o8Rkh5r9YJPGK4QzsgM6X9RbhGBdM-1714400283-1.0.1.1-m0gL9.wwTSLsBiN6krMOf5gB11oLBU2pJG9rqrlWPRBJlekNE1lAbZOChCnAd2FOuYIXe8nr.0gqE01NJJFeXw; _bee=xwLAscNNT7slgyHEA5lMI2Mz8cXdpapi; njrpl=xwLAscNNT7slgyHEA5lMI2Mz8cXdpapi; dilx=3rl4pAPec~pGceiAlWhQH; hfsc=L3yLfI0w6Tzw1JTNcA==; _ttc=3.3un09pjIFk4f.1745936290'}

    headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, zstd', 'accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive', 'accept-language': 'zh-CN,zh;q=0.9', 'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        'referer': 'https://www.temu.com/cost2aysho1p-m-634418213768139.html?_x_sessn_id=iiq007qrv0&refer_page_name=bgn_verification&refer_page_id=10005_1714400684112_octbf70vrn&refer_page_sn=10005',
        'pragma': 'no-cache', 'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin',
        'verifyauthtoken': 'OkL7QwrvIyyeV5EKEgYXDQ29f709bdce870a222',
        'Cookie': 'timezone=Asia%2FShanghai; currency=USD; language=en; region=211; webp=1; _nano_fp=Xpman0ToX0EJl0XanT_65OOMGhzho0aU0Y1DXXqJ; verifyAuthToken=OkL7QwrvIyyeV5EKEgYXDQ29f709bdce870a222; api_uid=Cm1olmYvra4SmwBaN4doAg==; _bee=sKf2XeJ0np7rslwU6QOEwM6yplXobapK; njrpl=sKf2XeJ0np7rslwU6QOEwM6yplXobapK; dilx=DJoGT6d3UlXfEFDmn_OZr; hfsc=L3yLfI0w6Tjx0pbIeQ==; _ttc=3.kdvvGQgLMXIm.1745936702'}


    '''
    https://www.temu.com/costwayshop-m-634418213768139.html?top_goods=601099570461044&refer_page_el_sn=201825&refer_page_name=home&refer_page_id=10005_1714399898059_x807ox6khp&refer_page_sn=10005&_x_sessn_id=4bsbs8q06d
    
    '''
    headers ={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Accept-Encoding": "gzip, deflate", "accept": "application/json, text/plain, */*", "Connection": "keep-alive",
        "accept-language": "zh-CN,zh;q=0.9", "cache-control": "no-cache",
        "content-type": "application/json;charset=UTF-8", "referer": "?login_scene=8",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\"", "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin",
        "verifyauthtoken": "I-f5l-kOUMvlBa0gQtPa2A88f068b0212dbc884",
        "Cookie": "timezone=Asia%2FShanghai; region=211; language=en; currency=USD; webp=1; _nano_fp=Xpman0TYXqdaXpTYlT_DZ3B6_UrZhtai_MNkLahJ; verifyAuthToken=I-f5l-kOUMvlBa0gQtPa2A88f068b0212dbc884; api_uid=Cm14m2YwVPZHWwBeSFHYAg==; __cf_bm=9OyJ70A6z59RZfAv_alISwShBKVL7pua9hHhw6LeZIA-1714443510-1.0.1.1-MLd_cYgkOQQGsJkmBbBeAY6zKPR2pzLiKXbknMltLJMwLmwOjMOH30l5LhjEOf7bAj.hqP5q5CLrdCn4j9ftCg; _bee=0loYmDUzI2lwVDQKOul2Z8efmrcgyapk; njrpl=0loYmDUzI2lwVDQKOul2Z8efmrcgyapk; dilx=RV9s4UZBgtikTj44tcSHE; hfsc=L3yLfI006jv50JDEfg==; _ttc=3.tsIDuEuAzm0Z.1745979517; _device_tag=CgI2WRIIWG9MU3RkbnkaMMHaLW+xIp8Jwj/ph4kNtZakoyom06wXnIGBgJpEBgNAk64ZYogVSw6JgFF0lRzKnjAC; AccessToken=4MZLP2FQ6O6PDHQG2AYG3J7QJUOM2WD3WQPNHUHQO2HISHXDUXGA0110d333b019; user_uin=BAMBG45KSNC5MDVAA6XLTUW2DZFZIXPZZ3G7NPFJ; isLogin=1714443556229"}

    headers ={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
        "Accept-Encoding": "gzip, deflate", "accept": "application/json, text/plain, */*", "Connection": "keep-alive",
        "accept-language": "zh-CN,zh;q=0.9", "cache-control": "no-cache",
        "content-type": "application/json;charset=UTF-8", "referer": "https://www.temu.com/costwayshop-m-634418213768139.html?login.html?login_scene=8",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\"", "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin",
        "verifyauthtoken": "pV_8YlvPSBw9c_1Pl0mhIQ2b612da39d7d19a47",
        "Cookie": "timezone=Asia%2FShanghai; region=211; language=en; currency=USD; webp=1; _nano_fp=Xpman0TYnpUqn0dxX9_EKAnKHr_Np0_LjioZvIqg; verifyAuthToken=pV_8YlvPSBw9c_1Pl0mhIQ2b612da39d7d19a47; api_uid=Cm1olmYwXm0SmwBaRs00Ag==; __cf_bm=DrZ1O9XrTkpM7uHY35ira_FfA2ZFVPo2DztQC6QJvgU-1714445934-1.0.1.1-ydh.SkRE3yNRzux9cxeR4t4ewlZahfa14S_E0BCqMtF2QN.JX.U3xUVYC8OLw17f6e8LPFCgz.KiG5FyrFd4cA; _bee=iiTtRKyyXjERjZmsfEa5tOIXd7oLoapW; njrpl=iiTtRKyyXjERjZmsfEa5tOIXd7oLoapW; dilx=urL7lJctdQCvaKw5EZbg3; hfsc=L3yLfI007Df715LLeg==; _ttc=3.XEw5PknbtLAL.1745981937; _device_tag=CgI2WRIIWG9MU3RkbnkaMDgJIopVNcp6F0a1sBhO/IFLt5MVGcEar/YTlVbnR72ck64ZYogVSw6JgFF0lRzKnjAC; AccessToken=DZBZXMHB4RF222TC6CP436EXX27SITJRUCSPXS4QRO7RLWGBG3NQ0110d3f3b544; user_uin=BDVWTNU3FSPDQHTLEX4PDYSHPIHTKEAIE3KO2CCW; isLogin=1714445946563"}




    ''

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

    data =  {"mall_id": 634418213768139, "filter_items": "1:1", "page_number": 1, "page_size": 60,
     "list_id": get_random(21), "scene_code": "mall_rule", "page_sn": 10040, "page_el_sn": 201265,
     "source": 10018, "fill_to_tab_id": -1,
     "anti_content": a}


    response = await ar.post('https://www.temu.com/api/bg/circle/c/mall/newGoodsList',
                       anti={
                         "event":True
                       },
                        json=data)

    print(response.text)

if __name__ == '__main__':

    asyncio.run(test())
