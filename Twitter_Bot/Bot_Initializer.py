from Bot import Bot
import json

location = 23424977

with open('twitter_credentials.json') as cred_data:
    info = json.load(cred_data)
    consumer_key = info['CONSUMER_KEY']
    consumer_secret = info['CONSUMER_SECRET']
    access_key = info['ACCESS_TOKEN']
    access_secret = info['ACCESS_SECRET']

bot1 = Bot(consumer_key, consumer_secret, access_key, access_secret)
trends = bot1.get_trends(location)
