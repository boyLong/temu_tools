import asyncio
import time
import random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
from common.logger import email_before_log, email_after_loger
from requests_go import async_session
client_tools = async_session()
import ctypes
import secrets
import http.cookies
import hashlib,hmac
from common.config import api_host
import re
from py_mini_racer import py_mini_racer
from tenacity import retry, stop_after_attempt, wait_fixed
def unsinged_right_shift(x, y):
    x,y = ctypes.c_uint32(x).value,y % 32
    return ctypes.c_uint32(x >> y).value


def get_random(e=21):
    chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    return "".join(secrets.choice(chars) for _ in range(e))

def password_encrypt(pub_info,password):
    pubkey = pub_info["pub_key"]

    l = hmac.new(
        pub_info["salt"].encode("utf-8"), password.encode("utf-8"), hashlib.sha256
    ).hexdigest()
    info = ":".join(
        [l, str(pub_info["server_time"]), pub_info["nonce"], pub_info["salt"]]
    )

    public_key = f"""-----BEGIN PUBLIC KEY-----
    {pubkey}
    -----END PUBLIC KEY-----"""
    pub_key = RSA.importKey(public_key)
    cipher = PKCS1_cipher.new(pub_key)
    rsa_text = cipher.encrypt(info.encode("utf-8)")).hex()  # 加密并转为b64编码
    return rsa_text


def cookie_to_json(cookie_str):
    cookie = http.cookies.SimpleCookie(cookie_str)
    cookie_json = {}
    for key, morsel in cookie.items():
        cookie_json[key] = morsel.value
    return cookie_json


def cookie_to_str(cookie_json):
    cookie = http.cookies.SimpleCookie()
    for key, value in cookie_json.items():
        cookie[key] = value
    return cookie.output(header='', sep=';').strip()


class AsyncAnti(object):
    def __init__(self, headers=None, cookie=None, lt_c=None,gt_c=None, _=None ):

        self.headers = {}

        self.lt_c = lt_c or [169, 166, 24, 25]
        self.gt_c = gt_c or [186, 127, 72, 47]
        self.anti_count = 1
        self._ = _ or [132, 169, 150, 34]
        self.nano = None
        self.api_uid = None
        self.location = None
        self.up_headers(headers, cookie)


    def up_headers(self, headers, cookie=None):
        for key, value in headers.items():
            self.headers[key.lower()] = value
        cookie = cookie or headers.get("cookie") or headers.get("Cookie")
        if not isinstance(cookie, dict):
            cookie = cookie_to_json(cookie)
        self.nano = cookie.get("_nano_fp")
        self.api_uid = cookie.get("api_uid")
        self.location = self.headers.get("referer", 'https://www.temu.com')
        self.up_server_time()

    def up_server_time(self, server_time=None):
        if server_time is None:
            self.ServerTime = int(time.time() * 1000 - random.randint(1000, 2000))
            self.UpdateServerTime = int(time.time() * 1000)
            self.UpdateFirstServerTime = self.UpdateServerTime - random.randint(50, 120)
        else:
            self.ServerTime = server_time.get("ServerTime")
            self.UpdateServerTime = server_time.get("UpdateServerTime")
            self.UpdateFirstServerTime = server_time.get("UpdateFirstServerTime")

    def get_track(self,  clientX, clientY, element="", track=None):

        timestamp = 220000 + random.randint(1000, 100000)
        if track:
            track = track[-30:]
            x = random.randint(700,750)
            y = random.randint(370,390)
            track_res = []
            for i in track:
                track_res.append(

                    {"elementId": element,
                     "timestamp": i[2]-self.ServerTime,
                     "clientX": int(i[0]+x),
                     "clientY": int(i[1]+y),}
                )

            return track_res
        track = [
            {
                "elementId": element,
                "timestamp": timestamp,
                "clientX": clientX,
                "clientY": clientY,
            }
        ]
        mid = random.randint(15, 24)
        for i in range(29):
            timestamp -=  random.randint(17, 30)
            clientY += random.randint(-10, 10)

            if i < mid:
                clientX += random.randint(10, 30)
                track.append(
                    {
                        "elementId": element,
                        "timestamp": timestamp,
                        "clientX": clientX,
                        "clientY": clientY,
                    }
                )
            else:
                clientX += random.randint(50, 100)

                track.append(
                    {
                        "elementId": "",
                        "timestamp": timestamp,
                        "clientX": clientX,
                        "clientY": clientY,
                    }
                )
        track.reverse()
        return track

    async def get_anti(self, event=False, clientX=None, clientY=None, track=None, element='', _nano_fp=None,
                       api_uid=None
                       ):

        location = {
            "href": self.location,
            "port": "",
        }
        screen = {"availWidth": 1980, "availHeight": 1080}
        if not clientX:
            clientX = 480 + int(random.random() * 100)
        if not clientY:
            clientY = 450 + int(random.random() * 100)

        if event:
            if track:
                track = self.get_track(clientX, clientY, element, track)
            else:
                track = self.get_track(clientX, clientY, element)

            client = {
                "elementId": "",
                "timestamp": track[-1]["timestamp"] + random.randint(10, 20),
                "clientX": track[-1]["clientX"],
                "clientY": track[-1]["clientY"],
            }

            client2 = {
                "elementId": "",
                "timestamp": track[-1]["timestamp"] + random.randint(30, 40),
                "clientX": clientX,
                "clientY": clientY,
            }

        else:
            track = []
            client = {}
            client2 = {}
        data = {
            "location": location,
            "screen": screen,
            "ServerTime": self.ServerTime,
            "UpdateServerTime": self.UpdateServerTime,
            "UpdateFirstServerTime": self.UpdateFirstServerTime,
            "UserAgent": self.headers.get("user-agent") or self.headers.get("User-Agent"),
            "nano": self.nano or _nano_fp,
            "referrer": self.location,
            "pdd_user_id": "",
            "api_uid": self.api_uid or api_uid,
            "pdd_vds": "",
            "count": self.anti_count,
            "client": client,
            "client2": client2,
            "track": track,
            "lt_c": self.lt_c,
            "gt_c": self.gt_c,
            "_": self._ ,
        }
        data = await client_tools.post("http://127.0.0.1:8980/anti", json=data)
        data = data.json()
        self.anti_count += 1
        return data["data"]


