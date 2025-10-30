import mysql.connector as myConn
conn = myConn.connect(host = "localhost",user = "root",password = "",database = "pytest")

cursor = conn.cursor()
sqlQuery = "DELETE FROM stud WHERE roll = %s"
rollNo = input("Enter the roll no of the student which record you wnat to delete : ")
cursor.execute(sqlQuery,tuple(rollNo))
print(cursor.rowcount,"record(s) deleted")

cursor.execute("SELECT * FROM stud")
result = cursor.fetchall()
print("\nRecords after delete records : ")
for r in result:
    print(r)

conn.commit()
cursor.close()
conn.close()