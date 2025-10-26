# set is a built-in data type used to store unordered, unindexed, and unique elements. It is very useful when you want to remove duplicates or perform mathematical set operations like union, intersection, difference, etc.

empty_set = set()
print("empty set : ",empty_set)
print("type of empty_set : ",end="")
print(type(empty_set))

set1 = {"karan","soni",20,"mumbai"}
print("set1 :",set1)
print("type of set1 : ",end="")
print(type(set1))

# add(value) : is used to add a single element to the set.
print("add() : ",end="")
set1.add("St.xavier")
print(set1)

# update() : is used to add multiple elements (from an iterable like a list, tuple, set, etc.) to the set.
print("update() : ",end="")
set1.update(["gondal","rajkot"])
set1.update(("Amity","NIT"))
print(set1)

# remove(value) : Removes a specific element; raises KeyError if not found
print("remove() : ",end="")
set1.remove("Amity")
print(set1)

# discard(value) : Removes a specific element; no error if not found.
print("discard() : ",end="")
set1.discard("NIT")
print(set1)

# pop() : is used to remove and return an arbitrary element from the set.
print("pop() : ",end="")
print(set1.pop())

# copy() : Returns a shallow copy of the set
set_copy = set1.copy()
print("copy() : ",end="")
print(set_copy)

# clear() : Removes all elements from the set
print("clear() : ",end="")
set1.clear()
print(set1) #now it is empty bcuz we perform a clear operation on set1.

# union() : returns a new set containing all unique elements from the original set and one or more other sets.
s1 = {1,2,3}
s2 = {3,4,2,5,6}
s3 = s1.union(s2)
print("union() : ",end="")
print(s3)

# intersection() : returns a new set that contains only the elements common to all the given sets.
print("intersection() : ",end="")
s4 = s1.intersection(s2)
print(s4)

# difference() : returns a new set containing elements only present in the original set and not in the other set(s). You can also use the - operator 
print("difference() : ",end="")
s5 = s1.difference(s2)
print(s5)

# symmetric_difference() : returns a new set containing elements that are in either of the sets, but not in both.
print("symmetric_difference() : ",end="")
s6 = s1.symmetric_difference(s2)
print(s6)

# intersection_update() : modifies the original set by keeping only the elements that are common between the set and the given set(s).
# print("intersection_update() : ",end="")
# s1.intersection_update(s2)
# print(s1)

# difference_update() : removes elements from the original set that are also present in another set (or sets).
# print("difference_update() : ",end="")
# s1.difference_update(s2)
# print(s1)


# symmetric_difference_update() : updates the original set to keep only elements that are not common between the two sets.
# print("symmetric_difference_update() : ",end="")
# s1.symmetric_difference_update(s2)
# print(s1)

# issubset() : is used to check whether all elements of one set are present in another set.
print("issubset() : ",end="")
print(s1.issubset(s2))

# issuperset() : is used to check whether a set contains all elements of another set — in other words, whether it is a superset of the other set.
print("issuperset() : ",end="")
print(s1.issuperset(s2))

# isdisjoint() : checks whether two sets have no elements in common.
print("isdisjoint() : ",end="")
print({1,2,3}.isdisjoint({4,5}))


