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
        'Cookie': 'timezone=Asia%2FShanghai currency=USD; language=en; region=211; webp=1; _nano_fp=Xpman09Yn0gqlpXonT_G2V8RTDSA7_ZxwVWa5DtA; verifyAuthToken=_xj765jhYzGek-KFSzF7yQ3b3e74cad82758b01; api_uid=CmyaqmYqPOohQwBnwUu4Ag==; __cf_bm=GTl1tAR5ZI26G2gap6jI7hWvYv97l0hNaxmD3VkGZDQ-1714044138-1.0.1.1-AwREXQ94SaKQwjJf9BBW8COA1R3beZSL2gIqxVFbVi5v0udNv7hwJcCXAI8VFLvFWjRffiS_gKlfIAcFF5eUjQ; _bee=JxvccLV0gWb1At5qcat2g7Nt4mm8vapk; njrpl=JxvccLV0gWb1At5qcat2g7Nt4mm8vapk; dilx=RTdtJeEWHI2RYbjG7WDC_; hfsc=L3yLfIk07T/90pbEeA==; _ttc=3.C7rMR3LZr0RT.1745580159'}
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

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Accept-Encoding": "gzip, deflate", "accept": "application/json, text/plain, */*", "Connection": "keep-alive",
        "accept-language": "zh-CN,zh;q=0.9", "cache-control": "no-cache",
        "content-type": "application/json;charset=UTF-8",
        "referer": "https://www.temu.com/jiameng-pets-m-222447459331.html?_x_sessn_id=dv0ig9wcau&refer_page_name=bgn_verification&refer_page_id=10005_1714272491046_ur4fxu87mg&refer_page_sn=10005",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\"", "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin",
        "verifyauthtoken": "4TSxHKN5HliYH7WgAlqHnQ197d687051b20b5df",
        "Cookie": "timezone=Asia/Shanghai; region=211; language=en; currency=USD; webp=1; _nano_fp=Xpman0P8X5Tbn0TbXT_RdxDbSnR8rZaIBUIiweg2; verifyAuthToken=4TSxHKN5HliYH7WgAlqHnQ197d687051b20b5df; api_uid=Cm1olmYtuOspkQBpEVQzAg==; __cf_bm=EcUyIqVFh1kfZfV3_Yx6zNV_EMCEL.7kTCiY87mkctU-1714272492-1.0.1.1-Ff_HEeSDHAfBBSKV1zl4K6aBbA1.Ggoz3Wr.ID9hgQgOapwvfnKJUSZIS2Ny_FhNBgVxbaL2plNlzrXUHndUGQ; _bee=G0bPuo7KbYjaFu2J3ZLvEffyrNPwiapz; njrpl=G0bPuo7KbYjaFu2J3ZLvEffyrNPwiapz; dilx=V8tLhqpbSEJtEhoQvyjBu; hfsc=L3yLfIs36zrx2pLOcQ==; _ttc=3.wkEv5ggPtTMU.1745808507"}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, zstd", "accept": "application/json, text/plain, */*",
        "Connection": "keep-alive", "accept-language": "zh-CN,zh;q=0.9", "cache-control": "no-cache",
        "content-type": "application/json;charset=UTF-8",
        "referer": "https://www.temu.com/jiameng-pets-m-222447459331.html?_x_sessn_id=r49k6drbnx&refer_page_name=bgn_verification&refer_page_id=10005_1714293278332_tx6m6sgzzn&refer_page_sn=10005",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\"", "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin",
        "verifyauthtoken": "SY3kUX2Z-lg-gsWHmw7-lweb2d7a751e12dde9d",
        "Cookie": "timezone=Asia%2FShanghai; region=211; language=en; currency=USD; webp=1; _nano_fp=Xpman0PbXqPJXqPjnC_A_I5QJ1XCsT7ol6u32_o7; verifyAuthToken=SY3kUX2Z-lg-gsWHmw7-lweb2d7a751e12dde9d; api_uid=Cm0wb2YuCiAAzQBgFhPhAg==; __cf_bm=cn88zPxJuaLMqm_hd6CS96C2pEBBS7TkUqOKZ_m19kE-1714293280-1.0.1.1-_Mya0FIJ6JgD5GORc3YNr79dAjU27rddGVH5og_fMbkmkrDotmH6w_Rzpvfg3wzWwT6P9G52aQnxjOtA8q0low; _bee=TslkS4CQUfqPis1UlpYbmqgtKzhACapG; njrpl=TslkS4CQUfqPis1UlpYbmqgtKzhACapG; dilx=WzuiW5Wg7eAqJZwfQaHOB; hfsc=L3yLfIs56jzw25HIeQ==; _ttc=3.d5D8wBVdJ6yK.1745829298"

    }

    headers =  {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, zstd", "accept": "application/json, text/plain, */*",
        "Connection": "keep-alive", "accept-language": "zh-CN,zh;q=0.9", "cache-control": "no-cache",
        "content-type": "application/json;charset=UTF-8",
        "referer": "https://www.temu.com/fashion-product-trends-m-5857109250737.html?refer_page_el_sn=201825&refer_page_name=bgn_verification&refer_page_id=10017_1714319644294_pruhvd5qt9&refer_page_sn=10017&_x_sessn_id=n6qscypoyg&filter_items=1%3A1",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\"", "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin",
        "verifyauthtoken": "46GaDjhHEs-MSiAc7BJzYwc97323f7a40cd2c88",
        "Cookie": "region=211; language=en; currency=USD; api_uid=CmyobGYucQh4ywBjVdGwAg==; timezone=Asia%2FShanghai; webp=1; _nano_fp=Xpman0XalpEqn0dxXo_yMdLWCu9yVzx09oy0rrPA; _bee=cfEwa17k1rIxWEjCIdxyfT5nHHFCHapg; njrpl=cfEwa17k1rIxWEjCIdxyfT5nHHFCHapg; dilx=0vbTfWgAFPIAxnBTvdOBi; hfsc=L3yLfIox4Dj70JDFfA==; _ttc=3.l0NyzN8AQPRL.1745855639; verifyAuthToken=46GaDjhHEs-MSiAc7BJzYwc97323f7a40cd2c88"}


    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, zstd", "accept": "application/json, text/plain, */*",
        "Connection": "keep-alive", "accept-language": "zh-CN,zh;q=0.9", "cache-control": "no-cache",
        "content-type": "application/json;charset=UTF-8",
        "referer": "https://www.temu.com/fashion-product-trends-m-5857109250737.html?_x_sessn_id=6tx4km80pd&refer_page_name=bgn_verification&refer_page_id=10005_1714319810684_4soxayewf6&refer_page_sn=10005",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\"", "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin",
        "verifyauthtoken": "J6eal2xgzgo7NeHW_E7f-g4a143c97e742dd8cc",
        "Cookie": "timezone=Asia%2FShanghai; region=211; language=en; currency=USD; webp=1; _nano_fp=Xpman0XalpCan5TyXC_PULOgj6pdPwnOR7Yjr7g1; verifyAuthToken=J6eal2xgzgo7NeHW_E7f-g4a143c97e742dd8cc; api_uid=CmxSomYuccOMjQBfIJRnAg==; __cf_bm=w_2H698F.uW30XRNwiGAaQCQRqg4I_1AegoIwu.1TN4-1714319811-1.0.1.1-Y_O6CIj3rh4hgVwXJzZY8ee7zpDyj4Z7oWyZtZ3nmMalLZpm5WvxRdm5Wt6w0SIFoGbsqjno428RREzjKYND4Q; _bee=xhxsM8gXEl4Xxd2T1hdypb1YzllATaps; njrpl=xhxsM8gXEl4Xxd2T1hdypb1YzllATaps; dilx=AKG2t8xWQz9MFHMn4sTZr; hfsc=L3yLfIox4Db605PNcQ==; _ttc=3.yMAS1dEMwqz5.1745855832"}

    # headers ={
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    #     "Accept-Encoding": "gzip, deflate", "accept": "application/json, text/plain, */*", "Connection": "keep-alive",
    #     "accept-language": "zh-CN,zh;q=0.9", "cache-control": "no-cache",
    #     "content-type": "application/json;charset=UTF-8",
    #     "referer": "https://www.temu.com/fashion-product-trends-m-5857109250737.html?_oak_mp_inf=EOCL3aum1ogBGiA4Zjk0YTNhMWVjMGQ0MTA1YjA5NWQxMDQyNDM1ZDdjOCD%2FmcCr8jE%3D&top_gallery_url=https%3A%2F%2Fimg.kwcdn.com%2Fproduct%2Ffancy%2Ffa49f10f-a05f-4e40-8405-8f699cf101cb.jpg&spec_gallery_id=2100590095&refer_page_sn=10005&refer_source=0&freesia_scene=1&_oak_freesia_scene=1&_oak_rec_ext_1=ODM2&_oak_gallery_order=311539360%2C1596074401%2C2038030781%2C656627091%2C71949729&refer_page_el_sn=200024&refer_page_name=home&refer_page_id=10005_1714320028123_f08ny9rl8j&_x_sessn_id=ef9g20pmkx",
    #     "pragma": "no-cache",
    #     "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
    #     "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\"", "sec-fetch-dest": "empty",
    #     "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin",
    #     "verifyauthtoken": "0ODHNec8hRP0I5oESnd_3g78eb0dd7af4bd0e2e",
    #     "Cookie": "timezone=Asia%2FShanghai; region=211; language=en; currency=USD; webp=1; _nano_fp=Xpman0XxX09qX0dbXT_LgukhRcyZVVXe_lQjJ7jn; verifyAuthToken=0ODHNec8hRP0I5oESnd_3g78eb0dd7af4bd0e2e; api_uid=CmxwvmYucqMmMwBxIuGRAg==; __cf_bm=V8AdoRuDUGss5.qU9L2yVoLt6bARyne9iI7Pqo4h99g-1714320035-1.0.1.1-E0eKTkN0wjf9TON0XaYbDSMBJfm6VxbrNmHMF50qFU7_nnkArJTrr57NcXldFBR_F_qfBXBINLpteacCMUAZGA; _bee=uCqiCfT7MrlLzathIjrhiOCPtkeXNapz; njrpl=uCqiCfT7MrlLzathIjrhiOCPtkeXNapz; dilx=1dUEZs325kn2nwj6WIc7q; hfsc=L3yLfIoy6T7725DNeg==; _ttc=3.s1RpAplmyoeg.1745856048"}
    headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, zstd', 'accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive', 'accept-language': 'zh-CN,zh;q=0.9', 'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        'referer': '?_x_sessn_id=6u7q6k9nfy&refer_page_name=bgn_verification&refer_page_id=10005_1714357698210_qu4lz5mcy3&refer_page_sn=10005',
        'pragma': 'no-cache', 'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin',
        'verifyauthtoken': 'BL67cv6B4VEOTGDd9ZNLyAfa849dd16c9bcb667',
        'Cookie': 'timezone=Asia%2FShanghai; currency=GBP; language=en; region=210; webp=1; _nano_fp=Xpman0XynqmoX5XqnC_2Sr_JxJpYJRIQKp833JCu; verifyAuthToken=BL67cv6B4VEOTGDd9ZNLyAfa849dd16c9bcb667; api_uid=CnCapGYvBcEolQBVCqr+Ag==; __cf_bm=eKqqGtV8Tf3_zVbKPzLuLzX3WS275JPZQDlbweUKshU-1714357697-1.0.1.1-BMiJy5wsgWVTsP_JmVLoBY0rFRF1XtWgmL.UBwgoheGTTJFB9od0aWWZQvOnup8pwImAFFjZFEj.Rl0fxN3W3A; _bee=vHZmEu5tz7kZBw4BEbHSF4eYN00eSaop; njrpl=vHZmEu5tz7kZBw4BEbHSF4eYN00eSaop; dilx=JrlSWm0WZbkwRDuaDakoP; hfsc=L3yLfIo17jn41p7MeA=='}
    headers =  {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, zstd', 'accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive', 'accept-language': 'zh-CN,zh;q=0.9', 'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        'referer': '?_x_sessn_id=4zij0a63tp&refer_page_name=bgn_verification&refer_page_id=10005_1714358452188_g5qtp4sbwb&refer_page_sn=10005',
        'pragma': 'no-cache', 'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin',
        'verifyauthtoken': '85rcjTwhgvUXgG875fRJOwe802f0df57591858a',
        'Cookie': 'timezone=Asia%2FShanghai; currency=USD; language=en; region=211; webp=1; _nano_fp=Xpman0Xyl0Tyn5EYX9_xlTXlkIB5vNUyfmNda~xP; verifyAuthToken=85rcjTwhgvUXgG875fRJOwe802f0df57591858a; api_uid=Cm14m2YvCLOFCQB4LJnWAg==; __cf_bm=Ld5OprYXfmetkqNpm3by5QGYONS4XABangEPLhISYXE-1714358451-1.0.1.1-fm9HLTAvqGSnDDoCB371BLXsQxEanAHfHT9TCuTZnQUThl9ruBDV3JZMSp27mGT1uYqhwDLehOm5DxGWJ7u_KQ; _bee=Q2ul0axS16iZdJTLiHHMGIfpNUgT8apC; njrpl=Q2ul0axS16iZdJTLiHHMGIfpNUgT8apC; dilx=arMly5oYSk3TpRqQTd9gq; hfsc=L3yLfIo14Tr925/Mew==; _ttc=3.UoLDnDaT6Dj0.1745894469'}
    headers =  {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
        'Accept-Encoding': 'gzip, deflate, zstd', 'accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive', 'accept-language': 'zh-CN,zh;q=0.9', 'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        'referer': 'https://www.temu.com/fashion-product-trends-m-5857109250737.html?_x_sessn_id=bhuln0jl6b&refer_page_name=bgn_verification&refer_page_id=10005_1714370100417_nsenmirwq3&refer_page_sn=10005',
        'pragma': 'no-cache', 'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin',
        'verifyauthtoken': '1hQqQCKSz-ho8dtDUiJfew58c61414598168bda',
        'Cookie': 'timezone=Asia%2FShanghai; currency=USD; language=en; region=211; webp=1; _nano_fp=Xpman0X8X0goX5T8no_fQjSitfIJARopafLQOY8T; verifyAuthToken=1hQqQCKSz-ho8dtDUiJfew58c61414598168bda; api_uid=Cm1olmYvNjVYLwB5NXIkAg==; _bee=KzrgZcVDTxn21WJGXILeMfhjl4238app; njrpl=KzrgZcVDTxn21WJGXILeMfhjl4238app; dilx=TdQfeKQy5c7wk5WyE0wnl; hfsc=L3yLfIo36T/415bJfQ==; _ttc=3.e0ERCBAmCG94.1745906110'}

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
    data = {"mall_id": 5857109250737, "main_goods_ids": ["601099516773562"], "filter_items": "3:1", "page_number": 1,
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
