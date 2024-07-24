import json
import base64
import cv2
from common.encrypt_tools import client_tools, captcha_encrypt
from verify.track.cBezier import bt
from verify.track.gt_track import GTrace
from common.Request import Request
from verify.BaseCaptch import BaseCaptcha
import numpy as np
import random
import time
import asyncio
from common.logger import logger


class SlideCaptcha(BaseCaptcha):
    def __init__(self,init_info,VerifyAuthToken, start_time=None, headers=None, session=None, proxy=True):
        self.init_info = init_info
        self.VerifyAuthToken = VerifyAuthToken
        self.headers = headers
        self.start_time = start_time or int(time.time()*1000)
        self.session = session or Request(proxy=proxy, headers=self.headers)

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

            s += g + self.decode_img(n[m: m + b])  # 替换部分字符串
            l = m + b

        s += n[l:]
        return s

    def identify_gap(self, bg, tp):
        bg_edge = cv2.Canny(bg, 100, 200)
        tp_edge = cv2.Canny(tp, 100, 200)

        # 转换图片格式
        bg_pic = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)
        tp_pic = cv2.cvtColor(tp_edge, cv2.COLOR_GRAY2RGB)

        # 缺口匹配
        res = cv2.matchTemplate(bg_pic, tp_pic, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 寻找最优匹配
        return max_loc

    def slide_captcha(self, data):
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
        s = self.identify_gap(image1, image2)
        return s

    async def verify(self, s):
        verify_code = int(s[0] * (250 / 320)) + 24

        s = int((s[0] + 30) * (250 / 320))
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
            "t1": self.start_time,
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
        return response.json()


