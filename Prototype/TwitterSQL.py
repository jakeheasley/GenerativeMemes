import mysql.connector as mysql
import Markov.Scrape_Markov as scrape
from pathlib import Path

#method for inserting into the database
def Insertion(handle):
    #connect to database
    mydb = mysql.connect(
        host = "softwaredev.caybzpwuhc8n.us-east-2.rds.amazonaws.com",
        port = 6666,
        user = "root",
        passwd = "paulsmemes",
        database = "Memes"
    )

    mycursor = mydb.cursor()

    scrape.get_all_tweets(handle)
    data = scrape.return_tweets()
    sql_insert = """insert ignore into content (source_text, author) values (%s,%s);"""
    mycursor.executemany(sql_insert, data)
    mydb.commit()
    mycursor.close()

def Query(handle):
    #connect to database
    mydb = mysql.connect(
        host = "softwaredev.caybzpwuhc8n.us-east-2.rds.amazonaws.com",
        port = 6666,
        user = "root",
        passwd = "paulsmemes",
        database = "Memes"
    )

    mycursor = mydb.cursor()
    query = """select source_text from content where author =  %s;"""
    mycursor.execute(query, (handle,))


    #do not know if should make everytime we query or just when it is empty
    Insertion(handle)

    with open("query.txt", "w+",encoding = "utf-8") as f:
        for x in mycursor:
            f.write(x[0]+"\n")

    file_name = "query.txt"
    base_path = Path(file_name).parent
    file_path = (base_path / file_name).resolve()
    mycursor.close()
    return file_path
