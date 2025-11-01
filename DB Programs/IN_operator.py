import mysql.connector as myConn
conn = myConn.connect(host = "localhost",user = "root",password = "",database = "pytest")
cursor = conn.cursor()
cursor.execute("SELECT * FROM stud WHERE college IN('marwadi')")
result = cursor.fetchall()
for r in result:
    print(r)

cursor.close()
conn.close()