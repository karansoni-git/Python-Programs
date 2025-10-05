# What is a Dictionary?
# a dictionary is a built-in data type used to store key-value pairs.
# It is unordered, mutable, and indexed by keys.

empty_dict = {}
# print(type(empty_dict))

details = {
    "name" : "karan",
    "age" : 20,
    "city" : "mumbai",
    "college" : "christ"
}

#accessing value : 
# first way
print("details[\"name\"] : ",end="")
print(details["name"]) #return value of key if exists otherwise returns an error

# second way
# get(key, fallback-statement(optional)) : Returns the value for the key if it exists; otherwise returns None
print("get(\"age\") : ",end="")
print(details.get("age","not found that key"))

# keys() : is used to get a view object that displays a list of all the keys in a dictionary.
print("keys() : ",end="")
print(details.keys())

# values() : returns a view object that displays a list of all the values in the dictionary.
print("values() : ",end="")
print(details.values())

# copy() : is used to create a shallow copy of a dictionary.
# does not affect the opriginal dictionary
print("copy() : ",end="")
copy_details = details.copy()
print(copy_details)

# items() : Returns a view object with all key-value pairs as tuples
print("items() : ",end="")
print(details.items())

# pop(key, fallback statement(optional)) : is used to remove a key from the dictionary and return its value.
print("pop() : ",end="")
print(details.pop("age","not exist")) #second argument run when the key not found

# popitem() : is used to remove and return the last inserted key-value pair from the dictionary
print("popitem() : ",end="")
print(details.popitem())

# update() : is used to add key-value pairs from one dictionary to another. If the key already exists, its value is updated. If not, a new key-value pair is added.
print("update() : ",end="")
details.update(lastname = "soni" ,college = "marwadi")
print(details)


# fromkeys(sequence, value) : Creates a new dictionary with keys from seq and values set to value (default is None)
print("dict.fromkeys() : ",end="")
keys = ["FirstName","LastName","Age","City"]
newDict = dict.fromkeys(keys,"Empty")
print(newDict)

# setdefault() : is used to get the value of a key, and if the key does not exist, it adds the key with a specified default value.
print("setdefault() : ",end="")
print(details.setdefault("height","5,8"))
print(details)

# clear() : Removes all items from the dictionary
print("clear() : ",end="")
newDict.clear()
print(newDict)

# removing item
print("del dict_name[key] ",end="")
del details["height"]
print("\nafter deletetion : ",end="")
print(details)

# adding items
details["height"] = "5,8"
print("after adding item: ",end="")
print(details)

# looping through dictionary
print("all keys : ",end="")
for key in details.keys():
    print(key,end=", ")

print("\nall values : ",end="")
for val in details.values():
    print(val,end=", ")

print("\nwhole dictionary : ",end="\n")
for i in details:
    print(i," - ",details[i])

print("\nall key - value pairs : ",end="\n")
for key,val in details.items():
    print(key," : ",val)

#len() : returns the length of the dictionary
print("len() : ",end="")
print(len(details))