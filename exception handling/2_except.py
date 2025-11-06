a = int(input("enter a : "))
b = int(input("enter b : "))

# The try block lets you test a block of code for errors.
try: 
    d = a/b

# The except block lets you handle the error.
except Exception as e:
    print(f"class name : {Exception}")
    print(f"Error : {e}")
    print("type of exception : ",type(e))
    print(f"using args : {e.args}")
