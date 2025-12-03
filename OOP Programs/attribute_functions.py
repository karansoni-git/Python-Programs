class sample:
    name = "karan soni"
    def __init__(self,age):
        self.age= age 
    
    def details(self):
        print(f"my name is {self.name} and i am {self.age} years old")
    
obj = sample(20)
obj.details()

# The hasattr(object name , attribute name) − to check if an attribute exists or not. 
print(hasattr(obj,"age"))

# The getattr(object name , attribute name) − to access the attribute of object. 
print(getattr(obj,"age"))

# The setattr(object name , attribyte name , value) − to set an attribute. If attribute does not exist, then it would be created.
setattr(obj,"city","gondal")
# accessing the attribute the we have added recently
print(obj.city)

# The delattr(object name, attribute name) − to delete an attribute. 
del obj.age

# print(obj.age) #throw an error because we have deleted the age attribute from the sample class

