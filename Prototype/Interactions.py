# Collection of functions that involve user interaction.
# All interaction functions should be passed the bot object, sql
# object, chain, and mention tweet
import tweepy
from ast import literal_eval

# todo: fuzzify instruction argument matching; i.e. for functions that allow it, use argument
#  from anywhere in the tweet, not just the word immediately following.


# Generates random tweet from twitter account specified by user
def impersonate(bot, sql, chain, mention):
    tweeter = "@" + mention['username']

    # Get the the person we want to impersonate from the instruction
    scrape = mention["text"].split(bot.handle, '1')[0].split()[2]
    tweet_id = mention["tweet_id"]

    # Error handling for unknown username and/or any other tweepy error
    if len(sql.author_query(scrape)) == 0:
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

        sql.insertion_tweet(tweets)
    tweets = sql.author_query(scrape)

    chain.update_text(tweets)
    generated = chain.make_sent()

    text = tweeter + " " + generated

    bot.upload_text(text=text, reply=tweet_id)


# Returns an inspirational quot
def inspire_me(bot, sql, chain, mention):
    tweet_id = mention["tweet_id"]
    tweeter = "@" + mention["username"]
    tweets = sql.tag_query("inspired")
    chain.update_text(tweets)

    text = tweeter + " " + chain.make_sent() + " #inspired"
    bot.upload_text(text=text, reply=tweet_id)


# Returns a generated weather report
def weather_report(bot, sql, chain, mention):
    tweet_id = mention["tweet_id"]
    tweeter = "@" + mention["username"]
    tweets = sql.tag_query("weather")

    chain.update_text(tweets)
    text = tweeter + " " + chain.make_sent() + " #WeatherReport"
    bot.upload_text(text=text, reply=tweet_id)


# Returns a horoscope based on given sign
def horoscope(bot, sql, chain, mention):
    sign_list = ["aquarius", "pisces", "aries", "taurus", "gemini", "cancer",
                 "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn"]
    tweet_id = mention["tweet_id"]
    tweeter = "@" + mention["username"]
    tweets = sql.tag_query("horoscope")

    chain.update_text(tweets)

    # Get sign from instruction
    sign = mention["text"].split(bot.handle, '1')[0].split()[2]

    # Checking for incorrect signs/Ophiuchus
    if sign.lower() not in sign_list:
        if sign.lower() is "Ophiuchus":
            text = tweeter + " I doesn't believe in that sign #only12"
        else:
            text = tweeter + " That sign doesn't seem to exist yet"
        bot.upload_text(text=text, reply=tweet_id)
    else:
        seed = "#" + sign[0].upper() + sign[1:] + ":"

        text = tweeter + " " + chain.make_sent_seed(seed) + " #horoscope"
        bot.upload_text(text=text, reply=tweet_id)


# What happens when the bot doesn't understand a command
def dont_understand(bot, sql, chain, mention):
    tweeter = "@" + mention["username"]
    tweet_id = mention["tweet_id"]
    chain.update_text(sql.tag_query("flirt"))
    text = tweeter + " " + "\"" + chain.make_sent(140) + " #ILoveYou #ButIDontUnderstandYou"
    bot.upload_text(text=text, reply=tweet_id)


# Dictionary of function names. Key = str(function), value = function
function_names = {
    "impersonate": impersonate,
    "dont_understand": dont_understand,
    "inspiration": inspire_me,
    "weather": weather_report,
    "horoscope": horoscope
}
