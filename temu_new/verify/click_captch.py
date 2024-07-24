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

class ClickCaptcha(BaseCaptcha):

    def parse(self, data):
        text = base64.b64decode(self.decode_img(data["semantics"][0])).decode()
        image_data = {
            "imageSrc": data["pictures"][0],
            "positions": data["semantics"][2],
            "partialEncryption": 1,
        }
        image = self.decrypt(image_data).replace("data:image/png;base64,", '')
        return {
            "image": image,  # base64
            "text": text,
        }

    async def verify(self, data):
        capthca_data = self.parse(data)
        capthca_data["token"] = token
        r = await client_tools.post(f"http://{api_host}/temu_captch/identity",
                                    json=capthca_data
                                    )
        data = r.json()
        if data["code"] != 200:
            logger.error(f"验证码识别错误{data}")
            self.save(capthca_data)
            return False

        res = await self.verify_click(data["data"])
        return res

    async def verify_click(self, box_mid_xys):
        del_list = []
        mell = []
        mel = []
        verify_code = []
        for box_mid_xy in box_mid_xys:
            mel_item = []
            try:
                box_mid_xy = [int(box_mid_xy["box_mid_xy"][0]*0.7645), int(box_mid_xy["box_mid_xy"][1]*0.7645)]
            except:
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
                "event": True,
                "element": "captchaImg",
                "track": mel,
                "key": "verify"
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


