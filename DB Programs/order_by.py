import mysql.connector as myConn
conn = myConn.connect(host = "localhost" , user = "root" , password = "" , database = "pytest")
cursor = conn.cursor()
cursor.execute("SELECT * FROM stud ORDER BY name ASC")
asc = cursor.fetchall()
print("Records In Ascending Order : ")
for r in asc:
    print(r)

cursor.execute("SELECT * FROM stud ORDER BY name DESC")
desc = cursor.fetchall()
print("\nRecords In Descending Order : ")
for r in desc:
    print(r)