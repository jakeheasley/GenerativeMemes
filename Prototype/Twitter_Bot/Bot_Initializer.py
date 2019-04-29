from Twitter_Bot.Bot import Bot
from SQL import SQL

from Markov_Object.Markov_Chain import Chain
from Login_Settings_General import Login_Settings

# Minneapolis ID
location = 23424977


chars = 140
tries = 100
ratio = .6

# Connects to SQL database
sql = SQL(host=Login_Settings.database['HOST'],
          port=Login_Settings.database['PORT'],
          username=Login_Settings.database['DB_USERNAME'],
          password=Login_Settings.database['DB_PASSWORD'],
          database=Login_Settings.database['DATABASE'])

# Creates twitter_bot that connects to twitter account
bot = Bot(consumer_key=Login_Settings.twitter['CONSUMER_KEY'],
          consumer_secret=Login_Settings.twitter['CONSUMER_SECRET'],
          access_key=Login_Settings.twitter['ACCESS_TOKEN'],
          access_secret=Login_Settings.twitter['ACCESS_SECRET'])

# Creates empty Markov chain for later use
chain = Chain(chars=chars,
              tries=tries,
              ratio=ratio,
              tweet_list=["dummy info \n"])

'''tuple_list = bot.get_user_tweets("RomanticcQuotes", tag="flirt") + bot.get_user_tweets("LikeLoveInLove", tag="flirt") + bot.get_user_tweets("romntic_quotes", tag="flirt")

sql.insertion(tuple_list)'''

chain.update_text(sql.trend_query("flirt"))

for x in range(1, 50):
    print(chain.make_sent(190))


'''tweets = bot.get_user_tweets("RoastsBot")
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