import mysql.connector as myConn
conn = myConn.connect(host = "localhost",user = "root",password = "",database = "pytest")
cursor = conn.cursor()
cursor.execute("SHOW TABLES")
print("Tables before drop : ")
for t in cursor:
    print(t)

# If the the table you want to delete is already deleted, or for any other reason does not exist, you can use the IF EXISTS keyword to avoid getting an error. 
cursor.execute("DROP TABLE IF EXISTS test") # it is better and safe to use this query.

# cursor.execute("DROP TABLE test") #this will throw an error if the table is not exist or already deleted.

cursor.execute("SHOW TABLES")
print("Tables after drop : ")
for t in cursor:
    print(t)
    