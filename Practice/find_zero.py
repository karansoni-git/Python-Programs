t1 = (10,48,0,84,238,0,13,0)
count = 0
for i in t1:
    if i == 0:
        count+=1
print("count(0) :",count)

#find occurence of 0 through count function 
print("count(0) : ",end="")
print(t1.count(0))