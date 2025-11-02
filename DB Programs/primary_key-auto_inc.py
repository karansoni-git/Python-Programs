import mysql.connector as myConn
conn = myConn.connect(host = "localhost" , user = "root" , password = "" , database = "pytest")
cursor = conn.cursor()
cursor.execute("CREATE TABLE stud (roll INT AUTO_INCREMENT PRIMARY KEY , name VARCHAR(20)  NOT NULL, college VARCHAR(20) NOT NULL)")
print("Table created successfully!!!")
conn.commit()
cursor.close()
conn.close()
