import mysql.connector as mysql
import Markov.Scrape_Markov as scrape
from pathlib import Path

class SQL:
    def __init__(self, host, port, username, password, database):
        self.host = host
        self.port = port
        self.username = username
        self.password  = password
        self.database = database
        self.handle  = ""

        self.db = mysql.connect(
            host = self.host,
            port = self.port,
            user = self.username,
            passwd = self.password,
            database = self.database
        )

        self.cursor = self.db.cursor()

    def set_handle(self,handle):
        self.handle  = handle

    def Insertion(self, list_tweets):
        temp = []
        for x in list_tweets:
            temp.append((x,self.handle))
        sql_insert = """insert ignore into content (source_text, author) values (%s,%s);"""
        self.cursor.executemany(sql_insert, temp)
        self.db.commit()

    def Query(self):
        query = """select source_text from content where author =  %s;"""
        self.cursor.execute(query, (self.handle,))
        temp = []
        for x in self.cursor:
            temp.append(x[0])
        return(temp)

    def Close(self):
        self.cursor.close()
