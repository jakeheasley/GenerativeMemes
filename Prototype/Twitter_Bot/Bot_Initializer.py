from Twitter_Bot.Bot import Bot
from SQL import SQL

import json
from Markov_Object.Markov_Chain import Chain
import Login_Settings
# Minneapolis ID
location = 23424977


chars = 140
tries = 100
ratio = .3

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

'''tuple_list = bot.get_user_tweets("ZodiacFacts", tag="horoscope")
sql.insertion(tuple_list)'''

latest_mention = "0"
mentions = bot.get_mentions(latest_mention)
for mention in mentions:
    tweet_id = mention["tweet_id"]

    if int(tweet_id) > int(latest_mention):
        latest_mention = tweet_id

with open("last_mention_id.txt","w+") as f:
    f.write(latest_mention)
    f.close()

with open("last_mention_id.txt","r") as f:
    print(f.read())

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