from Twitter_Bot.Bot import Bot
import json

# Minneapolis ID (location for trends near us)
location = 23424977

# authenticate the bot w/ login credentials from external json
with open('twitter_credentials.json') as cred_data:
    info = json.load(cred_data)
    consumer_key = info['CONSUMER_KEY']
    consumer_secret = info['CONSUMER_SECRET']
    access_key = info['ACCESS_TOKEN']
    access_secret = info['ACCESS_SECRET']

# instantiate bot
bot1 = Bot(consumer_key, consumer_secret, access_key, access_secret)
bot1.rate_status()

# trends testing
trends = bot1.get_trends(location)[0]['trends']
test = []
for trend in trends:
    if "#" not in trend["name"]:
        trends.remove(trend)
        test.append(trend)

for t in test:
    print(t['name'])
print('\n')
for trend in trends:
    print(trend['name'])
    if trend in test:
        print("yes")
