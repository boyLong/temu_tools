import temu_pb2
import struct
import time
import random
import websocket
from urllib import parse
from common.encrypt_tools import cookie_to_str

def getSync():
    sync = temu_pb2.Sync()
    sync.syncAll = True

    s = temu_pb2.TitanUpstream()
    s.appId = 10001
    s.command = 'titan.sync'
    s.protocol = 1
    s.compress = 0
    s.host = 'www.temu.com'
    s.upstreamSeq = 102
    s.body = sync.SerializeToString()
    return s.SerializeToString()


def F(e=None):
    e = e or 21
    chars = "bjectSymhasOwnProp-0123456789ABCDEFGHIJKLMNQRTUVWXYZ_dfgiklquvxz"
    t = ''.join(random.choice(chars) for _ in range(e))
    return t


def s(*args):
    device_id = "{}{}_{}".format(args[0] if args else "", int(time.time()*1000), F())
    return device_id


def get_payload(titanid, ua):
    t = temu_pb2.appInfo()
    t.titanid = titanid.encode()
    t.ua = ua.encode()
    t.os = 5

    t.repackage = False
    t.accesstoken = ''
    # t.customPayload = None
    t.authType = 0
    t.sceneType = 0

    c = temu_pb2.TitanSessionRequest()
    c.encryptedAppInfo = t.SerializeToString()
    c.requestType = 4
    c.protocolVersion = 1
    c.isPushConn = True


    s = temu_pb2.TitanUpstream()
    s.appId = 10001
    s.command = "titan.session"
    s.protocol = 1
    s.compress = 0
    s.host = 'www.temu.com'
    s.upstreamSeq = 101
    s.conId = 0
    s.sessionResumptionReq = c.SerializeToString()
    return s.SerializeToString()


class TemuWs:
    def __init__(self, ua, Cookie, proxy ):
        self.ws = None
        self.ua = ua
        self.device_id = s()
        self.ctx = 100
        if isinstance(Cookie, dict):
            self.Cookie = cookie_to_str(Cookie)
        else:
            self.Cookie = Cookie
        parsed_proxy = parse.urlparse(proxy)
        username = parsed_proxy.username
        password = parsed_proxy.password
        self.http_proxy_host = parsed_proxy.hostname
        self.http_proxy_port = parsed_proxy.port
        self.http_proxy_auth = (username, password)

    def parse_array_buffer(self, data):

        u = memoryview(data)
        magic, cmd, ctx, reserve = struct.unpack_from('!hhii', u, 0)
        a = struct.unpack_from('!i', u, 12)[0]

        payload = bytes(u[16:16 + a]) if a > 0 else b''

        return {
            'magic': magic,
            'cmd': cmd,
            'ctx': ctx,
            'reserve': reserve,
            'payload': payload
        }

    def create_array_buffer(self,payload):
        self.ctx += 1
        e = {
            "magic": 10, "cmd": 102, "ctx": self.ctx, "reserve": 1,
            "payload": payload,
         }

        magic = e['magic']
        cmd = e['cmd']
        ctx = e['ctx']
        reserve = e['reserve']
        payload = e['payload'] if 'payload' in e else None

        a = len(payload) if payload else 0
        c = bytearray(16 + a)
        u = memoryview(c)

        struct.pack_into('!hhii', u, 0, magic, cmd, ctx, reserve)
        struct.pack_into('!i', u, 12, a)

        if payload:
            u[16:16 + a] = payload

        return bytes(c)


    def on_message(self, ws, message):
        message = self.parse_array_buffer(message)

        print(message)
        TitanDownstream = temu_pb2.TitanDownstream()
        if self.ctx < 103:
            payload = TitanDownstream.FromString(message['payload'])
            print(payload)

            payload = getSync()
            message = self.create_array_buffer(payload)

            ws.send(message)
        else:
            self.ws.close()

    def on_open(self, ws):
        # Assuming get_payload and create_array_buffer are defined somewhere
        payload = get_payload(self.device_id, self.ua)
        message = self.create_array_buffer(payload)
        self.ws.send(message)
        print("Connected to WebSocket server.")

    def on_close(self, ws, *args):
        print("WebSocket connection closed.", args)

    def connect(self):
        self.ws = websocket.WebSocketApp(
            'wss://www.temu.com/?ws-titan-request-sign=dee0ea73',
            on_open=self.on_open,
            on_message=self.on_message,
            on_close=self.on_close,

            header={
                'Pragma': 'no-cache',
                'Origin': 'https://www.temu.com',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'User-Agent': self.ua,
                'Upgrade': 'websocket',
                'Cache-Control': 'no-cache',
                'Connection': 'Upgrade',
                'Sec-WebSocket-Version': '13',
                'Sec-WebSocket-Extensions': 'permessage-deflate; client_max_window_bits',
                "Cookie": self.Cookie,
            },
        )

        self.ws.run_forever(
                            ping_interval=10,
                            ping_timeout=1,
                            http_proxy_host=self.http_proxy_host,
                            http_proxy_port=self.http_proxy_port,
                            http_proxy_auth=self.http_proxy_auth,
                            proxy_type="http",
                            http_proxy_timeout=1
                        )


def main():
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    Cookie = ('region=211; language=zh-Hans; currency=USD; api_uid=Cm1sL2aNAIM5FwBVPDh6Ag==; timezone=Asia%2FShanghai; '
              'webp=1; _nano_fp=XpmxX0dan5mYXpTaXT_wW~LH6OOk_HYS45ktP8wQ; _bee=4FgJTgHmRC3wqsfGGpl1l3ZyXGR3Eap7;'
              ' njrpl=4FgJTgHmRC3wqsfGGpl1l3ZyXGR3Eap7; dilx=IaQZbo0mp0AnJ9_26SaPz; hfsc=L3yIeIwx7zn80ZTLfg==;'
              ' _ttc=3.E3GdMbwIUZ5g.1752052743; '
              '_device_tag=CgI2WRIIWG9MU3RkbnkaMGvXC3o2KGAuz4g3W3D1wi6iYO1pbJ+szBE8tXhRLn2fk64ZYogVSw6JgFF0lRzKnjAC; '
              'user_uin=BB7X3HBND5O37PCNNK2VENVLCF7RNO5SQBE3EAXD; _u_pa=%7B%22nrpt_211%22%3A0%7D;'
              ' AccessToken=FCBEU5NN6J5MH3ET22LJVHM7CQ6H4HFE3EQR32GEWSUEZ6ALJZWA0110d394299c; isLogin=1721614811952')
    client = TemuWs(ua,Cookie,proxy="http://baobao123-zone-custom-region-sg-session-a9c8fy9m43-sessTime-5:bao123456@47.236.40.83:8088")
    client.connect()


if __name__ == "__main__":
    main()
