import sqlite3

# conn = sqlite3.connect('test_sqlite.db')
# 何度も使いたいときにこちらを記述
conn = sqlite3.connect(':memory:')

curs = conn.cursor()
# テーブルを作る
curs.execute(
    'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT,name STRING)'
)
conn.commit()

データを入れる
curs.execute(
    'INSERT INTO persons(name) values("Mike")'
)
conn.commit()
curs.execute(
    'SELECT * from persons'
)
print(curs.fetchall())

curs.execute(
    'INSERT INTO persons(name) values("Nancy")'
)
conn.commit()

curs.execute(
    'INSERT INTO persons(name) values("Jun")'
)
conn.commit()
curs.execute(
    'UPDATE persons set name ="Michel" WHERE name="Mike"'
)

curs.execute('DELETE FROM persons WHERE name="Michel"')
conn.commit()

curs.execute(
    'SELECT * from persons'
)
print(curs.fetchall())


conn.close()
