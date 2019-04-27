import mysql.connector as mysql

#SQl class for interacting with the MYSQL database
class SQL:
    #intializing and connecting to database
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

    #inserting tweets tuples into MYSQL
    def insertion_tweets(self, tweet_tuple_list):
        sql_insert = """insert ignore into Tweets (Author, Tweet, id, trend, date_pulled, tweet_date) values (%s,%s,%s,%s,%s,%s);"""
        self.cursor.executemany(sql_insert, tweet_tuple)
        self.db.commit()

    #inserts the photo with blob and returns the id of the insertion to be used for insertion similar photo method
    def insertion_photo(self, temp_blob, temp_label, temp_text):
        temp_id = self.photo_id_search(temp_label)
        self.cursor.execute("insert ignore into ocr (photo, label, id) values (%s,%s,%s);",(temp_blob,temp_label, temp_id))
        self.db.commit()
        return(temp_id)

    def insertion_similar_photo(self, photo_text_list, id):
        tuple_list = []
        for x in photo_text_list:
            tuple_list.append((id,x))
        sql_insert = "insert ignore into ocr_similar (photo_text, photo_id) values (%s,%s);"
        self.cursor.executemany(sql_insert, tuple_list)
        self.db.commit()

    #helper method with finding correct id for label
    def photo_id_search(self, label):
        sql_query = "select id from ocr where label = %s"
        self.cursor.execute(sql_query,(label,))
        temp = self.cursor.fetchone()
        if (temp == None):
            self.cursor.execute("select count(id) from ocr;")
            temp = self.cursor.fetchone()
            if (temp == None):
                return(0)
        return(temp[0])

    #query tweets from database based on author's handle
    def author_query(self, author):
        query = """select Tweet from Tweets where author =  %s"""
        self.cursor.execute(query, (author,))
        query_list = []
        for x in self.cursor:
            query_list.append(x[0])
        return query_list

    #query tweets where the tag is passed as parameter
    def tag_query(self, trend):
        query = """select Tweet from Tweets where tag =  %s;"""
        self.cursor.execute(query, (trend,))
        query_list = []
        for x in self.cursor:
            query_list.append(x[0])
        return query_list

    #returns list of photo_text from a photo_label
    def ocr_label_query(self,photo_label):
        query_list = []
        query = "select id from ocr where label = %s;"
        self.cursor.execute(query,(photo_label,))
        temp = self.cursor.fetchone()
        if (temp != None):
            query = "select photo_text from ocr_similar where photo_id = %s"
            self.cursor.execute(query, (temp[0],))
            for x in self.cursor:
                query_list.append(x[0])

        return(query_list)

    #returns the blob for the photo to recreate the photo
    def blob_query(self, photo_label):
        query = "select photo from ocr where label = %s"
        self.cursor.execute(query,(photo_label,))

    # testes whether the current query has returned nothing
    def query_test(self):
        # currently in thought process
        a = 2
    #closes connection with database do so when done with object
    def close(self):
        self.cursor.close()
