import cx_Oracle

print("oracle")

conn = cx_Oracle.connect("KYH/java@localhost:1521/xe")
cursor = conn.cursor()
sql = "delete from pytable where col1 = :1"
data = ('5')
cursor.execute(sql,data)
    
cursor.close()

conn.commit()
conn.close()