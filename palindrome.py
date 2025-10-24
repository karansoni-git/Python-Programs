def palindrome(n):
    sum = 0 
    while(n > 0): 
        r = n % 10
        sum = (sum * 10) + r
        n = n // 10
    return sum

num = int(input("enter a number:"))
if(num == palindrome(num)):
    print("palindrome")
else:
    print("not palindrome")