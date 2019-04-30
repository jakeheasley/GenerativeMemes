"""Collection of functions that post to twitter feed without user interaction.
    All General_Post functions should be passed the bot, sql object, and chain"""


# Posts inspirational message
def inspire(bot, sql, chain):
    tweets = sql.trend_query("inspired")

    chain.update_text(tweets)
    generated = chain.make_sent()
    text = generated + " #inspired"
    bot.upload_text(text=text)


def weather(bot, sql, chain):
    tweets = sql.trend_query("weather")

    chain.update_text(tweets)
    generated = chain.make_sent()
    text = generated[:-1] + "." + " #WeatherReport"
    bot.upload_text(text=text)


def horoscope(bot, sql, chain):
    tweets = sql.trend_query("horoscope")

    chain.update_text(tweets)
    generated = chain.make_sent()
    text = generated + " #horoscope"
    bot.upload_text(text=text)


function_names = {"horoscope": horoscope,
                  "weather": weather,
                  "inspire": inspire
}