import mysql.connector as mysql

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

    def insertion(self, list_tweets):
        temp = []
        for x in list_tweets:
            temp.append((x,self.handle))
        sql_insert = """insert ignore into content (source_text, author) values (%s,%s);"""
        self.cursor.executemany(sql_insert, temp)
        self.db.commit()

    def author_query(self, author):
        query = """select source_text from content where author =  %s"""
        self.cursor.execute(query, (author,))
        query_list = []
        for x in self.cursor:
            query_list.append(x[0])
        return query_list

    def trend_query(self, trend):
        query = """select source_text from content where trend =  %s;"""
        self.cursor.execute(query, (trend,))
        query_list = []
        for x in self.cursor:
            query_list.append(x[0])
        return query_list

    def close(self):
        self.cursor.close()
