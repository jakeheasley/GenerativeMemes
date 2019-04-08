import mysql.connector as mysql

db = mysql.connect(host = "softwaredev.caybzpwuhc8n.us-east-2.rds.amazonaws.com",
port = 6666, user = "root", password = "paulsmemes")

cursor = db.cursor()
cursor.execute("create database Memes;")
cursor.execute("use Memes;")
cursor.execute("create table Tweets (Author text, Tweet longtext, id int, trend text, date_pulled date, tweet_date date, Primary key (id));")
cursor.close()
