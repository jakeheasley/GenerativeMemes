"""Collection of functions that post to twitter feed without user interaction.
    All General_Post functions should be passed the bot, sql object, and chain"""


# Posts inspirational message
def inspire(bot, sql, chain):
    handle = "inspire_us"
    sql.insertion(bot.get_user_tweets(handle))

    tweets = sql.author_query(handle)

    chain.update_text(tweets)
    generated = chain.make_sent()
    text = generated + " #inspired"
    bot.upload_text(text=text)


# Posts trending tweet
def trend(bot, sql, chain):
    location = 23424977
    bot.get_trends(location)

    search_trend = ""
    sql_trend = ""
    for key, val in bot.get_trends(location).items():
        search_trend = val
        sql_trend = key
        break

    tweet_list = bot.search_tweets(search_trend, sql_trend)
    sql.insertion(tweet_list)
    chain.update_text(sql.trend_query(sql_trend))
    text = chain.make_sent()

    if sql_trend not in text:
        text = text + " " + sql_trend

    bot.upload_text(text=text)

