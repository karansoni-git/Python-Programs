try:
    a = int(input("enter a : "))
    b = int(input("enter b : "))

    d = a/b
except ValueError as v:
    print("value error : ",v)
except ZeroDivisionError as z:
    print("zero error : ",z)
else:
    print(f"Division of {a}/{b} : {a/b}")