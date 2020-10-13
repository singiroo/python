import sqlite3

print("sqlite3")

conn = sqlite3.connect("../day13/crawlingdb.db")
cursor = conn.cursor()
sql = "delete from crawling"
data = ('12',)
cursor.execute(sql)

conn.commit()
conn.close()