from Twitter_Bot.Bot import Bot
from Markov_Object.Markov_Chain import Chain
from SQL import SQL
from Login_Settings_General import Login_Settings
import Interactions
import General_Posts
import datetime
import time

chars = 140
tries = 100
ratio = .4

# ID of latest post that mentioned bot. Default to zero (will change)
with open("last_mention_id.txt", "r") as f:
    latest_mention = f.read()
    f.close()

with open("latest_post.txt", "r") as f:
    info = f.read().splitlines()
    f.close()

# Gets last post from file in correct datetime format
latest_post = datetime.datetime.strptime(info.pop(0), "%Y-%m-%d %H:%M:%S.%f")

# List of General_Post functions (update as you create functions)
post_list = info

# Tracker that is set to the last time bot posted, does not include interactions


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
while True:
    # Gets all the times that the bot is mentioned
    mentions = bot.get_mentions(latest_mention)

    # Only runs if there are any new mentions
    if len(mentions) > 0:
        for mention in mentions:

            # Username of person that @ the bot
            tweeter = "@"+mention["username"]

            tweet_id = mention["tweet_id"]

            # Removes all text before mention and then parses later text into list
            instruction = mention["text"].split('@markoving_bot, 1')[0].split()[1:]
            # If instruction is not in interaction dictionary
            if len(instruction) is 0 or instruction[0].lower() not in Interactions.function_names.keys():
                Interactions.dont_understand(bot, sql, chain, mention)
            else:
                # Calls the interaction function
                user_function = Interactions.function_names[instruction[0].lower()]
                user_function(bot, sql, chain, mention)
            if int(tweet_id) > int(latest_mention):
                latest_mention = tweet_id

                # Saves last_mention to a file in case program needs to be restarted
                with open("last_mention_id.txt", "w+") as f:
                    f.write(latest_mention)

    # Determines if it has been three hours since previous post
    current_time = datetime.datetime.now()
    time_passed = current_time-latest_post

    if time_passed.total_seconds() > 10800:
        # Get function from dictionary using post_list
        post = General_Posts.function_names[post_list[0]]
        post(bot, sql, chain)

        # Moves the post function to the back of the function list. Ensuring
        # an even distribution of our various types of posts
        post_list.append(post_list.pop(0))

        latest_post = datetime.datetime.now()

        with open("latest_post.txt", "w+") as f:
            f.write(str(latest_post)+"\n")
            for l in post_list:
                f.write(l + "\n")

    #  Sleeps for 60 seconds
    time.sleep(15)
