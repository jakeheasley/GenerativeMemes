import mysql.connector as mysql
import Scrape_Markov as scrape

#connect to database
mydb = mysql.connect(
    host = "localhost",
    port = 25565,
    user = "meme",
    passwd = "software_dev",
    database = "meme"
)

mycursor = mydb.cursor()

Author = input()

#get all tweets from Inspire_us
scrape.get_all_tweets(Author)
data = scrape.return_tweets()


#insertion statement query
sql_insert = """insert ignore into content (source_text,author) values (%s,%s); """
mycursor.executemany(sql_insert,data)
mydb.commit()
mycursor.close()
