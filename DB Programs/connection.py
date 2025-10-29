# import the mqsql.connector module here mqsql is package name and connector is class
import mysql.connector as myCon #create an alias of module as myCon
try:
    # connector class has a method called connect() and return the connection object
    conn = myCon.connect(host = "localhost",user = "root" , password = "")
    print(conn) # printing the connection object mydb
    print("Connection Established Successfully!")
except Exception as e:
     print("erroe : " ,e)