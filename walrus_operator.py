'''
=> what is walrus operator?
-> The walrus operator := in Python (introduced in Python 3.8) allows you to assign a value to a variable as part of an expression.
-> It's officially called the assignment expression operator.
'''

# without walrus operator
l = len([1,2,3,4,5]) #here we have to find the length first
if(l > 4): #check the condition
    print("length is greater than 4")
else:
    print("length is smaller than 4")


# with walrus operator
# here the length of the list is assign first to the operator which is on the left hand side of the walrus operator
if(ans := len([1,2,43,4,4,2,3]) > 6): #than check the condition
    print(ans)
else:
    print(ans)

# walrus operator in while loop
while val := input("Enter The Keyword : ") != "exit":
    print("Enter Again!")