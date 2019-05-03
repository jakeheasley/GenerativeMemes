import mysql.connector as mysql
import Login_Settings
import json

db = mysql.connect(host = Login_Settings.database["HOST"], port = Login_Settings.database["PORT"], user = Login_Settings.database["DB_USERNAME"],
                   passwd = Login_Settings.database["DB_PASSWORD"], database = Login_Settings.database["DATABASE"])

cursor = db.cursor()

cursor.execute("select Tweet from Tweets;")

total_dict = {}

for x in cursor:
    if x[0] == None:
        continue
    for word in x[0].split():
        if word not in total_dict:
            total_dict[word] = 1
        else:
            total_dict[word] += 1

with open('total_dict.json','w') as f:
    json.dump(total_dict,f)
