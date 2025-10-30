import mysql.connector as myConn
conn = myConn.connect(host = "localhost" , user = "root" , password = "" , database = "pytest")
cursor = conn.cursor()
cursor.execute("SELECT name,college FROM stud")
oneRecord = cursor.fetchone()
print(oneRecord)