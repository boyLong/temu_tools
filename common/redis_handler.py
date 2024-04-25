from common.config import redis_config, cookie_key, cookie_len
import json
from redis import asyncio as aioredis
import redis

class RedisHandler(object):

    def __init__(self,):

        self.pool = aioredis.ConnectionPool(host=redis_config["REDIS_HOST"],
                                             port=redis_config["REDIS_PORT"],
                                             db=redis_config["REDIS_DB"],
                                             password=redis_config["REDIS_PASSWORD"])
        self.conn = aioredis.StrictRedis(connection_pool=self.pool)

    async def push(self, key, value):
        if isinstance(value, dict):
            value = json.dumps(value)
        await self.conn.lpush(key, value)

    async def add(self,key, value):
        if isinstance(value, dict):
            value = json.dumps(value)
        await self.conn.lpush(key, value)

    async def len(self, key):
        return await self.conn.llen(key)


class RedisHandlerSync(object):

    def __init__(self, ):

        self.pool = redis.ConnectionPool(host=redis_config["REDIS_HOST"],
                                            port=redis_config["REDIS_PORT"],
                                            db=redis_config["REDIS_DB"],
                                            password=redis_config["REDIS_PASSWORD"])
        self.conn = redis.StrictRedis(connection_pool=self.pool)

    def push(self, key, value):
        if isinstance(value, dict):
            value = json.dumps(value)
        self.conn.lpush(key, value)

    def add(self, key, value):
        if isinstance(value, dict):
            value = json.dumps(value)
        self.conn.lpush(key, value)

    def len(self, key):
        return self.conn.llen(key)


redis_Handler = RedisHandler()

redis_handler_sync = RedisHandlerSync()


if __name__ == '__main__':
    redis = RedisHandler()
    # await redis.push("test", {"name": "zhangsan"})
