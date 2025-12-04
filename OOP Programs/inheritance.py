'''
=> Inheritance allows us to define a class that inherits all the methods and properties from another class.
-> Parent class is the class being inherited from, also called base class.
-> Child class is the class that inherits from another class, also called derived class.
'''

class parent:
    def __init__(self,fname,lname,college):
        self.fname = fname
        self.lname = lname
        self.college = college
    
    def printDetails(self):
        print(f"i am {self.fname} {self.lname} studying in {self.college} University")

    # this means this function is belonging to the class.
    @staticmethod #this decorator/keyword is used to make the function static.
    def example():
        print("Hey, I am in the parent class")
    
class child(parent):
    def __init__(self, fname, lname):
        self.college = "Marwadi"
        super().__init__(fname, lname,self.college)
        super().example()

    def sample(self):
        print("Hey, I am i the child class")

c = child("Karan","Soni")
c.printDetails()
c.sample()
print(f"i am a student of {c.college} university")

# The isinstance() function is used to check the type of an object.
# The isinstance(object , Class) boolean function returns true if obj is an instance of class Class or is an instance of a subclass of Class. 
print("isinstance(c,child) : ",isinstance(c,child))
print("isinstance(c,parent) : ",isinstance(c,parent))

# The issubclass() function checks if a class is a subclass of another class or a tuple of classes.
print("issubclass(child,parent) : ",issubclass(child,parent))