from Login_Settings_General import Login_Settings
from SQL import SQL
from Bot import Bot
import Scheduler_Initializer


def config():
    sql = SQL(host=Login_Settings.database['HOST'],
              port=Login_Settings.database['PORT'],
              username=Login_Settings.database['DB_USERNAME'],
              password=Login_Settings.database['DB_PASSWORD'],
              database=Login_Settings.database['DATABASE'])

    # Creates twitter_bot that connects to twitter account
    bot = Bot(consumer_key=Login_Settings.twitter['CONSUMER_KEY'],
              consumer_secret=Login_Settings.twitter['CONSUMER_SECRET'],
              access_key=Login_Settings.twitter['ACCESS_TOKEN'],
              access_secret=Login_Settings.twitter['ACCESS_SECRET'])

    sql.table_setup()

    # Inserts initial dataset into database (500 per twitter account)
    inspire_list = bot.get_user_tweets("inspire_us", "inspired") + bot.get_user_tweets("InspowerMinds", "inspired")
    weather_list = bot.get_user_tweets("NWS", "weather") + bot.get_user_tweets("weatherchannel", "weather")
    horoscope_list = bot.get_user_tweets("ZodiacFacts", "horoscope")
    romance_list = bot.get_user_tweets("romntic_quotes", "flirt") + bot.get_user_tweets("LikeLoveInLove", "flirt") + \
                   bot.get_user_tweets("RomanticcQuotes", "flirt")
    sql.insertion_tweet(inspire_list+horoscope_list+weather_list+romance_list)
    sql.close()

    Scheduler_Initializer.initialize()


if __name__ == "main":
    config()
