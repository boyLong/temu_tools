from common.encrypt_tools import get_random
import socket


def extract_ip():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        st.connect(('10.255.255.255', 1))
        IP = st.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        st.close()
    return IP


local_ip = extract_ip()


def get_proxy(l=None):

    if l is None:
        if local_ip.startswith("192.168"):
            l = 1
        elif local_ip.startswith("10"):
            l = 2
        elif local_ip.startswith("172"):
            l = 1
        else:
            l = 2
    if l == 1:
        user = f"user-databurning-sessid-{get_random(8)}-sesstime-20-keep-true"
        proxy = f'http://{user}:databurning@43.128.74.58:30111'
    elif l == 2:
        user = f"user-databurning-sessid-{get_random(8)}-sesstime-20-keep-true"
        proxy = f'http://{user}:databurning@pr.roxlabs.cn:4600'
    elif l == 3:
        proxy = f"http://127.0.0.1:8888"


    return proxy