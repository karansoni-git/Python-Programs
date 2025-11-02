# from database.connector import *
import mysql.connector as myConn
# print(dir(mysql.connector)) # shows all functions and fields.
conn = myConn.Connect(host = "localhost",
               user = "root",
               password = "",
               database = "pytest")
cursor = conn.cursor()
cursor.execute("SELECT * FROM stud") #write the sql query and execute

rows = cursor.fetchall() #fetchall() method fetch the records (returns list) and we stored it in variable
print(type(rows)) #list
print("list of tuples : ",rows) # prints all records list of tuples.
# print(cursor.fetchall()) # prints all records list of tuples.

print("\nrow[0] : ",rows[0])
print("row[2] : ",rows[2])


# first way is to store records in variable and iterate through loop.
print("\nall records : ")
for row in rows:
    print(row) #print row by row.
    
#second way is directly loop on cursor
# for i in cursor:
#     print(i)

cursor.close()
conn.close()