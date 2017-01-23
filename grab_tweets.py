import os
import configparser
import tweepy

# create and import config
cf = configparser.ConfigParser()
cf.read('config.ini')

def grab_tweets(user):
