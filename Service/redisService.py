from app import redisConnection
import pickle
import json

class RedisService:
    """A Class to deal with redis """

    def get(self,key):
        """Function to get from redis
            Parameters
            ----------
            key : str, require
        """
        data = redisConnection.get(key)
        return data

    def store(self,key,data):
        """Function to save in redis
            Parameters
            ----------
            key : str, require
            data : str, require
        """
        redisConnection.set(key, data)
        return True
    
    def check(self,key):
        """Function to check a key in redis
            Parameters
            ----------
            key : str, require
        """
        return redisConnection.exists(key)
    
    def get_keys(self,pattern):
        """Function to all of keys from redis
            Parameters
            ----------
            pattern : str, require
        """
        final_keys = []
        keys = redisConnection.keys(pattern)
        [final_keys.append(key.decode()) for key in keys]
        return final_keys
    
    def delete(self,pattern):
        """Function to remove from redis
            Parameters
            ----------
            pattern : str, require
        """
        return redisConnection.delete(*pattern)
    
    def get_last_replies(self,last_key):
        """Function to get last key from redis and return json type
            Parameters
            ----------
            last_key : str, require
        """
        last_replies = self.get(last_key)
        return json.loads(last_replies)
