import mysql.connector as myConn
conn = myConn.connect(host = "localhost" , user = "root" , password = "" , database = "pytest")
cursor = conn.cursor()
cursor.execute("SELECT name,college FROM stud")
rows = cursor.fetchmany(4)
for r in rows:
    print(r)

conn.close()