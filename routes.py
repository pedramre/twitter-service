from __main__ import app
from Controller.tweetController import TweetController
from Model.tweetScraper import TweetScraper
from Service.twitterService import TwitterService
from flask import jsonify


# Define the Twitter user to track
users = ['alikarimi_ak8']
date = 'since:2023-02-27'
print('awdadad')
# Define an API route to get the tweets and replies from the user
@app.route('/tweets')
def get_tweets():
    scraper = TweetScraper(TwitterService())
    controller = TweetController(scraper)
    return controller.get_tweets(users[0], date)

@app.route('/audiences')
def get_audiences():
    scraper = TweetScraper(TwitterService())
    controller = TweetController(scraper)
    return controller.get_audiences(users[0], date)
    
    
    