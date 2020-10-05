import cx_Oracle

print("oracle")

conn = cx_Oracle.connect("KYH/java@localhost:1521/xe")
cursor = conn.cursor()
sql = "insert into pytable values(:1,:2,:3)"
data = ('3', '3', '3')
cursor.execute(sql,data)
    
cursor.close()

conn.commit()
conn.close()