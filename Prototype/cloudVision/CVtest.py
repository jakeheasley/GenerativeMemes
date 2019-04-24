import cvImageProcessor
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

# example usage for instantiating and using cvImageProcessor.CV object.


cv = cvImageProcessor.CV()

# meme = cv.open_image(input('enter a filepath: '))

cursor.execute("select photo from test;")
temp = cursor.fetchone()

blob = temp[0]
binarymeme = cv.open_blob(blob)
foo = cv.tag_image(binarymeme, 'full')

# memetext = cv.run_ocr(meme, 'text')
#
# memetags = cv.tag_image(meme, 'brief')

# print(meme)
# print(memetext)
# print(memetags)
print(foo)
db.close()
