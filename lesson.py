import os
import time
import datetime
import shutil

now = datetime.datetime.now()
print(now)
print(now.isoformat())
print(now.strftime('%d/%m/%y-%H'))

today = datetime.date.today()
print(today)
print(today.isoformat())

t = datetime.time(hour=1, minute=10)
print(t)

print(now)
d = datetime.timedelta(weeks=1)
print(now - d)

# print('##')
# time.sleep(2)
# print('##')
print(time.time())


file_name = 'test.txt'
if os.path.exists(file_name):
    shutil.copy(file_name, "{}.{}".format(file_name, now))

with open(file_name, 'w') as f:
    f.write('test')
