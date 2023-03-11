from __main__ import app
from Controller.tweetController import TweetController
from Model.tweetScraper import TweetScraper
from Service.twitterService import TwitterService


# Define the Twitter user to track
users = ['alikarimi_ak8','taylorlorenz','cathiedwood']
date = 'since:2023-03-10'

# sample thread link
# thread = 'https://twitter.com/GeorgePointon_/status/1629085362214543361'

# Define an API route to get the tweets and replies from the user
@app.route('/accounts')
def get_accounts():
    scraper = TweetScraper(TwitterService())
    controller = TweetController(scraper)
    return controller.get_users_tweets(users, date)

@app.route('/tweets/<user>')
def get_tweets(user):
    scraper = TweetScraper(TwitterService())
    controller = TweetController(scraper)
    return controller.get_user_tweets(user, date)

@app.route('/audiences/<user>')
def get_audiences(user):
    scraper = TweetScraper(TwitterService())
    controller = TweetController(scraper)
    return controller.get_audiences(user, date)

@app.route('/sentiment/<user>/<thread>')
def get_sentiment(user,thread):
    scraper = TweetScraper(TwitterService())
    controller = TweetController(scraper)
    return controller.get_sentiment(user,thread)
    
    
    