import tweepy
import re


class Bot:

    # Initialize bot with keys
    def __init__(self, consumer_key, consumer_secret, access_key, access_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        self.api = tweepy.API(auth)

    # Upload a text based tweet
    def upload_text(self, text):
        self.api.update_status(text)

    # Upload a picture
    def upload_media(self, filename):
        self.api.update_with_media(filename)

    # Scrape tweets
    def get_tweets(self, handle):
        # initialization of a list to hold all Tweets
        all_the_tweets = []

        # Initial set of 200 tweets
        new_tweets = self.api.user_timeline(screen_name=handle, count=200, include_rts=False, tweet_mode='extended')
        all_the_tweets.extend(new_tweets)

        # One less than id of oldest tweet
        oldest_tweet = all_the_tweets[-1].id - 1

        # Scraping tweets
        while len(new_tweets) > 0:
            # The max_id param will be used subsequently to prevent duplicates
            new_tweets = self.api.user_timeline(screen_name=handle,
                                                count=200, max_id=oldest_tweet,
                                                tweet_mode='extended',
                                                include_rts=False)
            # save most recent tweets
            all_the_tweets.extend(new_tweets)

            # id is updated to oldest tweet - 1 to keep track
            oldest_tweet = all_the_tweets[-1].id - 1

        just_tweets = []
        for tweet in all_the_tweets:

            # Removing unwanted links at end of tweets and changing amp to &
            tweet_text = re.sub("https:.*$", "", tweet.full_text.encode('utf-8'))
            tweet_text = re.sub("&amp", "&", tweet_text)

            just_tweets.append(tweet_text)

        return just_tweets

    # Returns list of trends from a location
    def get_trends(self, location):
        return self.api.trends_place(location)

    # Helper function that tells how many queries we have left per hour
    def rate_status(self):
        status = self.api.rate_limit_status()
        remaining = status['resources']['feedback']['/feedback/show/:id']['remaining']
        return remaining


