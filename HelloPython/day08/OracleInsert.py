import cx_Oracle

print("oracle")

conn = cx_Oracle.connect("KYH/java@localhost:1521/xe")
cursor = conn.cursor()
sql = "insert into pytable values(:1,:2,:3)"

for i in range(5):
    data = ('i', 'i', 'i')
    cursor.execute(sql,data)
    
cursor.close()

conn.commit()
conn.close()