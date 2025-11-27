''' 
=> File handling in Python is an essential concept used to read, write, append, and manipulate files on your system.

=> open() Function : is used to open a file in Python.
It returns a file object, which lets you read, write, or modify the file.
syntax : open(filename,mode)
full syntax : open(file, mode, buffering, encoding, errors, newline, closefd, opener)

=> mode : 
'r' : Read (default)                    
'w' : Write (overwrite)                 
'a' : Append                            
'x' : Create and write (error if exists)
'b' : Binary mode                       
't' : Text mode (default)               
'+' : Read & write '''

list_of_lines = ["sample 1\n","sample 2\n","sample 3\n"]

# file is the file object returned by open().
# open file in write mode
file = open("written_file.txt","w")

# write() : is used to write a string to a file.
file.write("This is a smaple file which is an example of file writing\n")
file.write("Karan soni,\n")
file.write("Thank you\n")

# The writelines() method is used to write a list of strings to a file.
file.writelines(list_of_lines)

# The close() method is used to close an open file in Python. Once a file is closed, you can no longer read from or write to it.
file.close()

# open file in append mode
file2 = open("written_file.txt","a")
file2.write("open file once again in append mode and add some text")
file2.close()

# can't write in file after closing it
# file2.write("is it possible to write after closing the file")

print("File written successfully")
