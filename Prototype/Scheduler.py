from Bot import Bot
from Markov_Chain import Chain
from SQL import SQL
from Login_Settings_General import Login_Settings
import Interactions
import General_Posts
import datetime
import time

# ID of latest post that mentioned bot. Default to zero (will change)
with open("last_mention_id.txt", "r") as f:
    latest_mention = f.read()
    f.close()

with open("latest_post.txt", "r") as f:
    info = f.read().splitlines()
    f.close()

# Gets last post time from file in correct datetime format
latest_post = datetime.datetime.strptime(info.pop(0), "%Y-%m-%d %H:%M:%S.%f")

# Get order of general posts
post_list = info

chars = 140
tries = 100
ratio = .4

# Creates twitter_bot that connects to twitter account
bot = Bot(consumer_key=Login_Settings.twitter['CONSUMER_KEY'],
          consumer_secret=Login_Settings.twitter['CONSUMER_SECRET'],
          access_key=Login_Settings.twitter['ACCESS_TOKEN'],
          access_secret=Login_Settings.twitter['ACCESS_SECRET'])

# Connects to SQL database
sql = SQL(host=Login_Settings.database['HOST'],
          port=Login_Settings.database['PORT'],
          username=Login_Settings.database['DB_USERNAME'],
          password=Login_Settings.database['DB_PASSWORD'],
          database=Login_Settings.database['DATABASE'])

# Creates empty Markov chain for later use
chain = Chain(chars=chars,
              tries=tries,
              ratio=ratio,
              tweet_list=["dummy info \n"])


def interaction_logic(tweet):
    """ Method that determines how the bot responds to a tweet. If the bot understands a command it will
     do the command. If it doesn't, it will try and go up the tweet thread until it finds a command to do. If that
     fails, it will respond by with stuff saying it doesn't understand"""
    instruction = tweet["text"].split('bot.handle, 1')[0].split()[1:]

    # Ignores any tweets from the bot itself
    if tweet["username"] == bot.handle[1:]:
        new_tweet = bot.get_status(tweet["reply_id"])
        return interaction_logic(new_tweet)

    # If the bot doesn't understand the tweet, check if the tweet is a reply
    # If the tweet is a reply, check the previous tweet, if not call dont_understand function
    elif len(instruction) is 0 or instruction[0].lower() not in Interactions.function_names.keys():
        if tweet["reply_id"] is None:
            user_function = Interactions.dont_understand
            return user_function, tweet
        else:
            new_tweet = bot.get_status(tweet["reply_id"])
            return interaction_logic(new_tweet)

    # if the bot does understand the tweet, do instruction
    else:
        user_function = Interactions.function_names[instruction[0].lower()]
        return user_function, tweet


def mentions():
    """Method that gets all of the latest mentions and runs the interaction logic funtion.
    Sets the latest_mention id too."""
    global latest_mention

    # Gets all the times that the bot is mentioned
    mention_list = bot.get_mentions(latest_mention)

    # Only runs if there are any new mentions
    if len(mention_list) > 0:
        for mention in mention_list:

            tweet_id = mention["tweet_id"]

            interaction, tweet = interaction_logic(mention)
            tweet["tweet_id"] = mention["tweet_id"]

            interaction(bot, sql, chain, tweet)

            if int(tweet_id) > int(latest_mention):
                latest_mention = tweet_id

                # Saves last_mention to a file in case program needs to be restarted
                with open("last_mention_id.txt", "w+") as f:
                    f.write(latest_mention)


# Facilitates general posting (what to post, when).
def general_posts():
    global latest_post

    # Determines if it has been three hours since previous post
    current_time = datetime.datetime.now()
    time_passed = current_time - latest_post

    if time_passed.total_seconds() > 10800:
        # Get function from dictionary using post_list
        post = General_Posts.function_names[post_list[0]]
        post(bot, sql, chain)

        # Moves the post function to the back of the function list. Ensuring
        # an even distribution of our various types of posts
        post_list.append(post_list.pop(0))

        latest_post = datetime.datetime.now()

        with open("latest_post.txt", "w+") as f:
            f.write(str(latest_post) + "\n")
            for l in post_list:
                f.write(l + "\n")


# Runs constantly
while True:
    mentions()
    general_posts()
    #  Sleeps for 15 seconds
    time.sleep(15)
