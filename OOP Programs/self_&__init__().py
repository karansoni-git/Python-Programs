'''
=> what is self parameter in function : The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
-> When you call a method on an object, Python automatically passes that object itself as the first argument to the method—by convention.
-> It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class

----------------------------------------------------------------------------------------------------------------

=> what is __init__() : __init__() is a special method (also called a constructor) that initializes an object when it is created from a class.

=> How __init__() Works
-> It runs automatically whenever you create an object.
-> It always has at least self as the first parameter.
-> You can pass extra arguments to set initial values.

-> The __init__() function is called automatically every time the class is being used to create a new object.
'''

class sample:

    def __init__(self,name,company):
        self.name = name
        self.company = company

    def details(self):
        company = "Google"
        print(f"my name is {self.name} and i work at {self.company}")
        print(f"But his dream is to go in {company}")

o1 = sample("Karan","Microsoft")
o2 = sample("Kushal","Deloitte")

o1.details()
o2.details()
