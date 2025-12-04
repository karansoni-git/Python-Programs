'''
Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.

what is a Class : A Class is like an object constructor, or a "blueprint" for creating objects.
A class defines what an object should look like, and an object is created based on that class.

what is an object :A real-world instance of a class.

When you create an object from a class, it inherits all the variables and functions defined inside that class.

'''

# created a class
class sample:
    # class variable attributes
    name = "karan soni"

    # class function/method attributes
    def details(self):
        print("this is sample function in sample class")
        print(f"my name is {self.name}")

s1 = sample()
s1.details()
print(f"class name : {sample}")
print(f"class address : {sample()}")
# You can modify properties on objects like this:
s1.age = 20
print(f"my age is {s1.age}")

# You can delete properties on objects by using the del keyword:
del s1.age
# print(f"my age is {s1.age}") #this will throws an error because it can not find the age variable

# You can delete objects by using the del keyword:
del s1
