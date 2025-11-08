'''
=> what is assert statement?
The assert statement in Python is used for debugging purposes. It tests whether a condition is True. If it is, the program continues to execute. If it's False, Python raises an AssertionError, stopping the program (unless handled with try/except).

=> syntax : assert condition, optional_message
'''

# age = int(input("Enter your age : "))
# assert age > 18

# try: 
#     age = int(input("Enter your age : "))
#     assert age >= 18
# except AssertionError:
#     print("age must be greater than 18")


try: 
    age = int(input("Enter your age : "))
    assert age >= 18,"age must be greater than 18"
except AssertionError as a:
    print("error : ",a)
    print("exception argument : ",a.args)
    print("error type(class) : ",type(a))


