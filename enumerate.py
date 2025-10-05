# the enumerate() function is used to iterate over a sequence (like a list, tuple, or string) and get both the index and the value at the same time.
# syntax : enumerate(iterable, start=0)
# iterable: any iterable object (list, tuple, string, etc.)
# start: the index value from which the counter should start (default is 0)

#enumerate in list
print("enumerate(list) :",end="\n")
l = [11,22,33,44]
for key,val in enumerate(l):
    print(key," : ",val)

#enumearte in tuple
print("enumerate(tuple) :",end="\n")
t = ("karan","soni",20)
for key,val in enumerate(t):
    print(key," : ",val)

#enumerate in string
print("enumerate(string) :",end="\n")
for index,val in enumerate("karan",start=1):
    print(index," : ",val)