#TrumPoem Generator

The new President of the United States is, in his own words, of the highest, BIGGEST caliber in almost all things. Now, without even knowing it, he's mastered the world of procedurally generated poetry&mdash;in the form of more tweets.

There are currently two scripts set up.

##Inaug.py

This script simply uses the included transcript of the Inauguration to randomly generate a list of words. The results can often be quite poetic, and quite terrifying. Call the script at the command line and provide an integer argument for the desired number of printed words.

There's nothing fancy at work here--this is mostly a proof of concept and will give you straight up random results.

##Twitbot.py

To use the bot, you'll need to install the required libraries with pip. Set up and source a virtual environment if you wish, and then:
```bash
pip install -r requirements.txt
```
The bot utilizes the `markovify` library to generate tweets based on Markov chains. This results in natural-sounding output that eerily resembles actual Trump tweets. Learn more about Markovify [here](https://github.com/jsvine/markovify)&mdash;there's a lot of settings you can play around with in an interactive session to generate longer texts, even entire Trump tweet-essays if you so desire.

The `twitbot.py` script doesn't take any arguments like `inaug.py`. Instead, it uses the `tweepy` Twitter library to make an API call out to @theRealDonald and grabs the maximum allowed number of tweets (currently, I think, 3200). It then does some cleaning up to remove policy violations on Twitter like hashtag pollution and automated mentions, and then uses that cleaned up set of tweets to generate 1 new tweet, which it then posts to the account referenced by the Twitter API keys in your `config.ini`.

Your `config.ini` should look something like this, located in the root directory of the repo:
```
[Keys]
consumer_key =
consumer_secret =
access_key =
access_secret =
```
with values after the equals signs. Reference the official Twitter API documentation for more information on setting up your authentication keys.

To automate your bot, simply set up something like a crontab job to run at an regular interval&mdash;the bot currently lives on my raspberry pi and posts hourly.
