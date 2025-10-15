'''
=> What is a Lambda Expression?
-> A lambda is an anonymous (nameless) function in Python.
-> It is a one-line function used for simple operations.
-> It can have any number of arguments but only one expression.
-> It returns the value of the expression automatically (no return keyword needed).
=> syntax : variable_name = lamda arguments : expression
'''
greeting = lambda : "Hello Coder"
add = lambda a,b : a+b
sub = lambda a,b : a-b
mul = lambda a,b : a*b
div = lambda a,b : a/b
mod = lambda a,b : a%b

print(greeting())
print(f"Addition : {add(10,4)}")
print(f"Subtraction : {sub(30,3)}")
print(f"Multiplication : {mul(8,7)}")
print(f"Division : {div(100,2)}")
print(f"Modulus : {mod(740,36)}")