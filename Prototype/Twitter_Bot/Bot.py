import tweepy
from tweepy import Cursor
import re
import datetime


class Bot:

    # Initialize and authorize bot with keys
    def __init__(self, consumer_key, consumer_secret, access_key, access_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        self.api = tweepy.API(auth)

    # Upload a text based tweet
    def upload_text(self, text):
        self.api.update_status(status=text)

    # Upload a picture (text optional)
    def upload_media(self, filename, text=None):
        if text is None:
            self.api.update_with_media(filename)
        else:
            self.api.update_with_media(filename, text)

    # Scrape tweets from specific user
    def get_user_tweets(self, handle):
        # initialization of a list to hold all Tweets
        tweets = []
        timeline = Cursor(self.api.user_timeline, screen_name=handle,
                          tweet_mode='extended',
                          exclude_replies=True,
                          include_rts=False)
        return self.clean_tweets(timeline)

    # Scrape tweets from specific search term
    def search_tweets(self, search_term):
        # initialization of a list to hold all Tweets
        search_term = search_term + "-filter:retweets"
        search_tweets = Cursor(self.api.search, q=search_term,
                               tweet_mode='extended',
                               exclude_replies=True)
        return self.clean_tweets(search_tweets)

    # Returns tuple-list of tweets that have been formatted
    def clean_tweets(self, timeline, trend=None):
        tweets = []
        date = datetime.datetime.today()
        date = date.strftime('%Y-%m-%d')
        for tweet in timeline.items(500):
            tweet_text = re.sub("https:.*$", "", tweet.full_text)
            tweet_text = re.sub("&amp", "&", tweet_text)
            tweets.append((tweet.user.screen_name,
                           tweet_text,
                           tweet.id_str,
                           trend,
                           date,
                           tweet.created_at.strftime('%Y-%m-%d')))

        return tweets

    # Returns dictionary of hashtag trends and respective search queries
    def get_trends(self, location):
        trends = self.api.trends_place(location)
        trend_search = {}
        for trend in trends[0]['trends']:
            if "#" in trend['name']:
                trend_search[trend['name']] = trend['query']
        return trend_search

    # Helper function that tells how many queries we have left per hour
    def rate_status(self):
        status = self.api.rate_limit_status()
        print(status)
        remaining = status['resources']['feedback']['/feedback/show/:id']['remaining']
        return remaining


