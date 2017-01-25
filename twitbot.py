#!/usr/bin/python

import markovify
import twittercalls

# create Markov text model
text_model = markovify.Text(
    " ".join(twittercalls.grab_tweets('realDonaldTrump')))

# create our new tweet and post it
tweet = text_model.make_short_sentence(140)
twittercalls.post_tweet(tweet)
