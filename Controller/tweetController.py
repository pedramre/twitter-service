from flask import jsonify
from Model.tweetScraper import TweetScraper
from Service.twitterService import TwitterService
import snscrape.modules.twitter as sntwitter
import collections

class TweetController:
    def __init__(self, scraper):
        self.scraper = scraper
        self.twitterService = TwitterService()
    
    def get_tweets(self, user, date):
        tweets = self.scraper.get_tweets(user,date)
        return jsonify(tweets)

    def get_audiences(self,user,date):
        tweets = self.scraper.get_tweets(user,date)
        for tweet in tweets:
            tweet_id = tweet['id']
            replies=self.scraper.get_replies(user,tweet_id)
            
        counter = collections.Counter(replies)
        return jsonify(replies,counter)

    def get_sentiment(self,thread):
        tweets = []
        tweets = self.scraper.get_thread(thread)
        return jsonify(tweets)