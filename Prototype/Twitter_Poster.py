from Twitter_Bot.Bot import Bot
from Markov_Object.Markov_Chain import Chain
import random
from SQL import SQL
from Login_Settings_General import Login_Settings

chars = 140
tries = 100
ratio = .5
handle = "Inspire_us"

# Geotag for Minneapolis
location = 23424977

# Creates twitter_bot that connects to twitter account
bot = Bot(consumer_key=Login_Settings.twitter['CONSUMER_KEY'],
          consumer_secret=Login_Settings.twitter['CONSUMER_SECRET'],
          access_key=Login_Settings.twitter['ACCESS_TOKEN'],
          access_secret=Login_Settings.twitter['ACCESS_SECRET'])

# Connects to SQL database
sql = SQL(host=Login_Settings.database['HOST'],
          port=Login_Settings.database['PORT'],
          username=Login_Settings.database['DB_USERNAME'],
          password=Login_Settings.database['DB_PASSWORD'],
          database=Login_Settings.database['DATABASE'])


# Get trend information
def make_trend():
    """Todo: what does this do?
    @:return todo: what does this do?"""
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
    """TODO: what does this do?
    @:return """
    database_insertion(tweet_list=bot.get_user_tweets(handle))
    return sql.author_query(handle)


def database_insertion(tweet_list):
    """TODO what does this do?"""
    sql.insertion(tweet_list)


if bool(random.getrandbits(1)):
    sql_list = make_trend()
else:
    sql_list = make_tweet()

chain = Chain(chars=chars,
              tries=tries,
              ratio=ratio,
              tweet_list=sql_list)

markov_tweet = chain.make_sent()

bot.upload_text(markov_tweet)
