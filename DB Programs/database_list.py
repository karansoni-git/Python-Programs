import mysql.connector as myConn
conn = myConn.connect(host = "localhost" , user = "root" , password = "")
cursor = conn.cursor()
cursor.execute("SHOW DATABASES")
for i in cursor:
    print(i)
cursor.close()
conn.close()