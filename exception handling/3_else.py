a = int(input("enter a : "))
b = int(input("enter b : "))

# The try block lets you test a block of code for errors.
try:
    d = a/b

# The except block lets you handle the error.
except:
    print("somethong went wrong")
    print("can not divide by 0")

# The else block lets you execute code when there is no error.
else:
    print(f"division of {a}/{b} : {int(a/b)}")