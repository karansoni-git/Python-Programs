import mysql.connector as myConn
conn = myConn.connect(host = "localhost" , user = "root" , password = "" , database = "pytest")

cursor = conn.cursor()
cursor.execute("UPDATE stud SET name = 'tirth' WHERE roll = 9")
print(cursor.rowcount , "row(s) updated")

cursor.execute("SELECT * FROM stud")
result = cursor.fetchall()
print("\nRecords after updation : ")
for r in result:
    print(r)
    
conn.commit()
cursor.close()
conn.close()
