import tweepy
from tweepy import Cursor
import re
import datetime
import json


class Bot:

    # Initialize and authorize bot with keys
    def __init__(self, consumer_key, consumer_secret, access_key, access_secret):
        """instantiate a new Bot and authorize it with credentials supplied.
        @:param consumer_key, consumer_secret, access_keu, acess_secret: strings of login info to the twitter API."""
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        self.api = tweepy.API(auth)
        self.handle = "@markoving_bot"

    def upload_text(self, text, reply=None):
        """tweets text.
        @:param text: string to tweet.
        @:param reply: optional tweet id of tweet to post in reply to."""
        if reply is None:
            self.api.update_status(status=text)
        else:
            self.api.update_status(status=text, in_reply_to_status_id=reply)

    def upload_media(self, filename, text=None):
        """tweets media.
        @:param filename: string filepath of media to post.
        @:param text: optional string to tweet."""
        if text is None:
            self.api.update_with_media(filename)
        else:
            self.api.update_with_media(filename, text)

    def get_user_tweets(self, handle, tag=None):
        """scrapes tweets from indicated user.
        @:param handle: the string handle of the user to scrape from.
        @:return: formatted list of all scraped tweets"""
        # initialization of a list to hold all Tweets
        tweets = []
        timeline = Cursor(self.api.user_timeline, screen_name=handle,
                          tweet_mode='extended',
                          exclude_replies=True,
                          include_rts=False)
        return self.clean_tweets(timeline, tag)

    def search_tweets(self, search_term, trend):
        """searches twitter for supplied search term.
        @:param search_term: string term to search
        @:return self.clean_tweets.
        TODO: what type is self.clean_tweets?
        TODO: why do we return trend?"""
        # initialization of a list to hold all Tweets
        search_term = search_term + "-filter:retweets"
        search_tweets = Cursor(self.api.search, q=search_term,
                               tweet_mode='extended')
        return self.clean_tweets(search_tweets, trend)

    def clean_tweets(self, timeline, tag=None):
        """formats tweets for database entry as a tuple-list.
        @:param timeline: TODO: what's this?
        @:param trend: optional hashtag associated with the trend of a tweet
        @:return list of tuples where each tuple corresponds to one tweet."""
        tweets = []
        date = datetime.datetime.today()
        date = date.strftime('%Y-%m-%d')
        for tweet in timeline.items(2000):
            tweet_text = re.sub("https:.*$", "", tweet.full_text)
            tweet_text = re.sub("&amp", "&", tweet_text)
            tweets.append((tweet.user.screen_name,
                           tweet_text.replace("\n", " "),
                           tweet.id_str,
                           tag,
                           date,
                           tweet.created_at.strftime('%Y-%m-%d')))
        return tweets

    def get_status(self, tweet_id):
        tweet = self.api.statuses_lookup([tweet_id],tweet_mode='extended')[0]
        tweet_text = re.sub("https:.*$", "", tweet.full_text)
        tweet_text = re.sub("&amp", "&", tweet_text)

        format_tweet = {"username": tweet.user.screen_name,
                                   "text": tweet_text,
                                   "tweet_id": tweet.id_str,
                                   "reply_id": tweet.in_reply_to_status_id}
        return format_tweet

    def get_mentions(self, recent_id):
        """gets all tweets that @mention the bot.
        @:param recent_id: ID string of latest mention that we have pulled
        @:return tweet_list returns dictionary of mentioned tweets with username, text, and tweet ID"""
        mentions = Cursor(self.api.search, q=self.handle + " -filter:retweets",
                          tweet_mode='extended',
                          since_id=recent_id,)
        tweet_list = []
        for tweet in mentions.items(500):
            # Ensures that the bot is not responding to a previous response
            if not ((tweet.user.screen_name == "markoving_bot") and (tweet.in_reply_to_status_id is not None)):
                tweet_text = re.sub("https:.*$", "", tweet.full_text)
                tweet_text = re.sub("&amp", "&", tweet_text)

                tweet_list.append({"username": tweet.user.screen_name,
                                   "text": tweet_text,
                                   "tweet_id": tweet.id_str,
                                   "reply_id": tweet.in_reply_to_status_id})

        return tweet_list

    def rate_status(self):
        """@:return number of queries remaining per hour."""
        return self.api.rate_limit_status()
