import sqlite3

print("sqlite3")

conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()
sql = "update mytable set col01 = ?, col02 = ?, col03 = ? where col01 = ?"
data = ('12', '34', '56', '4')
cursor.execute(sql,data)

conn.commit()
conn.close()