import tweepy
import json
import sys
import re


with open('twitter_credentials.json') as cred_data:
    info = json.load(cred_data)
    consumer_key = info['CONSUMER_KEY']
    consumer_secret = info['CONSUMER_SECRET']
    access_key = info['ACCESS_TOKEN']
    access_secret = info['ACCESS_SECRET']


def get_all_tweets(screen_name):
    global all_the_tweets
    # Authorization and initialization

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # initialization of a list to hold all Tweets
    all_the_tweets = []

    # We will get the tweets with multiple requests of 200 tweets each
    new_tweets = api.user_timeline(screen_name=screen_name, count=200, include_rts=False, tweet_mode='extended')
    # saving the most recent tweets
    all_the_tweets.extend(new_tweets)
    # save id of 1 less than the oldest tweet
    oldest_tweet = all_the_tweets[-1].id-1

    # grabbing tweets till none are left
    while len(new_tweets) > 0:
        # The max_id param will be used subsequently to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name,
        count=200, max_id=oldest_tweet, tweet_mode='extended', include_rts=False)

        # save most recent tweets

        all_the_tweets.extend(new_tweets)

        # id is updated to oldest tweet - 1 to keep track
        oldest_tweet = all_the_tweets[-1].id - 1
        print ('...%s tweets have been downloaded so far' % len(all_the_tweets))

    # transforming the tweets into a 2D array that will be used to populate the csv

    # outtweets = [[tweet.id_str,
    #             tweet.created_at,
    #            tweet.full_text.encode('utf-8')] for tweet in all_the_tweets]

    outtweets = []
    just_tweets = []
    for tweet in all_the_tweets:
        tweet_text = re.sub("https:.*$", "", tweet.full_text.encode('utf-8'))
        tweet_text = re.sub("&amp", "&", tweet_text)
        just_tweets.append(tweet_text)
        outtweets.append([tweet.id_str, tweet.created_at, tweet_text])

    all_the_tweets = just_tweets


def return_tweets():
    return all_the_tweets


all_the_tweets = []


if __name__ == '__main__':
    name = sys.argv
    get_all_tweets(name)
