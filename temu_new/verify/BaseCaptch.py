import base64
import os.path

from common.Request import Request
import time
from abc import abstractmethod
import py_mini_racer
import json

ctx = py_mini_racer.MiniRacer()
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
ctx.eval(js)


class BaseCaptcha(object):
    def __init__(self,init_info,VerifyAuthToken, start_time=None, headers=None, session=None, proxy=True):
        self.init_info = init_info
        self.VerifyAuthToken = VerifyAuthToken
        self.start_time = start_time or int(time.time()*1000)
        if session:
            self.session = session
            self.headers = session.get_headers()
        else:
            if not headers:
                raise Exception("必须传入headers")
            self.headers = headers
            self.session = Request(proxy=proxy, headers=self.headers)

    def save(self, info):
        image = info["image"]
        t = int(time.time())
        if isinstance(image, str):
            file = os.path.join("img", f"{t}_{info['text']}.png".replace(' ', '_'))
            with open(file, "wb") as f:
                f.write(base64.b64decode(image))
        else:
            index = 0
            for i in image:
                file = os.path.join("img", f"{t}_{info['text']}_{index}.png".replace(' ', '_'))
                with open(file, "wb") as f:
                    f.write(base64.b64decode(i))
                index += 1
    def decode_img(self, img):
        return ctx.call("decode", img)

    def decrypt(self, e):
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

    @abstractmethod
    async def verify(self, data):
        pass

