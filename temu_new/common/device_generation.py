# coding:utf-8
import asyncio
import hashlib
import json
import random
import secrets
import re
import time

false = False
true = True
null = None
from common.encrypt_tools import get_a4


class DeviceGeneration:
    """
    生成设备的信息，用于加密计算
    """

    def __init__(
        self,
        headers=None,
        device=None
    ) -> None:
        self.screen = random.choice(
            [
                [1920, 1080],
                [2560, 1440],
                [3840, 2160],
                [1366, 768],
                [7680, 4320],
                [1280, 1024],
                [1680, 1050],
            ]
        )
        self.performance_time = self.get_performanceTime()
        self.deviceMemory = random.choice([8, 16, 32])
        self.hardwareConcurrency = random.choice([8, 16, 20, 32])
        self.webGL = random.choice(
            [
                [
                    "Google Inc.",
                    "ANGLE (Intel(R) HD Graphics Direct3D11 vs_5_0 ps_5_0)",
                ],
                [
                    "Google Inc.",
                    "ANGLE (AMD Radeon (TM) R9 370 Series Direct3D11 vs_5_0 ps_5_0)",
                ],
                ["Google Inc.", "ANGLE (NVIDIA Quadro K600 Direct3D11 vs_5_0 ps_5_0)"],
                ["Google Inc.", "Intel(R) HD Graphics 4600"],
                ["ATI Technologies Inc.", "AMD Radeon R9 M370X OpenGL Engine"],
                [
                    "Google Inc.",
                    "ANGLE (NVIDIA Quadro M1000M Direct3D11 vs_5_0 ps_5_0)",
                ],
                [
                    "Google Inc. (Intel)",
                    "ANGLE (Intel, Intel(R) UHD Graphics (0x00009B41) Direct3D11 vs_5_0 ps_5_0, D3D11)",
                ],
            ]
        )
        self.fonts = list(
            "000000000001000000000000000000001000000100000000000000000001000000000000010000000000000000000000000000000000000000000000000110110"
        )
        for i in random.choices(range(129), k=random.randint(5, 10)):
            self.fonts[i] = "1"
        self.fonts = "".join(self.fonts)

        l = [self.fonts[f : f + 5] for f in range(0, 256, 5)]

        self.fonts = "".join([str(hex(int(i, base=2)))[2:] if i else "NaN" for i in l])

        self.FKGJ = self.get_FKGJ()
        self.availableScreenResolution = [
            self.screen[0],
            self.screen[1] - random.randint(45, 100),
        ]
        self.languages = self.get_languages()
        self.h = random.randint(90, 130)
        self.headers = headers
        self.ua = headers.get("User-Agent") or headers.get("user-agent")
        self.device = device or {}
        self.headerCache = ''
        self.moveData = []
        self.clickData = []

    def get_FKGJ(self, e=21):
        chars = "Uint8ArdomValuesObj012345679BCDEFGHIJKLMNPQRSTWXYZ_cfghkpqvwxyz~"
        return "".join(secrets.choice(chars) for _ in range(e))

    def get_webGLInfos(self):
        return [
            self.webGL[0],
            self.webGL[1],
            "WebKit",
            "WebKit WebGL",
            "WebGL 1.0 (OpenGL ES 2.0 Chromium)",
        ]

    def init_device(self, text=''):


        self.device = {
            "moveData": self.moveData,
            "clickData": self.clickData,
            "inputData": [],
            "blurData": [],
            "pasteData": "0",
            "headerCache": {
                "a": null,
                "b": self.headerCache,
                "c": null,
                "d": null,
                "e": null,
                "f": null,
                "g": null
            },
            "uid": "",
            "FKGJ": self.get_FKGJ(),
            "rawData": self.get_rawData(),
            "hasSensor": '{"gyroFlag":false,"acceFlag":false}',
            "isFront": "true",
            "webGLInfos": json.dumps(self.get_webGLInfos(), separators=(",", ":")),
            "windowSize": json.dumps(
                self.availableScreenResolution, separators=(",", ":")
            ),
            "winSelenium": "false",
            "chromium": "false",
            "headlessByProperties": "true",
            "languages": json.dumps(self.languages, separators=(",", ":")),
            "consoleLied": "false",
            "chromeExtensionScripts": "[]",
            "extensionImgs": json.dumps(
                self.get_extension_imgs(text), separators=(",", ":")
            ),
            "hookFuncs": '["Function.toString"]',
            "frontReferer": self.headers.get("referer") or self.headers.get("Referer"),
            "cssFeatures": "1288296882",
            "webglFt": json.dumps(self.get_webgl_f_t(), separators=(",", ":")),
            "performanceTime": json.dumps(
                self.performance_time, separators=(",", ":")
            ),
            "emptyEvalLength": "33",
            "errorFF": "false",
            "h5Features": json.dumps(self.get_h5features(), separators=(",", ":")),
            "fonts": self.fonts,
            "localIp": "0.0.0.0",
            "localIpDuration": random.randint(100, 300),
        }
        return self.device

    def generate_device(self, text=""):
        if not self.device:
            self.init_device(text=text)
        return self.device

    def reload(self, text="", headers=None, headerCache=""):
        if headerCache:
            self.headerCache = headerCache
        if headers:
            self.headers=headers
        if self.device:
            self.device.update(
                {
                    "extensionImgs": json.dumps(
                        self.get_extension_imgs(text), separators=(",", ":")
                    ),
                }
            )
            self.device.update({
                "frontReferer": self.headers.get("Referer") or self.headers.get("referer",'https://www.temu.com'),
            })

            self.device.update({
                "headerCache": self.headerCache
            })
            return self.device
        return self.generate_device(text=text)

    def get_webgl_f_t(self):
        webglFt = {
            "ALIASED_POINT_SIZE_RANGE": [1, 1024],
            "ALIASED_LINE_WIDTH_RANGE": [1, 1],
            "STENCIL_VALUE_MASK": 2147483647,
            "STENCIL_WRITEMASK": 2147483647,
            "STENCIL_BACK_VALUE_MASK": 2147483647,
            "STENCIL_BACK_WRITEMASK": 2147483647,
            "MAX_TEXTURE_SIZE": 16384,
            "MAX_VIEWPORT_DIMS": [32767, 32767],
            "SUBPIXEL_BITS": 4,
            "MAX_VERTEX_ATTRIBS": 16,
            "MAX_VERTEX_UNIFORM_VECTORS": 4096,
            "MAX_VARYING_VECTORS": 30,
            "MAX_COMBINED_TEXTURE_IMAGE_UNITS": 32,
            "MAX_VERTEX_TEXTURE_IMAGE_UNITS": 16,
            "MAX_TEXTURE_IMAGE_UNITS": 16,
            "MAX_FRAGMENT_UNIFORM_VECTORS": 1024,
            "SHADING_LANGUAGE_VERSION": "WebGL GLSL ES 3.00 (OpenGL ES GLSL ES 3.0 Chromium)",
            "VENDOR": "WebKit",
            "RENDERER": "WebKit WebGL",
            "VERSION": "WebGL 2.0 (OpenGL ES 3.0 Chromium)",
            "MAX_CUBE_MAP_TEXTURE_SIZE": 16384,
            "MAX_RENDERBUFFER_SIZE": 16384,
            "UNMASKED_VENDOR_WEBGL": self.webGL[0],
            "UNMASKED_RENDERER_WEBGL": self.webGL[1],
            "MAX_3D_TEXTURE_SIZE": 2048,
            "MAX_ELEMENTS_VERTICES": 2147483647,
            "MAX_ELEMENTS_INDICES": 2147483647,
            "MAX_TEXTURE_LOD_BIAS": 2,
            "MAX_DRAW_BUFFERS": 8,
            "MAX_FRAGMENT_UNIFORM_COMPONENTS": 4096,
            "MAX_VERTEX_UNIFORM_COMPONENTS": 16384,
            "MAX_ARRAY_TEXTURE_LAYERS": 2048,
            "MAX_PROGRAM_TEXEL_OFFSET": 7,
            "MAX_VARYING_COMPONENTS": 120,
            "MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS": 4,
            "MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS": 120,
            "MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS": 4,
            "MAX_COLOR_ATTACHMENTS": 8,
            "MAX_SAMPLES": 16,
            "MAX_VERTEX_UNIFORM_BLOCKS": 12,
            "MAX_FRAGMENT_UNIFORM_BLOCKS": 12,
            "MAX_COMBINED_UNIFORM_BLOCKS": 24,
            "MAX_UNIFORM_BUFFER_BINDINGS": 24,
            "MAX_UNIFORM_BLOCK_SIZE": 65536,
            "MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS": 212992,
            "MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS": 200704,
            "MAX_VERTEX_OUTPUT_COMPONENTS": 120,
            "MAX_FRAGMENT_INPUT_COMPONENTS": 120,
            "MAX_SERVER_WAIT_TIMEOUT": 0,
            "MAX_ELEMENT_INDEX": 4294967294,
            "MAX_CLIENT_WAIT_TIMEOUT_WEBGL": 0,
            "antialias": True,
            "MAX_TEXTURE_MAX_ANISOTROPY_EXT": 16,
            "VERTEX_SHADER.LOW_FLOAT.precision": 23,
            "VERTEX_SHADER.LOW_FLOAT.rangeMax": 127,
            "VERTEX_SHADER.LOW_FLOAT.rangeMin": 127,
            "VERTEX_SHADER.MEDIUM_FLOAT.precision": 23,
            "VERTEX_SHADER.MEDIUM_FLOAT.rangeMax": 127,
            "VERTEX_SHADER.MEDIUM_FLOAT.rangeMin": 127,
            "VERTEX_SHADER.HIGH_FLOAT.precision": 23,
            "VERTEX_SHADER.HIGH_FLOAT.rangeMax": 127,
            "VERTEX_SHADER.HIGH_FLOAT.rangeMin": 127,
            "VERTEX_SHADER.HIGH_INT.precision": 0,
            "VERTEX_SHADER.HIGH_INT.rangeMax": 30,
            "VERTEX_SHADER.HIGH_INT.rangeMin": 31,
            "FRAGMENT_SHADER.LOW_FLOAT.precision": 23,
            "FRAGMENT_SHADER.LOW_FLOAT.rangeMax": 127,
            "FRAGMENT_SHADER.LOW_FLOAT.rangeMin": 127,
            "FRAGMENT_SHADER.MEDIUM_FLOAT.precision": 23,
            "FRAGMENT_SHADER.MEDIUM_FLOAT.rangeMax": 127,
            "FRAGMENT_SHADER.MEDIUM_FLOAT.rangeMin": 127,
            "FRAGMENT_SHADER.HIGH_FLOAT.precision": 23,
            "FRAGMENT_SHADER.HIGH_FLOAT.rangeMax": 127,
            "FRAGMENT_SHADER.HIGH_FLOAT.rangeMin": 127,
            "FRAGMENT_SHADER.HIGH_INT.precision": 0,
            "FRAGMENT_SHADER.HIGH_INT.rangeMax": 30,
            "FRAGMENT_SHADER.HIGH_INT.rangeMin": 31,
            "MAX_DRAW_BUFFERS_WEBGL": 8,
        }
        webglFt = {
            "ALIASED_POINT_SIZE_RANGE": [
                1,
                1024
            ],
            "ALIASED_LINE_WIDTH_RANGE": [
                1,
                1
            ],
            "STENCIL_VALUE_MASK": 2147483647,
            "STENCIL_WRITEMASK": 2147483647,
            "STENCIL_BACK_VALUE_MASK": 2147483647,
            "STENCIL_BACK_WRITEMASK": 2147483647,
            "MAX_TEXTURE_SIZE": 16384,
            "MAX_VIEWPORT_DIMS": [
                32767,
                32767
            ],
            "SUBPIXEL_BITS": 4,
            "MAX_VERTEX_ATTRIBS": 16,
            "MAX_VERTEX_UNIFORM_VECTORS": 4096,
            "MAX_VARYING_VECTORS": 30,
            "MAX_COMBINED_TEXTURE_IMAGE_UNITS": 32,
            "MAX_VERTEX_TEXTURE_IMAGE_UNITS": 16,
            "MAX_TEXTURE_IMAGE_UNITS": 16,
            "MAX_FRAGMENT_UNIFORM_VECTORS": 1024,
            "SHADING_LANGUAGE_VERSION": "WebGL GLSL ES 3.00 (OpenGL ES GLSL ES 3.0 Chromium)",
            "VENDOR": "WebKit",
            "RENDERER": "WebKit WebGL",
            "VERSION": "WebGL 2.0 (OpenGL ES 3.0 Chromium)",
            "MAX_CUBE_MAP_TEXTURE_SIZE": 16384,
            "MAX_RENDERBUFFER_SIZE": 16384,
            "UNMASKED_VENDOR_WEBGL": "Google Inc. (Intel)",
            "UNMASKED_RENDERER_WEBGL": "ANGLE (Intel, Intel(R) Iris(R) Xe Graphics (0x0000A7A0) Direct3D11 vs_5_0 ps_5_0, D3D11)",
            "MAX_3D_TEXTURE_SIZE": 2048,
            "MAX_ELEMENTS_VERTICES": 2147483647,
            "MAX_ELEMENTS_INDICES": 2147483647,
            "MAX_TEXTURE_LOD_BIAS": 2,
            "MAX_DRAW_BUFFERS": 8,
            "MAX_FRAGMENT_UNIFORM_COMPONENTS": 4096,
            "MAX_VERTEX_UNIFORM_COMPONENTS": 16384,
            "MAX_ARRAY_TEXTURE_LAYERS": 2048,
            "MAX_PROGRAM_TEXEL_OFFSET": 7,
            "MAX_VARYING_COMPONENTS": 120,
            "MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS": 4,
            "MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS": 120,
            "MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS": 4,
            "MAX_COLOR_ATTACHMENTS": 8,
            "MAX_SAMPLES": 16,
            "MAX_VERTEX_UNIFORM_BLOCKS": 12,
            "MAX_FRAGMENT_UNIFORM_BLOCKS": 12,
            "MAX_COMBINED_UNIFORM_BLOCKS": 24,
            "MAX_UNIFORM_BUFFER_BINDINGS": 24,
            "MAX_UNIFORM_BLOCK_SIZE": 65536,
            "MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS": 212992,
            "MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS": 200704,
            "MAX_VERTEX_OUTPUT_COMPONENTS": 120,
            "MAX_FRAGMENT_INPUT_COMPONENTS": 120,
            "MAX_SERVER_WAIT_TIMEOUT": 0,
            "MAX_ELEMENT_INDEX": 4294967294,
            "MAX_CLIENT_WAIT_TIMEOUT_WEBGL": 0,
            "antialias": True,
            "MAX_TEXTURE_MAX_ANISOTROPY_EXT": 16,
            "VERTEX_SHADER.LOW_FLOAT.precision": 23,
            "VERTEX_SHADER.LOW_FLOAT.rangeMax": 127,
            "VERTEX_SHADER.LOW_FLOAT.rangeMin": 127,
            "VERTEX_SHADER.MEDIUM_FLOAT.precision": 23,
            "VERTEX_SHADER.MEDIUM_FLOAT.rangeMax": 127,
            "VERTEX_SHADER.MEDIUM_FLOAT.rangeMin": 127,
            "VERTEX_SHADER.HIGH_FLOAT.precision": 23,
            "VERTEX_SHADER.HIGH_FLOAT.rangeMax": 127,
            "VERTEX_SHADER.HIGH_FLOAT.rangeMin": 127,
            "VERTEX_SHADER.HIGH_INT.precision": 0,
            "VERTEX_SHADER.HIGH_INT.rangeMax": 30,
            "VERTEX_SHADER.HIGH_INT.rangeMin": 31,
            "FRAGMENT_SHADER.LOW_FLOAT.precision": 23,
            "FRAGMENT_SHADER.LOW_FLOAT.rangeMax": 127,
            "FRAGMENT_SHADER.LOW_FLOAT.rangeMin": 127,
            "FRAGMENT_SHADER.MEDIUM_FLOAT.precision": 23,
            "FRAGMENT_SHADER.MEDIUM_FLOAT.rangeMax": 127,
            "FRAGMENT_SHADER.MEDIUM_FLOAT.rangeMin": 127,
            "FRAGMENT_SHADER.HIGH_FLOAT.precision": 23,
            "FRAGMENT_SHADER.HIGH_FLOAT.rangeMax": 127,
            "FRAGMENT_SHADER.HIGH_FLOAT.rangeMin": 127,
            "FRAGMENT_SHADER.HIGH_INT.precision": 0,
            "FRAGMENT_SHADER.HIGH_INT.rangeMax": 30,
            "FRAGMENT_SHADER.HIGH_INT.rangeMin": 31,
            "MAX_DRAW_BUFFERS_WEBGL": 8
        }
        return webglFt

    def get_extension_imgs(self, text):
        imgs = re.findall('"(https.*?)"', text)

        extensionImgs = set()
        for img in imgs:
            img = img.replace("\\u002F", "/")
            if "apple.com/us/app/id1641486558" in img:
                img += "?rps=10005&r_pid=0"
            elif "play.google.com/store/apps/details" in img:
                img += "rps=10005&r_pid=0"
            elif "aimg.kwcdn.com" in img:
                pass
            elif "temu.com" in img:
                continue
            elif "static" in img:
                continue
            extensionImgs.add(img)
        return list(extensionImgs)

    def get_languages(self):
        languages = [
            "af",
            "af-ZA",
            "ar",
            "ar-AE",
            "ar-BH",
            "ar-DZ",
            "ar-EG",
            "ar-IQ",
            "ar-JO",
            "ar-KW",
            "ar-LB",
            "ar-LY",
            "ar-MA",
            "ar-OM",
            "ar-QA",
            "ar-SA",
            "ar-SY",
            "ar-TN",
            "ar-YE",
            "az",
            "az-AZ",
            "az-AZ",
            "be",
            "be-BY",
            "bg",
            "bg-BG",
            "bs-BA",
            "ca",
            "ca-ES",
            "cs",
            "cs-CZ",
            "cy",
            "cy-GB",
            "da",
            "da-DK",
            "de",
            "de-AT",
            "de-CH",
            "de-DE",
            "de-LI",
            "de-LU",
            "dv",
            "dv-MV",
            "el",
            "el-GR",
            "en",
            "en-AU",
            "en-BZ",
            "en-CA",
            "en-CB",
            "en-GB",
            "en-IE",
            "en-JM",
            "en-NZ",
            "en-PH",
            "en-TT",
            "en-US",
            "en-ZA",
            "en-ZW",
            "eo",
            "es",
            "es-AR",
            "es-BO",
            "es-CL",
            "es-CO",
            "es-CR",
            "es-DO",
            "es-EC",
            "es-ES",
            "es-ES",
            "es-GT",
            "es-HN",
            "es-MX",
            "es-NI",
            "es-PA",
            "es-PE",
            "es-PR",
            "es-PY",
            "es-SV",
            "es-UY",
            "es-VE",
            "et",
            "et-EE",
            "eu",
            "eu-ES",
            "fa",
            "fa-IR",
            "fi",
            "fi-FI",
            "fo",
            "fo-FO",
            "fr",
            "fr-BE",
            "fr-CA",
            "fr-CH",
            "fr-FR",
            "fr-LU",
            "fr-MC",
            "gl",
            "gl-ES",
            "gu",
            "gu-IN",
            "he",
            "he-IL",
            "hi",
            "hi-IN",
            "hr",
            "hr-BA",
            "hr-HR",
            "hu",
            "hu-HU",
            "hy",
            "hy-AM",
            "id",
            "id-ID",
            "is",
            "is-IS",
            "it",
            "it-CH",
            "it-IT",
            "ja",
            "ja-JP",
            "ka",
            "ka-GE",
            "kk",
            "kk-KZ",
            "kn",
            "kn-IN",
            "ko",
            "ko-KR",
            "kok",
            "kok-IN",
            "ky",
            "ky-KG",
            "lt",
            "lt-LT",
            "lv",
            "lv-LV",
            "mi",
            "mi-NZ",
            "mk",
            "mk-MK",
            "mn",
            "mn-MN",
            "mr",
            "mr-IN",
            "ms",
            "ms-BN",
            "ms-MY",
            "mt",
            "mt-MT",
            "nb",
            "nb-NO",
            "nl",
            "nl-BE",
            "nl-NL",
            "nn-NO",
            "ns",
            "ns-ZA",
            "pa",
            "pa-IN",
            "pl",
            "pl-PL",
            "pt",
            "pt-BR",
            "pt-PT",
            "qu",
            "qu-BO",
            "qu-EC",
            "qu-PE",
            "ro",
            "ro-RO",
            "ru",
            "ru-RU",
            "sa",
            "sa-IN",
            "se",
            "se-FI",
            "se-FI",
            "se-FI",
            "se-NO",
            "se-NO",
            "se-NO",
            "se-SE",
            "se-SE",
            "se-SE",
            "sk",
            "sk-SK",
            "sl",
            "sl-SI",
            "sq",
            "sq-AL",
            "sr-BA",
            "sr-BA",
            "sr-SP",
            "sr-SP",
            "sv",
            "sv-FI",
            "sv-SE",
            "sw",
            "sw-KE",
            "syr",
            "syr-SY",
            "ta",
            "ta-IN",
            "te",
            "te-IN",
            "th",
            "th-TH",
            "tl",
            "tl-PH",
            "tn",
            "tn-ZA",
            "tr",
            "tr-TR",
            "ts",
            "tt",
            "tt-RU",
            "uk",
            "uk-UA",
            "ur",
            "ur-PK",
            "uz",
            "uz-UZ",
            "uz-UZ",
            "vi",
            "vi-VN",
            "xh",
            "xh-ZA",
            "zh",
            "zh-CN",
            "zh-HK",
            "zh-MO",
            "zh-SG",
            "zh-TW",
            "zu",
            "zu-ZA",
        ]

        return random.choices(languages, k=1)

    def get_performanceTime(self):
        d = 0.09999999 + random.random() / 100000000
        d2 = 0.10000000 + random.random() / 100000000
        return [0.09999999403953552,0.10000002384185791]
        # return [0.09999999403953552,0.10000002384185791]
        # return [0.09999996423721313,0.10000002384185791]

    def get_h5features(self):
        return {
            "audioTypes": {
                "audio.ogg": "probably",
                "audio.mp3": "probably",
                "audio.opus": "probably",
                "audio.wav": "probably",
                "audio.m4a": "maybe",
            },
            "audioLoop": True,
            "history": True,
            "synthesis": True,
            "videoTypes": {
                "video.h264": "probably",
                "video.webm": "probably",
                "video.vp9": "probably",
            },
            "videoCrossOrigin": True,
            "videoLoop": True,
            "videoPreload": True,
            "inputCapture": False,
            "inputFile": True,
            "inputFormEnctype": True,
            "shadowroot": True,
            "geolocation": True,
            "download": True,
            "crossOrigin": True,
            "scriptDefer": True,
            "webCryptography": True,
        }

    def get_rawData(self):
        return {
            "ua": self.ua,
            "touchSupport": [1, False, False],
            "osCpu": "",
            "language": self.languages[0],
            "colorDepth": 24,
            "deviceMemory": self.deviceMemory,
            "screenResolution": self.screen,
            "availableScreenResolution": self.availableScreenResolution,
            "hardwareConcurrency": self.hardwareConcurrency,
            "timezoneOffset": -480,
            "timezone": "Asia/Shanghai",
            "cpuClass": "not available",
            "platform": "Win32",
            "cookiesEnabled": True,
            "webdriver": "not available",
            "addBehavior": False,
            "plugins": [
                [
                    "Chrome%20PDF%20Viewer",
                    "Portable%20Document%20Format",
                    [
                        {"type": "application%2Fpdf", "suffixes": "pdf"},
                        {"type": "text%2Fpdf", "suffixes": "pdf"},
                    ],
                ],
                [
                    "Chromium%20PDF%20Viewer",
                    "Portable%20Document%20Format",
                    [
                        {"type": "application%2Fpdf", "suffixes": "pdf"},
                        {"type": "text%2Fpdf", "suffixes": "pdf"},
                    ],
                ],
                [
                    "Microsoft%20Edge%20PDF%20Viewer",
                    "Portable%20Document%20Format",
                    [
                        {"type": "application%2Fpdf", "suffixes": "pdf"},
                        {"type": "text%2Fpdf", "suffixes": "pdf"},
                    ],
                ],
                [
                    "PDF%20Viewer",
                    "Portable%20Document%20Format",
                    [
                        {"type": "application%2Fpdf", "suffixes": "pdf"},
                        {"type": "text%2Fpdf", "suffixes": "pdf"},
                    ],
                ],
                [
                    "WebKit%20built-in%20PDF",
                    "Portable%20Document%20Format",
                    [
                        {"type": "application%2Fpdf", "suffixes": "pdf"},
                        {"type": "text%2Fpdf", "suffixes": "pdf"},
                    ],
                ],
            ],
            "sessionStorage": True,
            "localStorage": True,
            "indexedDb": True,
            "openDatabase": False,
            "vendor": "Google Inc.",
            "windowAllSize": {
                "h": [
                    self.availableScreenResolution[1] - self.h,
                    self.availableScreenResolution[1],
                ],
                "w": [
                    self.availableScreenResolution[0],
                    self.availableScreenResolution[0],
                ],
                "dh": self.h,
                "dw": 0,
            },
        }

    def get_a4(self, device):
        import requests
        res = requests.post(
            "http://127.0.0.1:8980/device", json={"device": device}
        )
        return res.json()

    async def a4(self):
        clientX = random.randint(800,900)
        clientY = random.randint(300,400)
        self.clickData = [
            {
                "clientX": clientX,
                "clientY": clientY,
                "timestamp": int(time.time()*1000)
            }
        ]
        for i in range(6):
            await asyncio.sleep(random.randint(15, 40) / 1000)
            clientX += random.randint(-10, 10)
            clientY += random.randint(-10, 10)
            self.moveData.append({
                "clientX": clientX,
                "clientY": clientY,
                "force": -1,
                "timestamp": int(time.time()*1000)
            })

        device = {
    "moveData": self.moveData,
    "clickData": self.clickData,
    "inputData": [],
    "blurData": [],
    "pasteData": "0",
    "headerCache": {
        "a": null,
        "b": self.headerCache,
        "c": null,
        "d": null,
        "e": null,
        "f": null,
        "g": null
    },
    "uid": "",
    "FKGJ": self.FKGJ,
    "rawData": {
        "ua": self.ua,
        "touchSupport": [
            1,
            false,
            false
        ],
        "osCpu": "",
        "language": "zh-CN",
        "colorDepth": 24,
        "deviceMemory": random.choice([8, 16, 32]),
        "screenResolution": self.screen,
        "windowSize": json.dumps(
            self.availableScreenResolution, separators=(",", ":")
        ),
        "hardwareConcurrency": random.choice([8, 16, 20, 32]),
        "timezoneOffset": -480,
        "timezone": "Asia/Shanghai",
        "cpuClass": "not available",
        "platform": "Win32",
        "cookiesEnabled": true,
        "webdriver": "not available",
        "addBehavior": false,
        "plugins": [
            [
                "Chrome%20PDF%20Viewer",
                "Portable%20Document%20Format",
                [
                    {
                        "type": "application%2Fpdf",
                        "suffixes": "pdf"
                    },
                    {
                        "type": "text%2Fpdf",
                        "suffixes": "pdf"
                    }
                ]
            ],
            [
                "Chromium%20PDF%20Viewer",
                "Portable%20Document%20Format",
                [
                    {
                        "type": "application%2Fpdf",
                        "suffixes": "pdf"
                    },
                    {
                        "type": "text%2Fpdf",
                        "suffixes": "pdf"
                    }
                ]
            ],
            [
                "Microsoft%20Edge%20PDF%20Viewer",
                "Portable%20Document%20Format",
                [
                    {
                        "type": "application%2Fpdf",
                        "suffixes": "pdf"
                    },
                    {
                        "type": "text%2Fpdf",
                        "suffixes": "pdf"
                    }
                ]
            ],
            [
                "PDF%20Viewer",
                "Portable%20Document%20Format",
                [
                    {
                        "type": "application%2Fpdf",
                        "suffixes": "pdf"
                    },
                    {
                        "type": "text%2Fpdf",
                        "suffixes": "pdf"
                    }
                ]
            ],
            [
                "WebKit%20built-in%20PDF",
                "Portable%20Document%20Format",
                [
                    {
                        "type": "application%2Fpdf",
                        "suffixes": "pdf"
                    },
                    {
                        "type": "text%2Fpdf",
                        "suffixes": "pdf"
                    }
                ]
            ]
        ],
        "sessionStorage": true,
        "localStorage": true,
        "indexedDb": true,
        "openDatabase": false,
        "vendor": "Google Inc.",
        "windowAllSize": {
            "h": [
                self.availableScreenResolution[1] - self.h,
                self.availableScreenResolution[1],
            ],
            "w": [
                self.availableScreenResolution[0],
                self.availableScreenResolution[0],
            ],
            "dh": self.h,
            "dw": 0,
        }
    },
    "hasSensor": "{\"gyroFlag\":false,\"acceFlag\":false}",
    "isFront": "true",
    "webGLInfos": "[\"Google Inc. (Intel)\",\"ANGLE (Intel, Intel(R) Iris(R) Xe Graphics (0x0000A7A0) Direct3D11 vs_5_0 ps_5_0, D3D11)\",\"WebKit\",\"WebKit WebGL\",\"WebGL 1.0 (OpenGL ES 2.0 Chromium)\"]",
    "windowSize": json.dumps(
        self.availableScreenResolution, separators=(",", ":")
    ),
    "winSelenium": "false",
    "chromium": "false",
    "headlessByProperties": "true",
    "languages": json.dumps(self.languages, separators=(",", ":")),
    "consoleLied": "false",
    "chromeExtensionScripts": "[]",
    "extensionImgs": json.dumps(
        self.get_extension_imgs(''), separators=(",", ":")
    ),
    "hookFuncs": "[\"Function.toString\"]",
    "frontReferer": self.headers.get("referer") or self.headers.get("Referer"),
    "cssFeatures": "1288296882",
    "webglFt": json.dumps(self.get_webgl_f_t(), separators=(",", ":")),
    "performanceTime": "[0.09999996423721313,0.10000002384185791]",
    "emptyEvalLength": "33",
    "errorFF": "false",
    "h5Features": "{\"audioTypes\":{\"audio.ogg\":\"probably\",\"audio.mp3\":\"probably\",\"audio.opus\":\"probably\",\"audio.wav\":\"probably\",\"audio.m4a\":\"maybe\"},\"audioLoop\":true,\"history\":true,\"synthesis\":true,\"videoTypes\":{\"video.h264\":\"probably\",\"video.webm\":\"probably\",\"video.vp9\":\"probably\"},\"videoCrossOrigin\":true,\"videoLoop\":true,\"videoPreload\":true,\"inputCapture\":false,\"inputFile\":true,\"inputFormEnctype\":true,\"shadowroot\":true,\"geolocation\":true,\"download\":true,\"crossOrigin\":true,\"scriptDefer\":true,\"webCryptography\":true}",
    "fonts": self.fonts,
    "localIp": "9:64:69:87:82:92:28:27",
    # "localIp": "0.0.0.0",
    "localIpDuration": random.randint(120, 160),
    "elements": {
        "sels": {
            "matchedKeys": []
        }
    },
    "outterJs": "{\"urls\":[\"https://www.googletagmanager.com/gtm.js?id=GTM-NSR6SG3\",\"https://static.kwcdn.com/m-assets/assets/js/react_webpack_runtime_5ef7c30b5b407807d2ce.js\",\"https://static.kwcdn.com/m-assets/assets/js/biz_vendors_b95ea31e26da6aaaa82a.js\",\"https://static.kwcdn.com/m-assets/assets/js/vendors_fd120b67b137f521041d.js\",\"https://static.kwcdn.com/m-assets/assets/js/8637_d97da129267753c7b52d.js\",\"https://static.kwcdn.com/m-assets/assets/js/5656_0c2c9777131ead192a0f.js\",\"https://static.kwcdn.com/m-assets/assets/js/3089_d645bdae681828bf22b9.js\",\"https://static.kwcdn.com/m-assets/assets/js/7719_b64ad3001400733dd416.js\",\"https://static.kwcdn.com/m-assets/assets/js/mall_454fd3f9a0f43e4d5128.js\"],\"words\":[\"AccessToken\",\"querySelector\",\"querySelector\",\"getElementsByTagName\",\"querySelector\",\"querySelectorAll\",\"querySelector\",\"querySelectorAll\",\"getElementsByTagName\",\"querySelector\",\"querySelectorAll\",\"querySelector\",\"querySelectorAll\",\"querySelector\",\"querySelector\",\"querySelectorAll\"]}"
}
        res = await get_a4(device)


        sign = hashlib.sha1(
            "fe".encode()
            + "HJ6793TJDI86DLS9D".encode()
            + res["data"]["timeStamp"].encode()
            + res["data"]["result"].encode()
        ).hexdigest()
        data = {
            "appKey": "fe",
            "data": res["data"]["result"],
            "sign": sign,
            "timestamp": res["data"]["timeStamp"],
        }
        return data


if __name__ == "__main__":
    a = DeviceGeneration(headers=   {
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'upgrade-insecure-requests': '1',
            'cookie': 'region=211; language=en; currency=USD; timezone=Asia%2FShanghai; webp=1',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'service-worker-navigation-preload': '2',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'sec-fetch-dest': 'document',
            'accept-language': 'zh-CN,zh;q=0.9',
            'priority': 'u=0, i',
        },)
    d = asyncio.run(a.a4())
    print(d)
    print(json.dumps(d, indent=2))
