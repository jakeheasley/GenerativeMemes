import mysql.connector as mysql
import Scrape_Markov as scrape


mydb = mysql.connect(
    host = "localhost",
    port = 25565,
    user = "meme",
    passwd = "software_dev",
    database = "meme"
)

mycursor = mydb.cursor()

i = 0

#get all tweets from Inspire_us
scrape.get_all_tweets("Inspire_us")
data = scrape.return_tweets()

#insertion statement query
sql_insert = "insert into test (va, test_id) values (%s,%s)"


#creating row for each tweet
for x in data:
    tuple = (x,i)
    mycursor.execute(sql_insert,tuple)
    mydb.commit()
    i = i + 1



mycursor.execute("select va from test;")

#writing the query into a file
with open("SQLQueryText.txt", "w", encoding = "utf-8") as text_file:
    for x in mycursor:
        text_file.write(x[0]+"\n")
