import mysql.connector as myConn
conn = myConn.connect(host = "localhost" , user = "root" , password = "" , database = "pytest")
cursor = conn.cursor()
cursor.execute("SELECT name,college FROM stud LIMIT 5")
result = cursor.fetchall()
print("First 5 Records : ")
for r in result:
    print(r)

print("\n5 Records start from index 3 : ")
cursor.execute("SELECT name,college FROM stud LIMIT 3 OFFSET 2")
positionalResult = cursor.fetchall()
for r in positionalResult:
    print(r)