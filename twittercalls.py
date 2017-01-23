import configparser
import tweepy

# create and import config
# config section title is 'Keys' and keys are named as below
cf = configparser.ConfigParser()
cf.read('config.ini')

# set up Twitter API
auth = tweepy.OAuthHandler(cf['Keys']['consumer_key'], cf['Keys']['consumer_secret'])
auth.set_access_token(cf['Keys']['access_key'], cf['Keys']['access_secret'])
api = tweepy.API(auth)

def grab_tweets(user, count = 5):

    # grab Status objects for desired user
    tweets = api.user_timeline(screen_name = user, count = count)

    # grab only the text value from the Status objects
    tweet_text = []
    for tweet in tweets:
        tweet_text.append(tweet.text)

    # split every tweet by spaces for word cleanup
    word_list = []
    for tweet in tweet_text:
        word_list.extend(tweet.split())

    # remove hashtags, links, and mentions to follow Twitter automation rules and beautify output
    not_allowed = ["@", "#", "http"]
    for item in not_allowed:
        for word in word_list:
            if item in word:
                word_list.remove(word)


    return word_list

def post_tweet(tweet):
    api.update_status(status = tweet)
