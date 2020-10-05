import sqlite3

print("sqlite3")

conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()
sql = "insert into mytable values(?, ?, ?)"
data = ('5', '6', '7')
cursor.execute(sql,data)

conn.commit()
conn.close()