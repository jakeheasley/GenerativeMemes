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

    def insertion(self, tweet_tuple):
        sql_insert = """insert ignore into Tweets (Author, Tweet, id, tag, date_pulled, tweet_date) values (%s,%s,%s,%s,%s,%s);"""
        self.cursor.executemany(sql_insert, tweet_tuple)
        self.db.commit()

    def author_query(self, author):
        query = """select Tweet from Tweets where author =  %s"""
        self.cursor.execute(query, (author,))
        query_list = []
        for x in self.cursor:
            query_list.append(x[0])
        return query_list

    def trend_query(self, trend):
        query = """select Tweet from Tweets where tag =  %s;"""
        self.cursor.execute(query, (trend,))
        query_list = []
        for x in self.cursor:
            query_list.append(x[0])
        return query_list

    def close(self):
        self.cursor.close()
