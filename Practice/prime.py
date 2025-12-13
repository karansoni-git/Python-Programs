num = int(input("Enter a number : "))
c = 0
for i in range(2,num):
    if(num % i == 0):
        c += 1
if(c >= 1):
    print(f"{num} is not prime")
else:
    print(f"{num} is prime")