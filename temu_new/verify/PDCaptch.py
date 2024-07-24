from verify.BaseCaptch import BaseCaptcha
import json
import base64
from common.encrypt_tools import client_tools,captcha_encrypt
from verify.track.cBezier import bt
from common.config import token
import random
import time
import asyncio
from common.logger import logger
from common.config import api_host

class PDCaptcha(BaseCaptcha):

    def parse(self, data):

        size = base64.b64decode(self.decode_img(data["text"][0])).decode()

        image_data = {
            "imageSrc": data["pictures"][0],
            "positions": data["semantics"][0],
            "partialEncryption": True,
        }
        image = self.decrypt(image_data).replace("data:image/png;base64,", '')


        return {
            "image": image,  # base64
            "model": int(size),
        }

    async def verify(self, data):
        data = self.parse(data)
        data["token"] = token
        size = data["model"]
        r = await client_tools.post(f"http://{api_host}/temu_captch/pd",
                                    json=data
                                    )
        data = r.json()
        if data["code"] != 200:
            logger.error(f"验证码识别错误{data}")
            return False
        verify_code = data["data"]
        end_x, end_y, u_x, u_y = await self.get_coordinate(verify_code, size)

        track_data = await self.get_track(end_x, end_y, u_x, u_y)
        mel = track_data["mel"]
        captcha_collect = await captcha_encrypt(track_data, self.init_info)
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
                "event": True,
                "track": mel,
                "key":"verify"
            }
        )
        res = response.json()
        if res["code"] == 0:
            return True
        else:
            if res["leftover"]:
                return False
            else:
                raise Exception("验证码次数全部用完")


    async def get_track(self, end_x, end_y, u_x, u_y):
        data_points = bt.trackArray(
            [random.randint(-650, -400), random.randint(-300, -100)],
            [end_x, end_y],
            numberList=random.randint(40, 50),
            le=4,
            type=3,
            bias=0.5,
            deviation=30,
            cbb=1,
            yhh=2,
        )
        data_points = [[int(x), int(y)] for x, y in data_points["trackArray"]]
        mell = []
        mel = []
        for i in data_points:
            await asyncio.sleep(random.randint(15, 25) / 1000)
            mel.append(
                [
                    i[0],
                    i[1],
                    int(time.time() * 1000),
                ]
            )
        mell.append(mel)
        await asyncio.sleep(25 / 1000)

        del_arr = [
            [
                data_points[-1][0],
                data_points[-1][1],
                int(time.time() * 1000),
            ]
        ]

        await asyncio.sleep(25 / 1000)
        # 上面随机轨迹切换滑动轨迹
        data_points = bt.trackArray(
            [end_x, end_y],
            [u_x,
             u_y, ],
            numberList=random.randint(40, 50),
            le=4,
            type=3,
            bias=0.5,
            deviation=30,
            cbb=1,
            yhh=2,
        )
        data_points = [[int(x), int(y)] for x, y in data_points["trackArray"]]
        mel_2 = []
        for i in data_points:
            await asyncio.sleep(random.randint(15, 25) / 1000)
            mel_2.append(
                [
                    i[0],
                    i[1],
                    int(time.time() * 1000),
                ]
            )

        mell.append(mel_2)
        mel.extend(mel_2)
        await asyncio.sleep(random.randint(150, 250) / 1000)
        uel_arr = [
            [
                u_x,
                u_y,
                int(time.time() * 1000),
            ]
        ]
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
            "orientation": [],
            "gyroscope": []
        }
        logger.info("轨迹生成完成")
        return data

    async def get_coordinate(self, verify_code, size):
        block = 240/size
        if size == 6:
            if verify_code[0] < 3:
                end_x = random.randint(verify_code[0] * block, (verify_code[0] + 1) * block)
                end_y = random.randint(-80, -20)
            else:
                end_x = random.randint((verify_code[0]-3)* block, (verify_code[0] -2) * block)

                end_y = random.randint(-120, -80)

            if verify_code[1] < 3:
                u_x = random.randint(verify_code[1] * block, (verify_code[1] + 1) * block)

                u_y = random.randint(-80, -20)
            else:
                u_x = random.randint((verify_code[1]-3) * block, (verify_code[1] - 2) * block)

                u_y = random.randint(-120, -80)
        else:
            if verify_code[0] < 4:
                end_x = random.randint(verify_code[0] * block, (verify_code[0] + 1) * block)

                end_y = random.randint(-80, -20)
            else:
                end_x = random.randint((verify_code[0]-4)* block, (verify_code[0] - 3) * block)
                end_y = random.randint(-120, -80)

            if verify_code[1] < 3:
                u_x = random.randint(verify_code[1] * block, (verify_code[1] + 1) * block)

                u_y = random.randint(-80, -20)
            else:
                u_x = random.randint((verify_code[1]-3) * block, (verify_code[1] - 2) * block)
                u_y = random.randint(-120, -80)

        return end_x, end_y, u_x, u_y