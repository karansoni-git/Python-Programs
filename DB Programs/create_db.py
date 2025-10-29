'''
=> What is cursor() and what it does :
    1. it is created on connection object connectionObject.cursor().
    2. It creates and returns a cursor object from the database connection.
    3. The cursor acts like a pointer/handle that allows you to:
        -> Execute SQL queries (SELECT, INSERT, UPDATE, DELETE, etc.).
        -> Fetch results from the database (fetchone(), fetchall(), etc.).
        -> Manage the context of a query execution.
    4. The cursor object is an important aspect of executing queries to the databases.         
    5. You can create multiple cursors from a single connection.
    6. Cursors should be closed after use to free resources.
    7. operations that cursor object can do :
        -> Execute SQL queries → (execute(), executemany())
        -> Fetch query results → (fetchone(), fetchall(), fetchmany())
        -> Control transactions → (commit(), rollback()) through the connection 
'''
import mysql.connector as myCon

conn = myCon.connect(host = "localhost" , user = "root" , password = "")
my_cursor = conn.cursor()
my_cursor.execute("CREATE DATABASE PyTest")
my_cursor.close()
conn.commit()
my_cursor.close() # closing the cursor object.
conn.close() # closing the conn object.
print("Database created succesfully!!")