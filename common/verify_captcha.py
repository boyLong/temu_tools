# coding:utf-8
import os.path
import subprocess
from functools import partial
from py_mini_racer import py_mini_racer
import aiofiles
import json
from urllib import parse
import asyncio
null = None
import re
import time
import numpy as np
import secrets
import base64
import cv2
import random
from common.request import AsyncRequest
from common.cBezier import bezierTrajectory
from common.track import GTrace
from common.encrypt_tools import AsyncAnti,captcha_encrypt,identity,hash_o
from common.logger import logger
from common.config import get_gif_url
import io

verify_count = {
    "count": 0,
    "success": 0,
    "error": 0,
    "error_ide": 0,
}

bt = bezierTrajectory()

def get_id(e=21):
    chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    return "".join(secrets.choice(chars) for _ in range(e))

class VerifyCaptcha(object):
    def __init__(self,headers, session=None, proxy=True, ):

        self.headers = headers.copy()
        self.VerifyAuthToken = headers.get("Verifyauthtoken") or headers.get("verifyauthtoken")
        if not self.VerifyAuthToken:
            raise "没有VerifyCaptcha"
        cookie = headers.get("cookie") or headers.get("Cookie")

        if 'bgn_verification' not in headers.get("referer", headers.get("Referer", '')) :

            if headers.get("referer"):
                referer = headers.get("referer")
                self.headers["referer"] = (
                    f"https://www.temu.com/bgn_verification.html?VerifyAuthToken={self.VerifyAuthToken}&"
                    f"from={parse.quote_plus(referer)}")
            elif headers.get("Referer"):
                referer = headers.get("Referer")
                self.headers["Referer"] = (
                    f"https://www.temu.com/bgn_verification.html?VerifyAuthToken={self.VerifyAuthToken}&"
                    f"from={parse.quote_plus(referer)}")
            else:
                referer = "https://www.temu.com"

            self.base_referer = referer
        else:
            self.base_referer = headers.get("referer", headers.get("Referer", ''))

        try:
            nano = re.findall("_nano_fp=(.*?);", cookie) or re.findall("_nano_fp=(.*?)$",cookie) or ['']
        except:
            nano = [""]
        self.nano = nano[0]
        try:
            api_uid = re.findall("api_uid=(.*?);", cookie) or re.findall("api_uid=(.*?)$",cookie) or ['']
        except:
            api_uid = [""]

        try:
            _bee = re.findall("_bee=(.*?);", cookie) or re.findall("_bee=(.*?)$", cookie) or ['']
            njrpl = re.findall("njrpl=(.*?);", cookie) or re.findall("njrpl=(.*?)$", cookie) or ['']
            dilx = re.findall("dilx=(.*?);", cookie) or re.findall("dilx=(.*?)$", cookie) or ['']
            hfsc = re.findall("hfsc=(.*?);", cookie) or re.findall("hfsc=(.*?)$", cookie) or ['']
            self.region = re.findall("region=(.*?);", cookie) or re.findall("region=(.*?)$", cookie) or ['']
            self.region = self.region[0]
            self.currency = re.findall("currency=(.*?);", cookie) or re.findall("currency=(.*?)$", cookie) or ['']
            self.currency = self.currency[0]
            self.language = re.findall("language=(.*?);", cookie) or re.findall("language=(.*?)$", cookie) or ['']
            self.language = self.language[0]
            self.gif_cookie = f'api_uid={api_uid[0]}; _bee={_bee[0]}; njrpl={njrpl[0]}; dilx={dilx[0]}; hfsc={hfsc[0]}'
            self._bee = _bee[0]
        except:
            self.gif_cookie = ""
            self.region = "211"
            self.currency = "USD"
            self.language = "en"
        self.gif_url = get_gif_url(self.region)
        self.api_uid = api_uid[0]
        self.anti_count = 1
        self.ServerTime = None
        self.UpdateServerTime = None
        self.UpdateFirstServerTime = None
        self.get_server_time()

        self.img_info = {}
        self.session = session or AsyncRequest(proxy=proxy, headers=self.headers)
        if self.session.anti is None:
            anti = AsyncAnti(self.session.get_headers(),
                             lt_c=[71, 97, 12, 171],
                             gt_c=[217, 54, 250, 195],
                             _=[
                                "ã",
                                "#",
                                "\u0010",
                                "È"
                             ])
            self.session.anti = anti
        self.ctx = py_mini_racer.MiniRacer()
        self.eval_js()

    async def get_gif(self):

        query = parse.urlparse(self.base_referer).query
        info = parse.parse_qs(query)
        page_id = f"10017_{int(time.time() * 1000)}_{get_id(10)}"
        _x_sessn_id = info.get("_x_sessn_id")
        if not _x_sessn_id:
            _x_sessn_id = get_id(10)
        else:
            _x_sessn_id = _x_sessn_id[0]
        req_time = str(int(time.time() * 1000))

        dcf = hash_o(f"{req_time}pv1")
        data = {
            "page_sn": "10017",
            "page_id": page_id,
            "cli_timezone": "Asia/Shanghai",
            "cli_region": self.region,
            "cli_currency": self.currency,
            "cli_language": self.language,
            "_x_sessn_id": _x_sessn_id,
            "time": req_time,
            "log_id": f"{req_time}{get_id(16)}",
            "user_id": "",
            "uin": "",
            "app_id": "",
            "screen_width": "1980",
            "screen_height": "1080",
            "dpr": "1",
            "app_version": "",
            "platform": "browser",
            "plat_type": "pc",
            "cookie_fp": self.nano,
            "storage_fp": self.nano,
            "dcf": f".1.{dcf}",
            "bg_id": self._bee,
            "os_language": "zh-CN",
            "_ck_h_sequ": "0",
            "support_beacon": "1"
        }
        data["page_url"] = self.headers.get("referer")
        data["refer_url"] = ""
        if info.get("refer_page_name"):
            data["refer_page_name"] = info.get("refer_page_name")[0]
        if info.get("refer_page_id"):
            data["refer_page_id"] = info.get("refer_page_id")[0]
        if info.get("refer_page_sn"):
            data["refer_page_sn"] = info.get("refer_page_sn")[0]
        data.update(
            {
                "op": "pv",
                "event": "page_show",
            }
        )
        headers = {
            'accept': '*/*',
            'content-type': 'text/plain;charset=UTF-8',
            'origin': 'https://www.temu.com',
            'referer': 'https://www.temu.com/',
            "cookie": self.gif_cookie
        }
        await self.session.post(self.gif_url,
                                headers=headers,
                                data=data)
        dcf = hash_o(f"{req_time}impr1")

        data = {
            "page_sn": "10017",
            "page_id": page_id,
            "cli_timezone": "Asia/Shanghai",
            "cli_region": self.region,
            "cli_currency": self.currency,
            "cli_language": self.language,
            "_x_sessn_id": _x_sessn_id,
            "page_el_sn": "225383",
            "is_show": "0",
            "ndisp_rsn": "1",
            "op": "impr",
            "time": req_time,
            "log_id": f"{req_time}{get_id(16)}",
            "user_id": "",
            "uin": "",
            "app_id": "",
            "screen_width": "1980",
            "screen_height": "1080",
            "dpr": "1",
            "app_version": "",
            "platform": "browser",
            "plat_type": "pc",
            "cookie_fp": self.nano,
            "storage_fp": self.nano,
            "dcf": f".1.{dcf}",
            "bg_id": self._bee,
            "os_language": "zh-CN",
            "_ck_h_sequ": "1",
            "support_beacon": "1"
        }
        if info.get("refer_page_name"):
            data["refer_page_name"] = info.get("refer_page_name")[0]
        if info.get("refer_page_id"):
            data["refer_page_id"] = info.get("refer_page_id")[0]
        if info.get("refer_page_sn"):
            data["refer_page_sn"] = info.get("refer_page_sn")[0]
        await self.session.post(self.gif_url,
                                headers=headers,
                                data=data)
    async def get_init(self):

        # await self.session.
        url = "https://www.temu.com/api/phantom/vc_pre_ck"
        data = {
            "sdk_type": 1,
            "client_time": int(time.time() * 1000),
            "verify_auth_token": self.VerifyAuthToken,
        }

        resp = await self.session.post(url=url, json=data, anti={
            "event": False
        })
        data = resp.json()
        if not data["success"]:
            raise Exception("验证码token失效")
        return data

    def get_server_time(self):
        self.ServerTime = int(time.time() * 1000-random.randint(1000,2000))
        self.UpdateServerTime = int(time.time() * 1000)
        self.UpdateFirstServerTime = self.UpdateServerTime - random.randint(50,120)

    @staticmethod
    def read_img2(img):
        image_stream = io.BytesIO()
        image_stream.write(base64.b64decode(img))
        image_stream.seek(0)
        return image_stream

    async def save_img(self, filename, img):
        try:
            async with aiofiles.open(os.path.join("img", filename), mode="wb") as f:
                await f.write(img)
        except Exception:
            logger.error("错误图片报错失败")
            pass

    def eval_js(self):
        js = """var u =[
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        24,
        3,
        -1,
        20,
        -1,
        17,
        8,
        -1,
        30,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        12,
        22,
        10,
        -1,
        -1,
        15,
        14,
        6,
        -1,
        5,
        -1,
        -1,
        7,
        18,
        -1,
        25,
        9,
        -1,
        28,
        -1,
        2,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        1,
        21,
        -1,
        31,
        13,
        16,
        -1,
        26,
        -1,
        27,
        -1,
        0,
        19,
        -1,
        11,
        4,
        -1,
        -1,
        23,
        -1,
        29,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1
    ]
    function decode(t) {
        var e = t.length;
        if (e % 8 != 0)
            return null;
        for (var n = [], r = 0; r < e; r += 8) {
            var i = u[t["charCodeAt"](r)]
            , o = u[t["charCodeAt"](r + 1)]
            , a = u[t["charCodeAt"](r + 2)]
            , c = u[t["charCodeAt"](r + 3)]
            , s = u[t["charCodeAt"](r + 4)]
            , x = u[t.charCodeAt(r + 5)]
            , d = u[t["charCodeAt"](r + 6)]
            , l = (31 & i) << 3 | (31 & o) >> 2
            , h = (3 & o) << 6 | (31 & a) << 1 | (31 & c) >> 4
            , v = (15 & c) << 4 | (31 & s) >> 1
            , p = (1 & s) << 7 | (31 & x) << 2 | (31 & d) >> 3
            , b = (7 & d) << 5 | 31 & u[t["charCodeAt"](r + 7)];
            n["push"](String['fromCharCode']((31 & l) << 3 | h >> 5)),
            n.push(String.fromCharCode((31 & h) << 3 | v >> 5)),
            n["push"](String.fromCharCode((31 & v) << 3 | p >> 5)),
            n.push(String.fromCharCode((31 & p) << 3 | b >> 5)),
            n["push"](String['fromCharCode']((31 & b) << 3 | l >> 5))
        }
        var y = n.join("");
        return (y = (y = (y = y['replace']("#", ""))["replace"]("@?", "")).replace("*&%", "")).replace("<$|>", "")
    }"""
        self.ctx.eval(js)


    def decode_img(self, img):
        return self.ctx.call("decode", img)

    @staticmethod
    def identify_gap_old(bg, tp):
        bg_edge = cv2.Canny(bg, 100, 200)
        tp_edge = cv2.Canny(tp, 100, 200)

        # 转换图片格式
        bg_pic = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)
        tp_pic = cv2.cvtColor(tp_edge, cv2.COLOR_GRAY2RGB)

        # 缺口匹配
        res = cv2.matchTemplate(bg_pic, tp_pic, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 寻找最优匹配

        return max_loc


    def encrypt_23(self, e):
        d = json.loads(self.decode_img(e["positions"]))["positions"]
        s = ""
        n = e["imageSrc"]
        l = 0
        for v in range(len(d)):
            h = d[v] if v < len(d) else {}
            m = h.get("index", 0)
            b = h.get("length", 0)
            g = ""
            if v == 0:
                if m > 0:
                    g = n[:m]
            else:
                g = n[l:m]

            s += g + self.decode_img(n[m : m + b])  # 替换部分字符串
            l = m + b

        s += n[l:]
        return s

    async def start(self):
        logger.info("验证码识别开始")
        print()
        await self.session.get(self.headers.get("referer"))
        await self.get_gif()
        self.init_info = await self.get_init()
        verify_count["count"] += 1
        while 1:
            try:
                captcha = await self.get_captcha()
                res = await self.handle(captcha)
                print(res)
                if res:
                    logger.info(f"验证识别通过")
                    return True
            except Exception as e:
                import traceback
                traceback.print_exc()
                logger.error(f"验证识别失败了。。。。{e}")
                return False

    async def get_captcha(self):
        logger.info("开始获取验证吗")
        screen = {"w": 1980, "h": 1080}
        data = {
            "v": "a",
            "ts": self.init_info["server_time"],
            "t0": int(time.time() * 1000),
            "tp": 1,
            "ua": self.headers.get("user-agent") or self.headers.get("User-Agent"),
            "rf": self.headers.get("Referer") or self.headers.get("referer"),
            "hl": "000000000001010",
            "sc": screen,
            "ihs": 1,
            "platform": 1,
        }

        captcha_collect = await captcha_encrypt(data,self.init_info)


        response = await self.session.post(
            "https://www.temu.com/api/phantom/obtain_captcha",
            json={
                "verify_auth_token": self.VerifyAuthToken,
                "captcha_collect": captcha_collect["data"],
                "salt": self.init_info["salt"],
                "reverse": False,
                "encrypt_version": 1,
            },
            anti={
              "event": False
            }
        )
        self.t1 = int(time.time() * 1000)
        logger.info("验证吗获取完成")
        return response.json()


    async def handle(self, data):
        if data["type"] == 23:
            logger.info("滑动验证码开始滑动")
            if len(data["semantics"]) == 6:
                image1_data = {
                    "imageSrc": data["pictures"][1],
                    "positions": data["semantics"][4],
                    "partialEncryption": 1,
                }
                image1 = self.encrypt_23(image1_data)
                image1 = np.asarray(
                    bytearray(
                        base64.b64decode(image1.replace("data:image/png;base64,", ""))
                    ),
                    dtype="uint8",
                )
                image1 = cv2.imdecode(image1, cv2.IMREAD_COLOR)
                image2_data = {
                    "imageSrc": data["pictures"][2],
                    "positions": data["semantics"][5],
                    "partialEncryption": 1,
                }
                image2 = self.encrypt_23(image2_data)
                image2 = np.asarray(
                    bytearray(
                        base64.b64decode(image2.replace("data:image/png;base64,", ""))
                    ),
                    dtype="uint8",
                )
                image2 = cv2.imdecode(image2, cv2.IMREAD_COLOR)
            else:
                pictures = data["pictures"]
                image1 = self.decode_img(pictures[1])
                image1 = np.asarray(
                    bytearray(
                        base64.b64decode(image1.replace("data:image/png;base64,", ""))
                    ),
                    dtype="uint8",
                )
                image1 = cv2.imdecode(image1, cv2.IMREAD_COLOR)

                image2 = self.decode_img(pictures[2])
                image2 = np.asarray(
                    bytearray(
                        base64.b64decode(image2.replace("data:image/png;base64,", ""))
                    ),
                    dtype="uint8",
                )
                image2 = cv2.imdecode(image2, cv2.IMREAD_COLOR)
            s = self.identify_gap_old(image1, image2)
            verify_code = int(s[0] * (250 / 320)) + 24
            s = int((s[0] + 30) * (250 / 320))

            if data["type"] != 22:
                sign = base64.b64decode(self.decode_img(data["semantics"][0])).decode()
            else:
                sign = ""
            res = await self.verify(s, verify_code, sign)
            return res

        elif data["type"] == 11:
            logger.info("点选验证码开始识别")
            text = base64.b64decode(self.decode_img(data["semantics"][0])).decode()
            image_data = {
                "imageSrc": data["pictures"][0],
                "positions": data["semantics"][2],
                "partialEncryption": 1,
            }
            image = self.encrypt_23(image_data).replace("data:image/png;base64,", '')

            data = {
                "image": image,  # base64
                "text": text,
            }
            self.img_info = data
            try:
                c = await identity(data)
            except Exception as e:
                filename = f"识别服务报错_{int(time.time())}_{text.replace(' ','_')}.png"
                verify_count["error_ide"] += 1
                logger.error(f"验证吗识别报错,{e},重新去获取验证吗")
                await self.save_img(filename,base64.b64decode(image))
                return False
            res = await self.verify_click(c["data"])
            return res
        else:
            with open("新的滑块",'a') as w:
                w.write(json.dumps(data)+"\n")
            raise Exception("不知道的滑块")

    async def verify(self, s, verify_code, sign):
        data_points = bt.trackArray(
            [random.randint(-650, -400), random.randint(-300, -100)],
            [random.randint(15, 25), random.randint(157, 162)],
            numberList=random.randint(40, 50),
            le=4,
            type=3,
            bias=0.5,
            deviation=30,
            cbb=1,
            yhh=2,
        )
        data_points = [[int(x), int(y)] for x, y in data_points["trackArray"]]
        mell = [[]]
        for i in data_points:
            await asyncio.sleep(random.randint(15, 25) / 1000)
            mell[0].append(
                [
                    i[0],
                    i[1],
                    int(time.time() * 1000),
                ]
            )
        await asyncio.sleep(25 / 1000)
        del_time = int(time.time() * 1000)
        del_arr = [
            [
                data_points[-1][0] + random.randint(0, 3),
                160 + random.randint(-4, 2),
                ]
        ]
        uel_arr = [
            [
                s,
                160 + random.randint(-4, 2),
                ]
        ]
        mel = []
        await asyncio.sleep(25 / 1000)
        track = GTrace()
        track_array = track.get_mouse_pos_path(s)[1][2:]

        del_arr[0].append(del_time)
        next_time = track_array[0][2]
        for pos in track_array:
            try:
                await asyncio.sleep((pos[2] - next_time) / 1000)
            except:
                pass
            mel.append([pos[0], 160 + pos[1], int(time.time() * 1000)])
            next_time = pos[2]

        uel_arr[0].append(int(time.time() * 1000))
        mell.append(mel)
        await asyncio.sleep(random.randint(150, 250) / 1000)
        screen = {"w": 1980, "h": 1080}
        data = {
            "v": "a",
            "ts": self.init_info["server_time"],
            "t1": self.t1,
            "t2": int(time.time() * 1000),
            "tp": 1,
            "ua": self.headers.get("user-agent") or self.headers.get("User-Agent"),
            "rf": self.headers.get("Referer") or self.headers.get("referer"),
            "platform": 1,
            "hl": "000000000001010",
            "sc": screen,
            "ihs": 1,
            "imageSize": {"width": 250, "height": 125},
            "uel": uel_arr,
            "mel": mel,
            "del": del_arr,
            "mell": mell,
        }
        logger.info("轨迹生成完成")
        captcha_collect = await captcha_encrypt(data, self.init_info)

        captcha_collect = captcha_collect
        url = "https://www.temu.com/api/phantom/user_verify"
        data = {
            "verify_auth_token": self.VerifyAuthToken,
            "salt": self.init_info["salt"],
            "captcha_collect": captcha_collect["data"],
            "reverse": False,
            "verify_code": verify_code,
        }
        response = await self.session.post(
            url,
            json=data,
            anti={
                "event":True,
                "track": mel
            }

        )
        res = response.json()
        if res["code"] == 0:
            verify_count["success"] += 1
            return True
        else:
            verify_count["error"] += 1
            logger.error(f"识别坐标错误,再次识别,剩余{res['leftover']}")
            if res["leftover"]:
                return False
            else:
                raise Exception("验证码次数全部用完")

    async def verify_click(self, box_mid_xys):
        del_list = []
        mell = []
        mel = []
        verify_code = []
        for box_mid_xy in box_mid_xys:
            mel_item = []
            try:
                box_mid_xy = [int(box_mid_xy["box_mid_xy"][0]), int(box_mid_xy["box_mid_xy"][1])]
            except:
                verify_count["error_ide"] += 1
                logger.error("坐标返回错误", box_mid_xy)
                file = f"坐标返回错误_{int(time.time())}_{self.img_info['text'].replace(' ', '_')}.png"
                await self.save_img(file, base64.b64decode(self.img_info["image"]))
                return False
            verify_code.append({"x":box_mid_xy[0],"y":box_mid_xy[1]})
            d = bt.trackArray(
                [random.randint(300, 400), random.randint(100, 150)],
                box_mid_xy,
                numberList=random.randint(25, 35),
                le=10,
                type=3,
                bias=0.9,
                deviation=100,
                cbb=2,
                yhh=200,
            )
            trackArray = [[int(x), int(y)] for x, y in d["trackArray"]]
            for i in trackArray:
                await asyncio.sleep(random.randint(10, 25) / 1000)
                m = [
                    i[0] + 0.7,
                    i[1] + 0.7,
                    int(time.time() * 1000),
                    ]
                mel_item.append(m)
                mel.append(m)
            mell.append(mel_item)
            del_ = mel_item[-1].copy()
            del_[2] + random.randint(100,200)
            del_list.append(del_)

        screen = {"w": 1980, "h": 1080}
        data = {
            "v": "a",
            "ts": self.init_info["server_time"],
            "t1": self.t1,
            "t2": int(time.time() * 1000),
            "tp": 1,
            "ua": self.headers.get("user-agent") or self.headers.get("User-Agent"),
            "rf": self.headers.get("Referer") or self.headers.get("referer"),
            "platform": 1,
            "hl": "000000000001010",
            "sc": screen,
            "ihs": 1,
            "imageSize": {"width": 250, "height": 125},
            "uel": [],
            "mel": mel,
            "del": del_list,
            "mell": mell,
            "orientation": [],
            "gyroscope": []
        }

        captcha_collect = await captcha_encrypt(data, self.init_info)
        logger.info("轨迹构造完成,开始提交")
        url = "https://www.temu.com/api/phantom/user_verify"
        data = {
            "verify_auth_token": self.VerifyAuthToken,
            "salt": self.init_info["salt"],
            "captcha_collect": captcha_collect["data"],
            "reverse": False,
            "verify_code": json.dumps(verify_code,separators=(',', ':')),
        }

        response = await self.session.post(
            url,
            json=data,
            anti={
                "event":True,
                "track": mel
            }
        )
        res = response.json()
        if res["code"] == 0:
            print(res)
            verify_count["success"] += 1
            return True
        else:
            verify_count["error"] += 1
            logger.error(f"识别坐标错误,再次识别,剩余{res['leftover']}")

            file = f"识别的坐标不对_{int(time.time())}_{self.img_info['text'].replace(' ','_')}.png"
            await self.save_img(file, base64.b64decode(self.img_info["image"]))
            if res["leftover"]:

                return False
            else:
                raise Exception("验证码次数全部用完")


if __name__ == '__main__':

    vc = VerifyCaptcha(
        headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        'cookie': 'region=211; language=en; currency=USD; api_uid=Cm3GdmYnd0WIgAB6WiKZAg==; timezone=Asia%2FShanghai; webp=1; _nano_fp=XpmaXqCjX5TJX5dono_kATLOtjFRvA5REZ9uhvzn; verifyAuthToken=c_lCBSF3lk082wqRUpZIQAb89db9f7f3ad8bb7a; _bee=KDJSXxjhneGpiuav2XnvERGNV88x4ap4; njrpl=KDJSXxjhneGpiuav2XnvERGNV88x4ap4; dilx=vSMbbXCXMx1UJRmWNQu3o; hfsc=L3yLe4E26zr/1JLMeg==; _ttc=3.Db7RTXGcLAD5.1745398601; __cf_bm=FrynRVbHAj0DUO6MYLbe5Wu5bp.fpLqGmSxXAQA4078-1713868323-1.0.1.1-LmbBdZQd8A_SmKbg.Y85dQ8yOU4D_NmJmDJWttV3Tnb3qXD0BSCeJm7O5.VuyMOipVFnUMe3m8hBn.xyNzXXOw; _device_tag=CgI2WRIIWG9MU3RkbnkaMP7pL4O3ohBSVBCt4m5P9TUh/U1xPkfh3ibmTl7hcVHXk64ZYogVSw6JgFF0lRzKnjAC; AccessToken=PKDXDERQTWZ23JULJIQ2WVZFGKXBIEAV3AIRBEAH7VER6YWHQDLA0110d3abd149; user_uin=BCU7UQQ6GNND54L6ZYUWVF5HF2LH3P5JKPQTZAQ7; isLogin=1713868346759; _u_pa=%7B%22nrpt_211%22%3A0%7D',
        'origin': 'https://www.temu.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.temu.com/bgn_verification.html?VerifyAuthToken=CSCt_IoKnzhw0pTRLe7sEw6afd0a826084ff9aa&from=https%3A%2F%2Fwww.temu.com%2F%3Frefer_page_name%3Dhome%26refer_page_id%3D10005_1713868333971_l291e9hyae%26refer_page_sn%3D10005&_x_sessn_id=k7ii9dznnb&refer_page_name=home&refer_page_id=10005_1713868358392_9v9sq5oiu9&refer_page_sn=10005',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'verifyauthtoken': 'CSCt_IoKnzhw0pTRLe7sEw6afd0a826084ff9aa',
        }

    )
    import asyncio
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(vc.start())
