from Twitter_Bot.Bot import Bot
import tweepy
from ast import literal_eval

import json
from Markov_Object.Markov_Chain import Chain
import Login_Settings
# Minneapolis ID
location = 23424977

chars = 140
tries = 100
ratio = .5

# Creates twitter_bot that connects to twitter account
bot = Bot(consumer_key=Login_Settings.twitter['CONSUMER_KEY'],
          consumer_secret=Login_Settings.twitter['CONSUMER_SECRET'],
          access_key=Login_Settings.twitter['ACCESS_TOKEN'],
          access_secret=Login_Settings.twitter['ACCESS_SECRET'])
print(bot.get_mentions(0))
'''
tweets = bot.get_user_tweets("RoastsBot")
tweet_string = []

for tweet in tweets:
    tweet_string.append(tweet[1])


chain = Chain(chars=chars,
              tries=tries,
              ratio=ratio,
              tweet_list=tweet_string)

markov = chain.make_sent(50)

for m in markov:
    print(m)
'''