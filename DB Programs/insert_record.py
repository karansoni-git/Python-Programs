import mysql.connector as myConn
conn = myConn.connect(host = "localhost" , user = "root", password = "" , database = "pytest")
cursor = conn.cursor()
cursor.execute("INSERT INTO stud (name,college) VALUES('karan','marwadi')")

# second way to insert record more efficiently.
# sqlQuery = "INSERT INTO stud (name,college) VALUES(%s,%s)"
# sqlValues = ("dhruvil","bvm")
# cursor.execute(sqlQuery,sqlValues)

print(cursor.rowcount,"inserted successfully!")
conn.commit()
cursor.close()
conn.close()