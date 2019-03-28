from Twitter_Bot.Bot import Bot
import json

# Minneapolis ID
location = 23424977

with open('twitter_credentials.json') as cred_data:
    info = json.load(cred_data)
    consumer_key = info['CONSUMER_KEY']
    consumer_secret = info['CONSUMER_SECRET']
    access_key = info['ACCESS_TOKEN']
    access_secret = info['ACCESS_SECRET']

bot1 = Bot(consumer_key, consumer_secret, access_key, access_secret)

print(bot1.search_tweets("%23ProcrastinationIn5Words"))

'''
trends = {bot1.get_trends(location)[0]['trends'], bot1.get_trends(location)[0]['trends']}
test = []
for trend in trends:
    if "#" in trend["name"]:
        test.append(trend)

for t in test:
    print(t['name'])
print('\n')

'''