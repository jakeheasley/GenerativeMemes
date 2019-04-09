import mysql.connector as mysql
from datetime import datetime
from SQL import SQL
from Twitter_Bot.Bot import Bot
from pathlib import Path
import json

sql = SQL(host = "softwaredev.caybzpwuhc8n.us-east-2.rds.amazonaws.com", port = 6666, username = "root", password = "paulsmemes",database = "Memes")
handle = "Test"

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

location = 23424977


temp = bot.get_trends(location)
search = ""
sql_q = ""
for key, value in temp.items():
    search = value
    sql_q = key
    break

print(search, sql_q)
