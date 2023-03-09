import snscrape.modules.twitter as sntwitter
import collections
import time
from textblob import TextBlob

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
        for reply in self.strategy.search_tweets(query):
            if reply.inReplyToTweetId == tweet_id:
                replies.append({
                    'displayname':reply.user.displayname,
                    'username':reply.user.username,
                    'rawContent':reply.rawContent,
                    'renderedContent':reply.renderedContent,
                    'date':reply.date,
                    })
        
        return replies

    def get_account_audiences(self,user,date):
        tweets = self.get_tweets(user,date)
        audiences = []
        for tweet in tweets:
            tweet_id = tweet['id']
            replies = self.get_replies(user,tweet_id)
            for index,reply in enumerate(replies):
                if index > 100:
                    break
                audiences.append({
                    'displayname':reply['displayname'],
                    'username':reply['username'],
                    })
        
        return audiences
    
    def get_thread(self,url):
        tweet_id = url.split('/')[-1]
        username = url.split('/')[-3]
        query = f'from:{username} since_id:{tweet_id}'
        tweets = []
        thread_sum = 0
        thread_audiences_sum = 0
        thread_reply_count = 0
        
        for tweet in self.strategy.search_tweets(query):
            audiences_sum = 0
            blob = TextBlob(tweet.rawContent)
            tweet_sentiment = blob.sentiment.polarity
            thread_sum += tweet_sentiment
            
            replies = self.get_replies(username,tweet.id)
            for reply in replies:
                blob = TextBlob(reply['rawContent'])
                reply_sentiment = blob.sentiment.polarity
                audiences_sum += reply_sentiment
                thread_audiences_sum += audiences_sum
                thread_reply_count += 1
                
            tweets.append({
                'id':tweet.id,
                'content':tweet.content,
                'rawContent':tweet.rawContent,
                'date':tweet.date,
                'tweet_sentiment':tweet_sentiment,
                'replies':replies,
                'audience_sentiment':audiences_sum / len(replies) if audiences_sum > 0 else 0
                })
        
        tweets.reverse()
        
        thread_sentiment = thread_sum / len(tweets) if thread_sum > 0 else 0
        audience_sentiment = thread_audiences_sum / thread_reply_count if thread_audiences_sum > 0 else 0

        return {'tweets':tweets,'thread_sentiment':thread_sentiment,'audience_sentiment':audience_sentiment}