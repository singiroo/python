import cx_Oracle

print("oracle")

conn = cx_Oracle.connect("KYH/java@localhost:1521/xe")
cursor = conn.cursor()
sql = "select col1, col2, col3 from pytable"
cursor.execute(sql)

for row in cursor :
    for i in range(len(row)): 
        print(row[i],end="\t")
        
        
    print()
    
cursor.close()
conn.close()