import secrets
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
    chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    s =  "".join(secrets.choice(chars) for _ in range(10))
    proxy = f'http://baobao123-zone-custom-region-sg-session-{s}-sessTime-5:bao123456@47.236.40.83:8088'

    # proxy = f'http://127.0.0.1:7890'
    return {"http": proxy, "https": proxy}