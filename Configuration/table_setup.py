import mysql.connector as mysql

db = mysql.connect(host = "softwaredev.caybzpwuhc8n.us-east-2.rds.amazonaws.com",
port = 6666, user = "root", password = "paulsmemes")

cursor = db.cursor()
cursor.execute("create database Memes;")
cursor.execute("use Memes;")
cursor.execute("create table Tweets (Author text, Tweet longtext, id bigint, trend text, date_pulled date, tweet_date date, Primary key (id));")
cursor.close()

"""use Memes;
create table ocr (photo longblob, label longtext, id int auto_increment, primary key(id));
create table ocr_similar (photo_text varchar(140), photo_id int, foreign key(photo_id) references ocr(id), primary key(photo_text, photo_id));"""
