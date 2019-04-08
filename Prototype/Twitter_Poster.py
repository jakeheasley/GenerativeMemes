from Twitter_Bot.Bot import Bot
from Markov_Object.Markov_Chain import Chain
from pathlib import Path
import json
import os
from datetime import datetime
from SQL import SQL

before = datetime.now()

chars = 140
tries = 100
ratio = .5
handle = "Inspire_us"

# Geotag for Minneapolis
location = 23424977

# Finding filepath for twitter_credentials.json
base_path = Path("twitter_credentials.json").parent
file_path = (base_path / "../Prototype/Twitter_Bot/twitter_credentials.json").resolve()

# Loads twitter credentials from json file
with open(file_path) as cred_data:
    info = json.load(cred_data)
    consumer_key = info['CONSUMER_KEY']
    consumer_secret = info['CONSUMER_SECRET']
    access_key = info['ACCESS_TOKEN']
    access_secret = info['ACCESS_SECRET']

# Creates twitter_bot that connects to twitter account
bot = Bot(consumer_key=consumer_key,
          consumer_secret=consumer_secret,
          access_key=access_key,
          access_secret=access_secret)

# Connects to SQL database
sql = SQL(host="softwaredev.caybzpwuhc8n.us-east-2.rds.amazonaws.com",
          port=6666,
          username="root",
          password="paulsmemes",
          database="Memes")


# Get trend information
def make_trend():
    trend = ""
    for x in bot.get_trends(location).values():
        trend = x
        break

    tweet_list = bot.search_tweets(trend)
    database_insertion(tweet_list)


def make_tweet():
    database_insertion(tweet_list=bot.get_user_tweets(handle))


def database_insertion(tweet_list):
    sql.insertion(tweet_list)


sql_list = []
chain = Chain(chars=chars,
              tries=tries,
              ratio=ratio,
              tweet_list=sql_list)

markov_tweet = chain.make_sent(1)

for chain in markov_tweet:
    bot.upload_text(chain)

os.remove(file_path)
after = datetime.now()

# print("total time for program "+after-before)
