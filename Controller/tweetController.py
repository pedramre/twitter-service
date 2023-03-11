from flask import jsonify
from Model.tweetScraper import TweetScraper
from Service.twitterService import TwitterService
import snscrape.modules.twitter as sntwitter

class TweetController:
    def __init__(self, scraper):
        self.scraper = scraper
        self.twitterService = TwitterService()
    
    def get_users_tweets(self, users, date):
        try:
            tweets = {}
            for user in users:
                tweets[user] = self.scraper.get_tweets(user,date)
            return jsonify({'status':'success','message':"users tweets fetched successfully",'data':tweets})
        except:
            return jsonify({'status':'faild','message':"error, something is wrong",'data':[]})

    def get_user_tweets(self, user, date):
        try:
            tweets = self.scraper.get_tweets(user,date)
            return jsonify({'status':'success','message':"user tweets fetched successfully",'data':tweets})
        except:
            return jsonify({'status':'faild','message':"error, something is wrong",'data':[]})

    def get_audiences(self,user,date):
        try:
            audiences = self.scraper.get_account_audiences(user,date)
            audiences_list = []
            [audiences_list.append(audience['username']) for audience in audiences]
            active_audiences = self.scraper.get_account_active_audiences(audiences_list)
            
            return jsonify({'status':'success','message':"user audiences fetched successfully",'data':{'audiences':audiences,'active_audiences':active_audiences}})
        except:
            return jsonify({'status':'faild','message':"error, something is wrong",'data':[]})

    def get_sentiment(self,user,thread):
        try:
            tweets = []
            tweets = self.scraper.get_thread(user,thread)
            return jsonify({'status':'success','message':"user sentiments fetched successfully",'data':tweets})
        except:
            return jsonify({'status':'faild','message':"error, something is wrong",'data':[]})