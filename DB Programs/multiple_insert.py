import mysql.connector as myConn
conn = myConn.connect(host = "localhost" , user = "root" , password = "" , database = "pytest")
cursor = conn.cursor()
sqlQuery = "INSERT INTO stud (name , college) VALUES (%s,%s)"
sqlValues = [("vatshal","christ"),("vedant","marwadi"),("rudra","dsu")]
cursor.executemany(sqlQuery,sqlValues)
print("row Id : " , cursor.lastrowid)
conn.commit()
cursor.close()
conn.close()