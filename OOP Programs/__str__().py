'''
=> the __str__() method is a special (magic/dunder) method that defines how an object is converted to a string (what you see when you print it).
=> The __str__() function controls what should be returned when the class object is represented as a string.

-> It returns a human-readable string representation of the object.
-> When you use print(obj) or str(obj), Python internally calls obj.__str__().
'''

# Example without __str__
class normal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __len__(self):
        return 10   

# Example with __str__
class str:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Object has name : {self.name} and age : {self.age}"

first = normal("karan",20)
print("String representation without __str__() : ",first)

second = str("Karan",20)
print("String representation with _str__() : ",second)



# class sample:

#     def ex(self):
#         return sample() #here we calling the class
#     # this sample() call the class __str__() method which represent the string format of class
    
#     def __str__(self):
#         return  "string format of sample class"


# o1 = sample()
# o2= sample()

# print(o1.ex())
# print(o2.ex())
