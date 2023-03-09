import snscrape.modules.twitter as sntwitter
import redis
from Service.redisService import RedisService

class TwitterService:
    def __init__(self) -> None:
        self.redisService = RedisService()
    def search_tweets(self, query):
        return sntwitter.TwitterSearchScraper(query).get_items()
    
    def get_tweets(self,tweet_id):
        return sntwitter.TwitterTweetScraper(tweet_id).get_items()
    
