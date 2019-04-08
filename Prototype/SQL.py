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

    def Insertion(self):
        scrape.get_all_tweets(self.handle)
        data = scrape.return_tweets()
        sql_insert = """insert ignore into content (source_text, author) values (%s,%s);"""
        self.cursor.executemany(sql_insert, data)
        self.db.commit()

    def Query(self):
        query = """select source_text from content where author =  %s;"""
        self.cursor.execute(query, (self.handle,))
        

        #Should we insert everytime to make sure that there is source stuff from that author/handle?

        with open("query.txt", "w+",encoding = "utf-8") as f:
            for x in self.cursor:
                f.write(x[0]+"\n")

        file_name = "query.txt"
        base_path = Path(file_name).parent
        file_path = (base_path / file_name).resolve()
        return file_path



    def Close(self):
        self.cursor.close()
