from common.request import AsyncRequest


import asyncio

from common.request import AsyncRequest
from common.encrypt_tools import AsyncAnti,get_random

async def test():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-type': 'application/json;charset=UTF-8',
        'cookie': 'region=211; language=en; currency=USD; api_uid=CmwYcmYwxamDvQBShgnSAg==; timezone=Asia%2FShanghai; webp=1; _nano_fp=Xpman0T8X5Xjn0donT_0BafzuX2X6kWgRfNEqsrY; _bee=urvJrxI5fTSPK26T8twp3EVtoGrfuapE; njrpl=urvJrxI5fTSPK26T8twp3EVtoGrfuapE; dilx=QjgpTdXHtIrmmyk5Ov5TO; hfsc=L3yLfI036z3+1ZfNcA==; _ttc=3.cGaMdTOUPjRO.1746008380; verifyAuthToken=bftMS-bt78TOJD8edznB8g888ac69818fec1b1f',
        'origin': 'https://www.temu.com',
        'priority': 'u=1, i',
        'referer': 'https://www.temu.com/practical-backpack-m-6198684838469.html?refer_page_el_sn=201825&refer_page_name=bgn_verification&refer_page_id=10017_1714472382187_pq0i9udb5z&refer_page_sn=10017&_x_sessn_id=hg06oee7z7&filter_items=1%3A1',
        'sec-ch-ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
        'verifyauthtoken': 'bftMS-bt78TOJD8edznB8g888ac69818fec1b1f',
    }
    headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, zstd', 'accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive', 'accept-language': 'zh-CN,zh;q=0.9', 'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8', 'pragma': 'no-cache',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"', 'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'referer': 'https://www.temu.com/practical-backpack-m-6198684838469.html?_x_sessn_id=e341kt0ojj&refer_page_name=bgn_verification&refer_page_id=10005_1714479987636_cbuhviiazo&refer_page_sn=10005',
        'verifyauthtoken': 'Gc5lvuUYLsLhSk_YOu9NtQ39dbefbb74d2040d3',
        'Cookie': 'timezone=Asia%2FShanghai; currency=USD; language=en; region=211; webp=1; _nano_fp=Xpman0T8lpUJlpTaXC_pJ58sfbCPK3VOJgahEOvV; verifyAuthToken=Gc5lvuUYLsLhSk_YOu9NtQ39dbefbb74d2040d3; api_uid=CmxwDmYw43RINgBUUiu2Ag==; _bee=ZNKQfyIyDsafjCEeyy88NPx5ZO2v4apf; njrpl=ZNKQfyIyDsafjCEeyy88NPx5ZO2v4apf; dilx=ZppSVbHFaV8XidkPKJkiV; hfsc=L3yLfI034Dfw2pLPew==; _ttc=3.vcOjI5ELdFM2.1746015993'}

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, zstd', 'accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive', 'accept-language': 'zh-CN,zh;q=0.9', 'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8', 'pragma': 'no-cache',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"', 'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'referer': 'https://www.temu.com/practical-backpack-m-6198684838469.html?_x_sessn_id=c54qfncgsd&refer_page_name=bgn_verification&refer_page_id=10005_1714480064547_gr2pm03dwf&refer_page_sn=10005',
        'verifyauthtoken': 'FtumcDqnrzzkZvyxeRMCtA1980032fe0930844a',
        'Cookie': 'timezone=Asia%2FShanghai; currency=USD; language=en; region=211; webp=1; _nano_fp=Xpman0TJX09jnpdylT_W~h9S1pdr7Ccr~kmwvCO8; verifyAuthToken=FtumcDqnrzzkZvyxeRMCtA1980032fe0930844a; api_uid=Cm1olmYw48A8MgBwVZ2eAg==; _bee=qrA64G1hOosFE5zFeJ5gIoUvMTZdlapY; njrpl=qrA64G1hOosFE5zFeJ5gIoUvMTZdlapY; dilx=ZvFS187noycKcDKgHFB14; hfsc=L3yLfI046T7+1ZTJeg==; _ttc=3.MdyOeuzjzq66.1746016071'}

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, zstd', 'accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive', 'accept-language': 'zh-CN,zh;q=0.9', 'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        'referer': 'https://www.temu.com/practical-backpack-m-6198684838469.html?refer_page_name=login&refer_page_id=10013_1714480337850_1i9vvdp2co&refer_page_sn=10013&_x_sessn_id=fv9y1xm01z',
        'pragma': 'no-cache', 'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin',
        'verifyauthtoken': 'RZO0I-FA2VDFnHW1WcgCDwd9ecf822025cbee1b',
        'Cookie': 'timezone=Asia%2FShanghai; region=211; language=en; currency=USD; webp=1; _nano_fp=Xpman0TJX0XYXpEYnC_~zkLmRzhcXCvLnqbDd3qY; verifyAuthToken=RZO0I-FA2VDFnHW1WcgCDwd9ecf822025cbee1b; api_uid=Cm14m2Yw5NNFEQBbUZ14Ag==; __cf_bm=pVSWec1yeYrgXIptgo.ZYkr4aLbMrKTpiIXS6Ab.pEk-1714480374-1.0.1.1-DAw9Zt7MBuXLi.lYR9yb6c4R7iIxELyE.cchd5lq8UogU5U4jqEISZ0K0eSSk6IxPupAnMekDyQQQpJ0tmEwAA; _bee=dFcYKuNF8eRaiDunp23JwCFs0fjOoapY; njrpl=dFcYKuNF8eRaiDunp23JwCFs0fjOoapY; dilx=k4UtSzZkTpE474FBZ0iXG; hfsc=L3yLfI046T380ZHNfQ==; _ttc=3.UlS2SOLHoYTe.1746016376; _device_tag=CgI2WRIIWG9MU3RkbnkaMMuuwGQuxV+a9+VsqCbFqQTxSRi+e181WIa7H6p6d6/6k64ZYogVSw6JgFF0lRzKnjAC; AccessToken=ZBRBFY2MJYFQFGBL3QFMAKU7IFXCDO7TNJLHOP64XIS7TLTQDMCA0110d3c6a53d; user_uin=BDMLBWAZV52N7A36DAVOLL7TIC42RRHTDJYTXOH4; isLogin=1714480401634'}



    ar = AsyncRequest(headers=headers, proxy=False)
    ar.anti = AsyncAnti(headers=ar.get_headers(),
                                      lt_c=[230, 9, 217, 13],
                                      gt_c=[167, 184, 169, 116],
                                      _=[
                                            "T",
                                            "*",
                                            "ì",
                                            "ª"
                                        ])
    a = await ar.anti.get_anti(event=True)
    data = {"mall_id":6198684838469,"filter_items":"1:1","page_number":1,"page_size":60,"list_id":get_random(21),

            "scene_code":"mall_rule","page_sn":10040,"page_el_sn":201265,"source":10018,"fill_to_tab_id":-1,"anti_content":a}





    response = await ar.post('https://www.temu.com/api/bg/circle/c/mall/newGoodsList',
                       anti={
                         "event":True
                       },
                        json=data)

    print(response.text)

if __name__ == '__main__':

    asyncio.run(test())
