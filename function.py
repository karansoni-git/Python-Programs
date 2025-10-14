def sample():
    # the below line is a documentation of the function
    "sample code inside the function"
    print("this is sample function")
    print("Thank You!")
sample()
# accessing the documentation of the function through __doc__
print(sample.__doc__)


# normal function
def avg():
    a = int(input("Enter first number : "))
    b = int(input("Enter secon1d number : "))

    avg = (a + b)/2
    print(f"average of {a} and {b} is {avg}")
avg()

#argument in function 
def greeting(name):
    print(f"Hello, {name}")
greeting("Karan")
greeting("kirtan")

#returning a value from function
def sum(num1,num2):
    sum = num1 + num2
    return sum
s = sum(20,20)
print(f"sum : {s}")

#default parameter in function
def default(name,closure="thank you"):
    print(f"hello, {name}")
    print(closure)
default("Karan")
default("Abhay","bye bye")