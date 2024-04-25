import json
import secrets
import asyncio
import time
import traceback

from TemuLogin import TemuLogin
from concurrent.futures import ThreadPoolExecutor
from common.encrypt_tools import get_random,get_nano,get_a4
from common.logger import logger
from common.redis_handler import redis_Handler,redis_handler_sync
pool = ThreadPoolExecutor(max_workers=10)

cookie_len = 30
async def uk_save_redis():
    k_len = await redis_Handler.len("uk_temu_cookie")
    if k_len > 30:
        return
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        'referer': "https://www.temu.com",
        'pragma': 'no-cache',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        "cookie": "timezone=Asia%2FShanghai; region=210; language=en; currency=GBP; webp=1"
    }
    user = f"user-databurning-sessid-{get_random(8)}-sesstime-20-keep-true"
    proxy = f'http://{user}:databurning@43.128.74.58:30111'
    tl = TemuLogin(headers=headers, proxy=proxy)
    try:
        res = await tl.start()
        if res:
            await redis_Handler.push("uk_temu_cookie", json.dumps(res))

    except Exception as e:
        import trace
        traceback.print_exc()
        logger.error(f"uk_save_redis error {e}")


async def us_save_redis():
    k_len = await redis_Handler.len("us_temu_cookie")
    if k_len > 30:
        return
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        'referer': "https://www.temu.com",
        'pragma': 'no-cache',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        "cookie": "timezone=Asia%2FShanghai; region=211; language=en; currency=USD; webp=1"
    }
    user = f"user-databurning-sessid-{get_random(8)}-sesstime-20-keep-true"
    proxy = f'http://{user}:databurning@43.128.74.58:30111'
    tl = TemuLogin(headers=headers, proxy=proxy)
    try:
        res = await tl.start()
        if res:
            await redis_Handler.push("us_temu_cookie", json.dumps(dict(res)))

    except Exception as e:
        import trace
        traceback.print_exc()
        logger.error(f"uk_save_redis error {e}")


def run(r):
    if r == "uk":
        loop = asyncio.new_event_loop()
        loop.run_until_complete(uk_save_redis())
    elif r== 'us':
        loop = asyncio.new_event_loop()
        loop.run_until_complete(us_save_redis())


def run_n():
    loop = asyncio.new_event_loop()
    loop.run_until_complete(get_a4({}))

if __name__ == '__main__':

    import time
    executor = ThreadPoolExecutor(4)

    while 1:
        if redis_handler_sync.len("us_temu_cookie") < 30:
            executor.submit(run, "us")

        # if redis_handler_sync.len("uk_temu_cookie") < 30:
        #     executor.submit(run, "uk")
        #
        # else:
        #     time.sleep(0.01)
        break
    executor.shutdown(wait=True)



