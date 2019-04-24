import Login_Settings
import mysql.connector as mysql


# print(Login_Settings.database)
db = mysql.connect(host=Login_Settings.database['HOST'],
          port=Login_Settings.database['PORT'],
          user=Login_Settings.database['DB_USERNAME'],
          password=Login_Settings.database['DB_PASSWORD'],
          database=Login_Settings.database['DATABASE'],
          use_pure = True
          )

cursor = db.cursor()

binaryData = 0

with open('robot.jpg','rb') as file:
    binaryData = file.read()
    cursor.execute("insert ignore into test (photo) values (%s);",(binaryData,))
    db.commit()


cursor.execute("select * from test;")

temp = cursor.fetchone()
#
with open('test.jpg', 'wb') as file:
    file.write(temp[1])