async def get_nano():
    nano = await client_tools.get("http://127.0.0.1:8980/nano")
    return nano.json()["data"]


async def get_a4(device):
    res = await client_tools.post(
        "http://127.0.0.1:8980/device", json={"device": device}
    )

    return res.json()


async def captcha_encrypt(data, init_info):
    captcha_collect = await client_tools.post(
        "http://127.0.0.1:8980/captcha_encrypt",
        json={"data": data, "init": init_info},
    )
    return captcha_collect.json()

r = [
    0,
    1996959894,
    -301047508,
    -1727442502,
    124634137,
    1886057615,
    -379345611,
    -1637575261,
    249268274,
    2044508324,
    -522852066,
    -1747789432,
    162941995,
    2125561021,
    -407360249,
    -1866523247,
    498536548,
    1789927666,
    -205950648,
    -2067906082,
    450548861,
    1843258603,
    -187386543,
    -2083289657,
    325883990,
    1684777152,
    -43845254,
    -1973040660,
    335633487,
    1661365465,
    -99664541,
    -1928851979,
    997073096,
    1281953886,
    -715111964,
    -1570279054,
    1006888145,
    1258607687,
    -770865667,
    -1526024853,
    901097722,
    1119000684,
    -608450090,
    -1396901568,
    853044451,
    1172266101,
    -589951537,
    -1412350631,
    651767980,
    1373503546,
    -925412992,
    -1076862698,
    565507253,
    1454621731,
    -809855591,
    -1195530993,
    671266974,
    1594198024,
    -972236366,
    -1324619484,
    795835527,
    1483230225,
    -1050600021,
    -1234817731,
    1994146192,
    31158534,
    -1731059524,
    -271249366,
    1907459465,
    112637215,
    -1614814043,
    -390540237,
    2013776290,
    251722036,
    -1777751922,
    -519137256,
    2137656763,
    141376813,
    -1855689577,
    -429695999,
    1802195444,
    476864866,
    -2056965928,
    -228458418,
    1812370925,
    453092731,
    -2113342271,
    -183516073,
    1706088902,
    314042704,
    -1950435094,
    -54949764,
    1658658271,
    366619977,
    -1932296973,
    -69972891,
    1303535960,
    984961486,
    -1547960204,
    -725929758,
    1256170817,
    1037604311,
    -1529756563,
    -740887301,
    1131014506,
    879679996,
    -1385723834,
    -631195440,
    1141124467,
    855842277,
    -1442165665,
    -586318647,
    1342533948,
    654459306,
    -1106571248,
    -921952122,
    1466479909,
    544179635,
    -1184443383,
    -832445281,
    1591671054,
    702138776,
    -1328506846,
    -942167884,
    1504918807,
    783551873,
    -1212326853,
    -1061524307,
    -306674912,
    -1698712650,
    62317068,
    1957810842,
    -355121351,
    -1647151185,
    81470997,
    1943803523,
    -480048366,
    -1805370492,
    225274430,
    2053790376,
    -468791541,
    -1828061283,
    167816743,
    2097651377,
    -267414716,
    -2029476910,
    503444072,
    1762050814,
    -144550051,
    -2140837941,
    426522225,
    1852507879,
    -19653770,
    -1982649376,
    282753626,
    1742555852,
    -105259153,
    -1900089351,
    397917763,
    1622183637,
    -690576408,
    -1580100738,
    953729732,
    1340076626,
    -776247311,
    -1497606297,
    1068828381,
    1219638859,
    -670225446,
    -1358292148,
    906185462,
    1090812512,
    -547295293,
    -1469587627,
    829329135,
    1181335161,
    -882789492,
    -1134132454,
    628085408,
    1382605366,
    -871598187,
    -1156888829,
    570562233,
    1426400815,
    -977650754,
    -1296233688,
    733239954,
    1555261956,
    -1026031705,
    -1244606671,
    752459403,
    1541320221,
    -1687895376,
    -328994266,
    1969922972,
    40735498,
    -1677130071,
    -351390145,
    1913087877,
    83908371,
    -1782625662,
    -491226604,
    2075208622,
    213261112,
    -1831694693,
    -438977011,
    2094854071,
    198958881,
    -2032938284,
    -237706686,
    1759359992,
    534414190,
    -2118248755,
    -155638181,
    1873836001,
    414664567,
    -2012718362,
    -15766928,
    1711684554,
    285281116,
    -1889165569,
    -127750551,
    1634467795,
    376229701,
    -1609899400,
    -686959890,
    1308918612,
    956543938,
    -1486412191,
    -799009033,
    1231636301,
    1047427035,
    -1362007478,
    -640263460,
    1088359270,
    936918000,
    -1447252397,
    -558129467,
    1202900863,
    817233897,
    -1111625188,
    -893730166,
    1404277552,
    615818150,
    -1160759803,
    -841546093,
    1423857449,
    601450431,
    -1285129682,
    -1000256840,
    1567103746,
    711928724,
    -1274298825,
    -1022587231,
    1510334235,
    755167117
]


