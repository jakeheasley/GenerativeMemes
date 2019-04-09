from Prototype.Twitter_Bot.Bot import Bot
from Prototype.Markov_Object.Markov_Chain import Chain
from pathlib import Path
import json
import random
from SQL import SQL

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
    search_trend = ""
    sql_trend = ""
    for key, val in bot.get_trends(location).items():
        search_trend = val
        sql_trend = key
        break

    tweet_list = bot.search_tweets(search_trend, sql_trend)
    database_insertion(tweet_list)
    return sql.trend_query(sql_trend)


def make_tweet():
    database_insertion(tweet_list=bot.get_user_tweets(handle))
    return sql.author_query(handle)


def database_insertion(tweet_list):
    sql.insertion(tweet_list)


if bool(random.getrandbits(1)):
    sql_list = make_trend()
else:
    sql_list = make_tweet()

chain = Chain(chars=chars,
              tries=tries,
              ratio=ratio,
              tweet_list=sql_list)

markov_tweet = chain.make_sent(1)

for chain in markov_tweet:
    bot.upload_text(chain)
