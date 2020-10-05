import cx_Oracle

print("oracle")

conn = cx_Oracle.connect("KYH/java@localhost:1521/xe")
cursor = conn.cursor()
sql = "update pytable set col1 = :1, col2 = :2, col3 = :3 where col1=2"
data = ('5', '6', '7')
cursor.execute(sql,data)
    
cursor.close()

conn.commit()
conn.close()