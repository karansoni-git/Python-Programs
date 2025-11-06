'''
=> What is a try-except block?
-> A try-except block is used for exception handling in Python.
-> It allows you to catch runtime errors and handle them gracefully, instead of crashing the program.
'''
a = int(input("enter a : "))
b = int(input("enter b : "))

# The try block lets you test a block of code for errors.
try:
    d = a/b
except: #The except block lets you handle the error.
    print("somethong went wrong")
    print("can not divide by 0")
