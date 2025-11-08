'''
=> What is raise in Python?
-> raise is used to manually trigger (raise) an exception.
-> It can raise built-in exceptions or custom exceptions.
-> Helps in validating conditions or signaling that something went wrong.
'''


# raise the exception
name = input("Enter Your Name : ")
age = int(input("Enter Your Age : "))

try:
    if(age < 18):
        raise ValueError
    else:
        print("Welcome to the driving license test")
except ValueError:
    print("Age is not valid for driving") 


# raise the exception with message
# name = input("Enter Your Name : ")
# age = int(input("Enter Your Age : "))

# try:
#     if(age < 18):
#         raise ValueError("Your age should be greater than 18 for driving")
#     else:
#         print("Welcome to the driving license test")
# finally:
#     print("Thank You!")


# raise the exception with message and handle it with except block
# name = input("Enter Your Name : ")
# age = int(input("Enter Your Age : "))

# try:
#     if(age < 18):
#         raise ValueError("Your age should be greater than 18 for driving")
#     else:
#         print("Welcome to the driving license test")
# except ValueError as v:
#     print(v)
# finally:
#     print("Thank You!")
