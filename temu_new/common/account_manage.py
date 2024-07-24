# from common.redis_handler import redis_client
import asyncio
from common.logger import logger
from common.encrypt_tools import get_random
from tenacity import retry, stop_after_attempt, wait_fixed
from common.encrypt_tools import client_tools
import random


async def get_account_info():
    # username = f"{get_random(random.randint(10, 20))}@gmail.com"
    # password = 'temu_shop_123'

    return "music_lover@burning.icu---Bm5zPq1S".split("---")
    return username, password


def before_log(stats):
    logger.info(f"正在获取验证码..请稍后...第{stats.attempt_number}次查询")


if __name__ == '__main__':

    asyncio.run(get_email_code())