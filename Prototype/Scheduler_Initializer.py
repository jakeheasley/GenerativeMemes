'''Run this whenever you run the program on a new machine
as it will determine what the latest mention is before scheduler determines it'''

from Twitter_Bot.Bot import Bot
import Login_Settings

# Creates twitter_bot that connects to twitter account
bot = Bot(consumer_key=Login_Settings.twitter['CONSUMER_KEY'],
          consumer_secret=Login_Settings.twitter['CONSUMER_SECRET'],
          access_key=Login_Settings.twitter['ACCESS_TOKEN'],
          access_secret=Login_Settings.twitter['ACCESS_SECRET'])

latest_mention = "0"
mentions = bot.get_mentions(latest_mention)
for mention in mentions:
    tweet_id = mention["tweet_id"]

    if int(tweet_id) > int(latest_mention):
        latest_mention = tweet_id

with open("last_mention_id.txt","w+") as f:
    f.write(latest_mention)
    f.close()
