import snscrape.modules.twitter as sntwitter
import collections

class TweetScraper:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def get_tweets(self, user, date):
        tweets = []
        query = f"from:{user} {date}" 
        for tweet in self.strategy.search_tweets(query):
            if tweet.inReplyToTweetId is not None:
                tweets.append({
                    'type': 'reply',
                    'username': tweet.user.username,
                    'date': tweet.date,
                    'text': tweet.content,
                    'url': tweet.url,
                    'id': tweet.id,
                })
            else:
                tweets.append({
                    'type': 'tweet',
                    'username': tweet.user.username,
                    'date': tweet.date,
                    'text': tweet.content,
                    'url': tweet.url,
                    'id': tweet.id,
                })
        return tweets
    
    def get_replies(self,user, tweet_id):
        replies = []
        query = f'to:{user} since_id:{tweet_id}'
        counter = 0
        for reply in self.strategy.search_tweets(query):
            if reply.inReplyToTweetId == tweet_id:
                replies.append(reply.user.username)
                counter += 1
                print('counter',counter)
                if(counter <= 2):
                    break
        
        return replies