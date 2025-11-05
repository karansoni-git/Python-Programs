import mysql.connector as myConn 
conn = myConn.connect(host = "localhost" , user = "root" , password = "" , database = "pytest")
cursor = conn.cursor()
cursor.execute("SELECT name,college FROM stud WHERE name LIKE 'k%' ")
result = cursor.fetchall()
for r in result:
    print(r)
    
cursor.close()
conn.close()