def hash_o(e, t=0):
    def encode_utf8_char(r):
        if r < 128:
            return chr(r)
        elif r < 2048:
            return chr(192 | r >> 6) + chr(128 | 63 & r)
        elif r < 55296 or r >= 57344:
            return chr(224 | r >> 12) + chr(128 | r >> 6 & 63) + chr(128 | 63 & r)
        else:
            r = 65536 + ((1023 & r) << 10 | 1023 & ord(e[n + 1]))
            return (chr(240 | r >> 18) + chr(128 | r >> 12 & 63) +
                    chr(128 | r >> 6 & 63) + chr(128 | 63 & r))

    e = ''.join([encode_utf8_char(ord(c)) for c in e])
    t = ~t
    for n in range(len(e)):
        t = unsinged_right_shift(t,8) ^ r[255 & (t ^ ord(e[n]))]
    return unsinged_right_shift(~t ,0)


@retry(stop=stop_after_attempt(20), wait=wait_fixed(3), before=email_before_log, after=email_after_loger)
async def get_email(username, password,timestamp):
    get_url = f"http://{api_host}/temu_captch/receive-email?username={username}&password={password}&time={int(timestamp)-30}"
    print(get_url)
    resp = await client_tools.get(get_url)
    data = resp.json()
    if data['success'] and data['email_info']:
        email_info = data['email_info']
        return email_info
    raise Exception("验证码获取失败")


# @retry(stop=stop_after_attempt(20), wait=wait_fixed(3), before=email_before_log, after=email_after_loger)
# async def get_email(username,password=None,timestamp=None):
#     get_url = f"http://uspscc.com/api/getcode.php?&yhm={username}&mm=1"
#     resp = await client_tools.get(get_url)
#     if 'verification code in the Temu' in resp.text:
#         code= re.findall("[^0-9](\d{6})[^0-9]", resp.text)[0]
#         return {
#             "subject": code
#         }
#     raise Exception("验证码获取失败")


