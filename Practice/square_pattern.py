# for i in range(1,4):
#     for j in range(1,4):
#         if(i == 2 and j == 2):
#             print(" ",end=" ")
#             continue
#         print("*",end=" ")
#     print()

n = int(input("Enter a number : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i == 1 or i == n):
            print("*",end="")
        else:
            if(j == 1 or j == n):
                print("*",end="")
            else:
                print(" ",end="")
    print()