from verify.verify import VerifyCaptcha

vc = VerifyCaptcha(

        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'zh-CN,zh;q=0.9',
            'anti-content': '0aqWfqlv0jTaF992_8uJfJysVaM8-3rj3kI5GG4iwT5_izIeOV22Y83i-KK-HHPLQZTu69ZrVLQX5kQtZkEstgUuEgaryyorR7ioTsyG1zRYVJpmZwsJvzkUhle5IUEFRH4F8OcoJ12QLYfL5_5a1CuqQTX_3iGvhZsH5JDjntmcAvFb9BLnnlw64HzbHrm4tuKVzZdgszlZQogvnJkkFAbRDRW041FjlGPo881xqcXEHMCCfRa1Z6g4GcenLB7ayeQX55BII4uHZoe_lHhenv3BrLsfBsfk8qqXNH5FSsQkg84P6ontPDPhL259azGu9Mn22yoVmLQ3y9Z40Vi1HzcsOFDn5pFVRq8kkAJ3VsSmwK8DXyc3O4DQj1GkvEzfCVfug4D1nlRPKQOgJZifJ48CGjbrVWlgiRhN5y6fxzIlChE1YDhxpsEphrjo3yJnJtRYy7XCkiRQrEMaDGUgHPCmV1JmJESJsISZzeRTxxrplRNJQBSjiw6ZtDe4Pp1-5Pt',
            'cache-control': 'no-cache',
            'content-type': 'application/json;charset=UTF-8',
            'cookie': 'region=211; language=en; currency=USD; api_uid=Cm0EX2aaUUQqPABWklNYAg==; timezone=Asia%2FShanghai; webp=1; _nano_fp=XpmxXpXJlpTon5TjXT_W6_Y2hlAhX1ZWvwkrPBfE; verifyAuthToken=Bu8B3uL0pd9nFo9D21D2SA4b0859970a6c84e7a; _bee=NRQwXSXMHiPoKEYhToh0ZHh0ZLYl6apf; njrpl=NRQwXSXMHiPoKEYhToh0ZHh0ZLYl6apf; dilx=~W72okKKqE_uNFUBOyEtX; hfsc=L3yIeYo44Dr415LJfQ==; _ttc=3.RXc9qPul89Lf.1752925405',
            'origin': 'https://www.temu.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.temu.com/bgn_verification.html?VerifyAuthToken=TbByplp3v9qqoU1_ERhuqQea04513e2934ca729&from=https%3A%2F%2Fwww.temu.com%2Flogin.html%3Flogin_scene%3D8%26from%3Dhttps%3A%2F%2Fwww.temu.com%2Fbest-of-asia-by--m-634418213975418.html&type=iframe&iframeMsgId=6pfpuuqp4q9g703c5mcxo',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'verifyauthtoken': 'Bu8B3uL0pd9nFo9D21D2SA4b0859970a6c84e7a',
        },
        proxy=False
)

import asyncio

print(asyncio.run(vc.start()))
