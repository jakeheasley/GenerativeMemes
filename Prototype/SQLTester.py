import mysql.connector as mysql
from datetime import datetime
from SQL import SQL

sql = SQL(host = "softwaredev.caybzpwuhc8n.us-east-2.rds.amazonaws.com", port = 6666, username = "root", password = "paulsmemes",database = "Memes")
handle = "Test"
sql.set_handle(handle)
sql.Insertion(["This is a test","This is a test 2"])
temp = sql.Query()
print(temp)
sql.Close()
