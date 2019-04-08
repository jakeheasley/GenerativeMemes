from Twitter_Bot.Bot import Bot
import json
from Markov_Object.Markov_Chain import Chain

# Minneapolis ID
location = 23424977

chars = 140
tries = 100
ratio = .5

with open('twitter_credentials.json') as cred_data:
    info = json.load(cred_data)
    consumer_key = info['CONSUMER_KEY']
    consumer_secret = info['CONSUMER_SECRET']
    access_key = info['ACCESS_TOKEN']
    access_secret = info['ACCESS_SECRET']

bot = Bot(consumer_key=consumer_key,
          consumer_secret=consumer_secret,
          access_key=access_key,
          access_secret=access_secret)

tweets = bot.get_user_tweets("inspire_us")

chain = Chain(chars=chars,
              tries=tries,
              ratio=ratio,
              tweet_list=tweets)

print(chain.make_sent(1))
