import sqlite3

print("sqlite3")

conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()
sql = "select col01, col02, col03 from mytable"
cursor.execute(sql)

for row in cursor:
    for i in range(len(row)):
        print(row[i],end="\t")

    print()
    

conn.close()