import mysql.connector as myConn
conn = myConn.connect(host = "localhost", user = "root", password = "", database = "pytest")

name = input("Enter Name : ")
college = input("Enter College Name : ")
sqlQuery = "INSERT INTO stud (name , college) VALUES(%s,%s)"
sqlValues = (name,college)

cursor = conn.cursor()
cursor.execute(sqlQuery,sqlValues)
print(cursor.rowcount,"inserted successfully!")

conn.commit()
cursor.close()
conn.close()