if __name__ == '__main__':
    # a = AsyncAnti({
    #     "Accept": "application/json, text/plain, */*",
    #     "Accept-Encoding": "gzip, deflate, br",
    #     "Accept-Language": "zh-CN,zh;q=0.9",
    #     #"Anti-Content": "0aqAfqnyX-Hg8gd9Q4ep3V2dn_GAssBxnZ4fciXuMoB-H1dEyvfPkyCEdqRnnQX3POYg3fby2Tg2zOjtKP2wmdZsvgOI9Fh7kxGtbtKPt84n3vA14LbstOo17i9AEWWb886nbi-BQw8q_TJZFH0XonOwTUUZoJJTBEhCqmAqOasN0xE9IR0eN6rb2Sa27ZkWN8R2yUxDiZAW1F1C1U9Dobulaj8NeUebaXqmb_WEOR2VU-5L4DEqeuT2eYMHI0SbsUhBVK61rCDk9GNYWzVQR9or5DIB1_eSixuvfIx5410v_cK2QY2Jdn5b6Ah6y89JrV2jQMKLV9IC-R3E7w1xZWKs55f5k4wBdWwlGZqMVTWqNY6RzXGWTd8Ev-1mrJ0FmjMrwDwXUEKjwyMdExKPMPTXLneiK_-kxcS_yM_0i4XskQdz4jVPinhM8JKxgHTzX2Xt0sZXyZmBfByyFbZwPhEIE4gXwkxYkxlF1TspenM54CfzXYvmIivQr4CY0mc-r2QiQMxYqiZHNWS7_uLwmSHi6ZupHuG8-zKDU8auNn_fkUMYdz-GYSkp9RKMIEbJ6EOjPpvvPxMpzsSZq2ZlLbpKl2xjTF35LczkgZSnwPMRbtI379ro7kSwLCfnHdyrjCHkBI_4scfng-HVmkgT77Zg4dbd9yV1XTvT3jutu_y1Sz-jkJopr-jwmlDljGR_4aEKicmQIy5pidimdjvuxUdbyWSQ6-qYwYUWJseK3rGDcGDaIgKJFLq5z8VGTJRVoe9K6Wv6DDrLAf0heWXWaF90tcdthqIU",
    #     "Content-Type": "application/json;charset=UTF-8",
    #     # "Cookie":'api_uid=CnDcb2XzCmx5KAEfRejwAg==; region=211; language=en; currency=USD;  timezone=Asia%2FShanghai; webp=1; _bee=XlM78xljkgQl0oWzDSY2EldlSeqAJapo; njrpl=XlM78xljkgQl0oWzDSY2EldlSeqAJapo; dilx=EYTbrLtdGR_Gno5OeRLit;',
    #     # "Cookie": f'api_uid={api_uid}; timezone=Asia%2FShanghai; shipping_city=211; webp=1; region=211; language=en; currency=USD;_bee={cookie_bee}; njrpl={cookie_bee}; dilx={cookie_dilx}; hfsc={cookie_hfsc}',
    #     "Origin": "https://www.temu.com",
    #     "Pragma": "no-cache",
    #     #"Referer": f'https://www.temu.com/channel/best-sellers.html?filter_items=1%3A1&scene=home_title_bar_recommend&refer_page_el_sn=201341&refer_page_name=home&refer_page_id=10005_{int(time.time() * 1000)}_{randam_10()}&refer_page_sn=10005&_x_sessn_id={randam_10()}',
    #     #"Referer":"https://www.temu.com",
    #     "Sec-Ch-Ua": "v=\"123\", \"Not_A;Brand\";v=\"24\", \"Google Chrome\";v=\"123\"",
    #     "Sec-Ch-Ua-Mobile": "?0",
    #     "Sec-Ch-Ua-Platform": "\"Windows\"",
    #     "Sec-Fetch-Dest": "empty",
    #     "Sec-Fetch-Mode": "cors",
    #     "Sec-Fetch-Site": "same-origin",
    #     "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
    # })
    # import asyncio
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # loop.run_until_complete(a.get_nano())
    #
    # a = asyncio.run(get_email('','',1))
    # print(a)

    # print(password_encrypt({"pub_key":"MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCI/6xg11SMEvUEqfP1C3U0/kG5f6ufxHVWnmqLNuRgUVvVWxfVeAWjnlEWONq8YRB6tlfp8/bDpxnzaqvczuuBpIUhCGtBe9WFKECk6hucdQrtgQnxecYbnm5wSe9NVf/TbADOHKbEzUbRd/nzar9r4q7P0yAajdzZ8VdIKgjK6wIDAQAB","key_version":57,"salt":"856e5b0632a4a526","server_time":1720779214,"nonce":"5b7ce9a975b473e5","sign":"f38e9979034e46d50beef5b3a66a85cd64c7e41b7b2db8bc41b60803aa534959"}, 'temu_data@123123'))
    print(asyncio.run(get_email('07ja4nsvabhs4@burning.icu', 'temu_data@123123', 0)))