import mysql.connector as mysql
from Login_Settings_General import Login_Settings

db = mysql.connect(host = Login_Settings.database["HOST"], port = Login_Settings.database["PORT"], user = Login_Settings.database["DB_USERNAME"],
                   passwd = Login_Settings.database["DB_PASSWORD"], database = Login_Settings.database["DATABASE"])

cursor = db.cursor()

cursor.execute("select * from ocr_similar;")

for x in cursor:
    print(x[0])
