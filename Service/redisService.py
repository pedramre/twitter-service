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
    
    def get_keys(self,pattern):
        final_keys = []
        keys = redisConnection.keys(pattern)
        [final_keys.append(key.decode()) for key in keys]
        return final_keys
    
    def delete(self,pattern):
        return redisConnection.delete(*pattern)
    
    def get_last_replies(self,last_key):
        last_replies = self.get(last_key)
        return json.loads(last_replies)
