import os
import configparser
import tweepy

# create and import config
# config section title is 'Keys' and keys are named as below
cf = configparser.ConfigParser()
cf.read('config.ini')

def grab_tweets(user, count = 5):
    # authorize twitter with tweepy
    auth = tweepy.OAuthHandler(cf['Keys']['consumer_key'], cf['Keys']['consumer_secret'])
    auth.set_access_token(cf['Keys']['access_key'], cf['Keys']['access_secret'])
    api = tweepy.API(auth)

    # grab Status objects for desired user
    tweets = api.user_timeline(screen_name = user, count = count)

    # grab only the text value from the Status objects
    tweet_text = []
    for tweet in tweets:
        tweet_text.append(tweet.text)

    return tweet_text
