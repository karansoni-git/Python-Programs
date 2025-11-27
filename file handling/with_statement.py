''' this is a second and good way to dealing with file handling operations
syntax : with open(file, mode) as file_object_name: 

=> This line does three important things:
1. Opens the file in any mode.
2. Assigns the file object to the file_object_name variable.
3. Automatically closes the file after the with block ends, even if an error occurs inside the block. '''

with open("with_stmt.txt","w") as file_write:
    file_write.write("this line is written using (with open(file, mode) as file_object_name:)")

with open("with_stmt.txt","r") as file_read:
    print(file_read.read())
