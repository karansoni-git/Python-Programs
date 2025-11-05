import mysql.connector as myConn
conn = myConn.connect(host = "localhost" , user = "root" , password = "" , database = "pytest")

cursor = conn.cursor()
cursor.execute("SHOW TABLES")
for t in cursor:
    print(t)
cursor.close()
conn.close()