import sqlite3

print("sqlite3")

conn = sqlite3.connect("../day13/crawlingdb.db")
cursor = conn.cursor()
sql = "select * from crawling"
cursor.execute(sql)

for row in cursor:
    for i in range(len(row)):
        print(row[i],end="\t")

    print()
    

conn.close()