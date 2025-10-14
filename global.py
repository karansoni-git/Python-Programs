'''
-> Variables that are created outside of a function are known as global variables.
-> Global variables can be used by everyone, both inside of functions and outside.
-> If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
'''
name = "karan"

def dt():
    global name #this refer to the global name variable
    name = "kirtan" #changes the value of global name variable
    print(f"my name is {name}")

print(f"before changes : {name}")
dt()
print(f"after changes : {name}")


def sample():
    global age #here we have created a variable which is global
    age = 20
    print(f"age is {age}")

sample()
print(f"age outside the function {age}")