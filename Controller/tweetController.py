from flask import jsonify
from Model.tweetScraper import TweetScraper
from Service.twitterService import TwitterService
import snscrape.modules.twitter as sntwitter

class TweetController:
    def __init__(self, scraper):
        self.scraper = scraper
        self.twitterService = TwitterService()
    
    def get_users_tweets(self, users, date):
        tweets = {}
        for user in users:
            tweets[user] = self.scraper.get_tweets(user,date)
        return jsonify(tweets)

    def get_user_tweets(self, user, date):
        tweets = self.scraper.get_tweets(user,date)
        return jsonify(tweets)

    def get_audiences(self,user,date):
        
        audiences = self.scraper.get_account_audiences(user,date)
        audiences_list = []
        [audiences_list.append(audience['username']) for audience in audiences]
        active_audiences = self.scraper.get_account_active_audiences(audiences_list)
        
        return jsonify({'audiences':audiences,'active_audiences':active_audiences})

    def get_sentiment(self,thread):
        tweets = []
        tweets = self.scraper.get_thread(thread)
        return jsonify(tweets)