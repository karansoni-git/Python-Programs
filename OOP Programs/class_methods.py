'''
=> class methods are methods that are bound to the class, not the instance. They work with the class itself rather than a specific object.
=> They are defined using the @classmethod decorator, and by convention, the first parameter is called cls (referring to the class).
'''

class myClass:
    currentYear = 2025

    @classmethod #this decorator is used to bind property to the class so it will be common for all instance of class
    def sample(cls):
        print(f"we are living in {cls.currentYear}")
    
o = myClass()
print(f"class value of currentYear variable: {o.currentYear}")
o.currentYear = 2030
print(f"object value of currentYear variable: {o.currentYear}")
o.sample()
        