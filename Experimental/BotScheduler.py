import time
from datetime import datetime

before = datetime.now()
sum = 0
# while (True):
seconds = 5
sum = sum + 1
print(sum)
time.sleep(seconds)
after = datetime.now()

print(after-before)
