import snscrape.modules.twitter as sntwitter
import redis
from Service.redisService import RedisService

class TwitterService:
    """A Class to handle queries """

    def __init__(self) -> None:
        self.redisService = RedisService()
    
    def search_tweets(self, query):
        """Function to search and get tweets by query string
            Parameters
            ----------
            query : str, require
        """
        return sntwitter.TwitterSearchScraper(query).get_items()
    
    def get_tweets(self,tweet_id):
        """Function to get tweets by tweet id
            Parameters
            ----------
            tweet_id : str, require
        """
        return sntwitter.TwitterTweetScraper(tweet_id).get_items()
    
