import mysql.connect as mysql
import datetime as datetime

#connceting to the local database

def CreateTables():
    database = mysql.connect(
        host = "localhost",
        port = 25565,
        username = "meme",
        password = "software_dev",
        database = "meme"
    )

    connection = database.cursor()

    #modify to create all tables that are needed
    connection.execute("Create table meme (source_text Longtext, text_id int Primary Key)")

def Insertion(text, image):
    database = mysql.connect(
        host = "localhost",
        port = 25565,
        username = "meme",
        password = "software_dev",
        database = "meme"
    )

    connection = database.cursor()

    sql_insertion_tuple = (text)
    sql_insertion_query = "Insert into meme (source_text, text_id) values (%s)"

    #inserting and commiting new row
    connection.execute(sql_insertion_query, sql_insertion_tuple)
    connection.commit()
    #need to add exceptions to rules


    connection.close()
    database.close()
