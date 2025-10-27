# What is a Tuple?
# A tuple is an ordered, immutable, and iterable collection of elements. Tuples can store elements of different data types and are defined using parentheses ().
# Heterogeneous	: Can store mixed data types.

tuple1 = ("karan","soni",20,"gondal")
print("tuple() : ",tuple1)

# count(value) : Returns the number of times element value appears in the tuple.
print("count(20) : ",end="")
print(tuple1.count(20))

# index(value,start,end) : is used to find the first occurrence of a specified value in a tuple and return its index (position). Raises a ValueError if the item is not found.
print("index(gondal) : ",end="")
print(tuple1.index("gondal"))
 
#len() : returns the length of the tuple.
print("len() : ",end="")
print(len(tuple1))

# reversed() : built-in function that returns an iterator that goes through the elements in reverse order.
# It works with tuples, lists, strings, and other sequence types.
print("reversed() : ",end="")
reversed_tuple = reversed(tuple1)
print(tuple(reversed_tuple))

#indexing 
print("tuple1[3] : ",end="")
print(tuple1[3])

# slicing
print("tuple1[0:2] : ",end="")
print(tuple1[0:2])

#lopping 
print("lopping : ",end="")
for i in tuple1:
    print(i , end=" ")

print()
#membership functions
print("in : ")
print("karan" in tuple1)

print("not in : ")
print("soni" not in tuple1)

#concatenation 
print("concatenation() : ",end="")
tuple2 = ("christ","rajkot")
tuple3 = tuple1 + tuple2
print(tuple3)

# repetition 
print("repetition : ",end="")
repeated_list = tuple2 * 3
print(repeated_list)

# Built-in functions 
print("min() : ",end="")
print(min((98,82,848,12)))

print("max() : ",end="")
print(max((98,82,848,12)))

print("sum() : ",end="")
print(sum((98,82,848,12)))

print("sorted() : ",end="") #return a sorted list instead of tuple
print(sorted((98,82,848,12)))

#unpacking
a,b,c,d = tuple1
print(a,b,c,d ,sep="-")

