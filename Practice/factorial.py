# num = int(input("Enter a number : "))
# factorial = 1
# for i in range(1,num+1):
#     factorial = factorial * i
# print(f"factorial of {num} is {factorial}")


def rec(n):
    if(n==1):
        return (n)
    else:
        return n * rec(n-1)
    
num = int(input("enter a number:"))
print(f"Factorial of {num} : {rec(num)}")

