list1 = ["karan",20,"gondal","bca"]
print("list1 : ",end="")
print(list1)
# append(value) : is used with lists to add a single item to the end of the list.
print("append(sem5) : ",end="")
list1.append("sem5")
print(list1)

# extend() : is used with lists to add multiple items from another iterable (like a list, tuple, set) to the end of the list.
list2 = ["ty","christ college"]
print("list2 : ",end="")
print(list2)
list1.extend(list2)
print("extend() : ",end="")
print(list1)

# insert(index, value) : is used to add an item at a specific position in a list.
print("insert(1,parekh) : ",end="")
list1.insert(1,"parekh")
print(list1)

# remove(value) : is used to delete the first occurrence of a specified value from a list.
print("remove(ty) : ",end="")
list1.remove("ty")
print(list1)

# pop(index) : Removes and returns the element at index i. remove last element if index is not mentioned
print("pop() : ",end="")
list1.pop()
print(list1)
print("pop(2) : ",end="")
list1.pop(2)
print(list1)

# clear() : is used to remove all elements from a list, making it an empty list.
print("clear() ",end="\n")
list2.clear()
print("list2 : ",end="")
print(list2)

# index(value,start,end) : is used to find the first occurrence of a specified value in a list and return its index (position). Raises a ValueError if the item is not found.
print("index(gondal) : ",end="")
print(list1.index("gondal"))

# count() : is used to count how many times a specific value appears in a list.
print("count(bca) : ",end="")
print(list1.count("bca"))

# sort(key=None optional, reverse=(True or False) optional) : is used to sort the elements of a list in place
print("sort() : ",end="")
list1.sort()
print(list1)
# sort + reverse list
print("sort(reverse=True) : ",end="")
list1.sort(reverse=True)
print(list1)

# reverse() : Reverses the elements of the list in place.
print("reverse() : ",end="")
list1.reverse()
print(list1)

# copy() : Returns a shallow copy of the list.
print("copy() : ",end="")
copy_list1 = list1.copy()
print(copy_list1)

# sorted() : sort a the elements of list,tuple or any sequences of numbers
print("sorted() : ",end="")
print(sorted(list1))