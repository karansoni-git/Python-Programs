import sys

# for i in range(1,11):
#     print(i)
#     if(i == 7):
#         sys.exit()#this function will exit the script (terminate the program)

# print("loop was exited by sys.exit() function") #this will not be going to print because of sys.exit()


try:
    print("this will terminate soon!")
    sys.exit()
    print("sample code")
except :
    print("some error")
