import mysql.connector as myConn
conn = myConn.connect( host="localhost", user="root", password="", database="pytest" ) 
cursor = conn.cursor() 
cursor.execute("SELECT * FROM stud") 
 
result = cursor.fetchall()
 
print("Rno\t\tName\t\tCollege") 
for x in result: 
    print("%2d %17s %18s"%(x[0],x[1],x[2])) 

cursor.close() 
conn.close()
