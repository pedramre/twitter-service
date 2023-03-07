from app import redisConnection
import pickle
import json

class RedisService:
    def get_by_redis(self,key):
        print('key',key)
        data = redisConnection.get(key)
        if data:
            data = json.loads(data)
        return data

    def store_in_redis(self,key,data):
        data = json.dumps(data)
        return redisConnection.set(key,data) 