import mysql.connector as mysql

mydb = mysql.connect(
    host = "softwaredev.caybzpwuhc8n.us-east-2.rds.amazonaws.com",
    port = 6666,
    user = "root",
    passwd = "paulsmemes",
    database = "Memes"
)

cursor = mydb.cursor()

cursor.execute("select * from content;")
temp = cursor.fetchall()
print(temp[1])
