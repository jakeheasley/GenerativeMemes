import mysql.connector as mysql


class SQL:
    def __init__(self, host, port, username, password, database):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.handle = ""

        self.open_connection()

    def table_setup(self):
        """This creates the tables that are later used in this file.
        Make sure that you are on a new schema."""
        try:
            self.cursor.execute("create database Memes;")
            self.cursor.execute("use Memes;")
            self.cursor.execute("create table Tweets (Author text, Tweet longtext, id bigint, trend text, date_pulled date, tweet_date date, Primary key (id));")
        except:
            print("tables are already setup")

    def insertion_tweet(self, tweet_tuple):
        """inserts a tweet into the Tweets table in the database
        @:param takes a tuple with the information (Author of tweet, Tweet text, id of Tweet,
        id of Tweet, hashtag/category of tweet, date pulled of tweet, date of tweet creation)
        """
        sql_insert = """insert ignore into Tweets (Author, Tweet, id, tag, date_pulled, tweet_date) values (%s,%s,%s,%s,%s,%s);"""
        self.cursor.executemany(sql_insert, tweet_tuple)
        self.db.commit()

    # inserts the photo with blob and returns the id of the insertion to be used for insertion similar photo method
    def insertion_photo(self, temp_blob, temp_label, temp_text):
        temp_id = self.photo_id_search(temp_label)
        self.cursor.execute("insert ignore into ocr (photo, label, id) values (%s,%s,%s);",(temp_blob,temp_label, temp_id))
        self.db.commit()
        return temp_id

    def insertion_similar_photo(self, photo_text_list, id):
        tuple_list = []
        for x in photo_text_list:
            tuple_list.append((id,x))
        sql_insert = "insert ignore into ocr_similar (photo_text, photo_id) values (%s,%s);"
        self.cursor.executemany(sql_insert, tuple_list)
        self.db.commit()

    def photo_id_search(self, label):
        sql_query = "select id from ocr where label = %s"
        self.cursor.execute(sql_query,(label,))
        temp = self.cursor.fetchone()
        if (temp == None):
            self.cursor.execute("select count(id) from ocr;")
            temp = self.cursor.fetchone()
            if temp is None:
                return 0
        return temp[0]

    def author_query(self, author):
        """returns list of tweets based on the author of the tweet
        @:param takes the handle of author of Twitter (without @ just string)
        @:return a list of tweets which are strings to be proccessed
        """
        query = """select Tweet from Tweets where author =  %s"""
        self.cursor.execute(query, (author,))
        query_list = []
        for x in self.cursor:
            query_list.append(x[0])
        return query_list

    def tag_query(self, tag):
        """returns list of tweets that based on their tag
        @:param the tag of tweet that was inserted into database
        @:return a list of tweets that have associated tag in database
        """
        query = """select Tweet from Tweets where tag =  %s;"""
        self.cursor.execute(query, (tag,))
        query_list = []
        for x in self.cursor:
            query_list.append(x[0])
        return query_list

    # returns list of photo_text from a photo_label
    def ocr_label_query(self,photo_label):
        query_list = []
        query = "select id from ocr where label = %s;"
        self.cursor.execute(query,(photo_label,))
        temp = self.cursor.fetchone()
        if temp is not None:
            query = "select photo_text from ocr_similar where photo_id = %s"
            self.cursor.execute(query, (temp[0],))
            for x in self.cursor:
                query_list.append(x[0])

        return query_list

    # returns the blob for the photo to recreate the photo
    def blob_query(self, photo_label):
        query = "select photo from ocr where label = %s"
        self.cursor.execute(query,(photo_label,))

    def open_connection(self):
        """opens connection to database and cursor, used after closing and
        initializing of SQL object"""
        self.db = mysql.connect(
            host=self.host,
            port=self.port,
            user=self.username,
            passwd=self.password,
            database=self.database
        )

        self.cursor = self.db.cursor()

    def close(self):
        """suggested to close connections to cursor and database after querying"""
        self.cursor.close()
        self.db.close()
