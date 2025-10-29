import mysql.connector as d

conn = d.connect(
    host="localhost",
    user="root",
    password="",
    database="pytest"
)

cursor = conn.cursor()
cursor.execute("CREATE TABLE test( rollno INT(20) , name VARCHAR(20) , course varchar(20) , college varchar(30))")
conn.commit()
cursor.close()
conn.close()
print("table created successfully!!!")