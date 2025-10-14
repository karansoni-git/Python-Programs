# # What is a for loop?
# # A for loop in Python is used to iterate over a sequence (like a list, tuple, string, dictionary, set, or range).
# # It allows you to run a block of code multiple times.

# # for loop with range
print("for loop with range() :",end="\n")
for i in range(5):
    print("hello karan")

# # for loop with list
print("\nfor loop with list :",end="\n")
cars = ["BMW","AUDI","PORSCHE","MINI COOPER"]
for car in cars:
    print("I LOVE" , car)

# # for loop with tuple
print("\nfor loop with tuple :",end="\n")
cities = ("mumbai","ahmedabad","rajkot","surat")
for city in cities:
    print("i live in ",city)

# # for loop with string
print("\nfor loop with string :",end="")
for c in "karan soni":
    print(c.upper(),end=" ")

# for loop with enumerate
print("\n\nfor loop with enumerate :",end="\n")
for index,val in enumerate(cars,start=1):
    print(index," : ",val)

# for loop with dictionary
details = {
    "firstname" : "karan",
    "lastname" : "soni",
    "age" : 20
}
print("\nfor loop with dictionary :",end="\n")
for i in details:
    print(i," => ",details[i])

# for loop with set
print("\nfor loop with set :",end="\n")
s = {20,22,25}
for i in s:
    print(i)

# else with for loop
print("\nfor loop with else :",end="\n")
for i in range(1,4):
    print(i)
else:
    print("loop completed")
