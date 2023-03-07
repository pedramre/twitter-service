import snscrape.modules.twitter as sntwitter
import redis
from Service.redisService import RedisService

class TwitterService:
    def __init__(self) -> None:
        self.redisService = RedisService()
    def search_tweets(self, query):
        items = list(sntwitter.TwitterSearchScraper(query).get_items())
        return items
    
