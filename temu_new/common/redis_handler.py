import asyncio
import redis.asyncio as redis
from redis.exceptions import ConnectionError
from common.config import redis_config
from tenacity import retry, stop_after_attempt
import json


class RedisHandler(object):
    def __init__(self,host, port, db, password):
        self.host = host
        self.port = port
        self.db = db
        self.password = password
        self.__connect__()

    def __connect__(self):

        self.pool = redis.ConnectionPool(host=self.host,
                                         port=self.port,
                                         db=self.db,
                                         password=self.password)
        self.client = redis.Redis(connection_pool=self.pool)

    @retry(stop=stop_after_attempt(3))
    async def hget(self, name, key):
        try:
            value = await self.client.hget(name, key)
            return value
        except ConnectionError:
            await asyncio.sleep(1)
            self.__connect__()
            raise ConnectionError("ConnectionError")

    @retry(stop=stop_after_attempt(3))
    async def get(self, name):
        try:
            value = await self.client.get(name)
            return value
        except ConnectionError:
            await asyncio.sleep(1)
            self.__connect__()
            raise ConnectionError("ConnectionError")


    @retry(stop=stop_after_attempt(3))
    async def hset(self, name, key, value):
        try:
            res = await self.client.hset(name, key, value)
            return res
        except ConnectionError:
            await asyncio.sleep(1)
            self.__connect__()
            raise ConnectionError("ConnectionError")

    @retry(stop=stop_after_attempt(3))
    async def srandmember(self,key):
        try:
            value = await self.client.srandmember( key)
            return value
        except ConnectionError:
            await asyncio.sleep(1)
            self.__connect__()
            raise ConnectionError("ConnectionError")

    @retry(stop=stop_after_attempt(3))
    async def sadd(self,key, value):
        try:
            value = await self.client.sadd(key, value)
            return value
        except ConnectionError:
            await asyncio.sleep(1)
            self.__connect__()
            raise ConnectionError("ConnectionError")

    @retry(stop=stop_after_attempt(3))
    async def incr(self, key):
        try:
            value = await self.client.incr(key)
            return value
        except ConnectionError:
            await asyncio.sleep(1)
            self.__connect__()
            raise ConnectionError("ConnectionError")

    @retry(stop=stop_after_attempt(3))
    async def decr(self, key):
        try:
            value = await self.client.decr(key)
            return value
        except ConnectionError:
            await asyncio.sleep(1)
            self.__connect__()
            raise ConnectionError("ConnectionError")

    @retry(stop=stop_after_attempt(3))
    async def set(self, key, value):
        try:
            value = await self.client.set(key, value)
            return value
        except ConnectionError:
            await asyncio.sleep(1)
            self.__connect__()
            raise ConnectionError("ConnectionError")


redis_client = RedisHandler(redis_config["REDIS_HOST"],redis_config["REDIS_PORT"],redis_config["REDIS_DB"],redis_config["REDIS_PASSWORD"])


