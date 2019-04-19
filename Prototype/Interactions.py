"""Collection of functions that involve user interaction.
    All interaction functions should be passed the bot object, sql
    object, chain, and mention tweet"""
import tweepy
from ast import literal_eval


# Generates random tweet from twitter account specified by user
def generate(bot, sql, chain, mention):
    tweeter = "@" + mention['username']
    scrape = mention["text"].split('@markoving_bot, 1')[0].split()[2]
    tweet_id = mention["tweet_id"]

    # Error handling for unknown username and/or any other tweepy error
    try:
        tweets = bot.get_user_tweets(scrape)
    except tweepy.TweepError as e:

        # Evaluating error message as dict
        error_dict = literal_eval(e.response.text)

        # Getting error code
        error_num = error_dict["errors"][0]["code"]
        if int(error_num) == 34:
            text = tweeter + " Sorry, but we couldn't find that Twitter user!"
        else:
            text = tweeter + " Sorry! Something's gone wrong on my end. Try again!"
        bot.upload_text(text=text, reply=tweet_id)
        return

    sql.insertion(tweets)
    tweets = sql.author_query(scrape)

    chain.update_text(tweets)
    generated = chain.make_sent()

    text = tweeter + " " + generated

    bot.upload_text(text=text, reply=tweet_id)


# Dictionary of function names. Key = str(function), value = function
function_names = {
    "generate": generate
}