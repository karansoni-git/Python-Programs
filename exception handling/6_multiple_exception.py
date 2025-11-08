
try:
    a = int(input("enter a : "))
    b = int(input("enter b : "))
    d = a/b
except (ZeroDivisionError,ValueError):
    print("Some Error In Program")
else:
    print(f"division of {a}/{b} : {int(a/b)}")