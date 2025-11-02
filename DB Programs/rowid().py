'''
=> lastrowid : 
-> you can get the last inserted row ID (auto-increment primary key) using the lastrowid property of the cursor object.
-> cursor.lastrowid works only for INSERT queries with an AUTO_INCREMENT column.
-> For multiple inserts using executemany(), it returns the ID of the first inserted row.
-> If your table has no AUTO_INCREMENT column, lastrowid will return 0.
'''

import mysql.connector as myConn
conn = myConn.connect(host = "localhost",user="root",password="",database="pytest")
cursor = conn.cursor()
cursor.execute("INSERT INTO stud (name,college) VALUES ('jay','darshan university')")
print(cursor.rowcount,"inserted successfully!")
conn.commit()
print("row Id : " , cursor.lastrowid)
cursor.close()
conn.close()