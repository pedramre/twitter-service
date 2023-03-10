from app import redisConnection
import pickle
import json

class RedisService:
    def get(self,key):
        data = redisConnection.get(key)
        return data

    def store(self,key,data):
        redisConnection.set(key, data)
        return True
    
    def check(self,key):
        return redisConnection.exists(key)