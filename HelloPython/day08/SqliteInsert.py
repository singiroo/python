import sqlite3

print("sqlite3")

#Autocommit 사용자:

conn = sqlite3.connect("mydb.db", isolation_level=None)

cursor = conn.cursor()
sql = "insert into mytable values(?, ?, ?)"
data = ('5', '6', '7')
cursor.execute(sql,data)

#conn.commit()

conn.close()