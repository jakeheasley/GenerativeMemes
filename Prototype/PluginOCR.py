import Login_Settings
import SQL
import cloudVision.cvImageProcessor as CV
import mysql.connector as mysql


cloud_vision = CV.CV()
binary_data = 0
with open("pikachu.jpg",'rb') as file:
    binary_data = file.read()

binary_meme = cloud_vision.open_blob(binary_data)
temp = cloud_vision.tag_image(binary_meme,'full')
print(binary_meme)

sql = SQL.SQL(host=Login_Settings.database['HOST'],
          port=Login_Settings.database['PORT'],
          username=Login_Settings.database['DB_USERNAME'],
          password=Login_Settings.database['DB_PASSWORD'],
          database=Login_Settings.database['DATABASE'])

temp = sql.insertion_photo(binary_data,"suprised pikachu meme","testing")
sql.insertion_similar_photo(["testing 1","testing 2"],temp)
