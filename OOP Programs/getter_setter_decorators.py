'''
=> getter and setter are implemented using the @property decorator.
=> They let you control attribute access in an object-oriented way—like Java-style getters & setters—but still allow dot notation (obj.attr).
'''

class sample:

    # @property → makes name behave like an attribute but actually calls the method.   
    @property
    def name(self):
        return f"firstname : {self.fname} | lastname : {self.lname}"
    
    # @name.setter → allows validation or transformation before setting.    
    @name.setter
    def name(self,val):
        self.fname = val.split(" ")[0]
        self.lname = val.split(" ")[1]

o1 = sample()
o1.name = "Karan soni"
print(o1.name)

o2 = sample()
o2.fname = "kushal"
o2.lname = "patadiya"
print(f"{o2.fname} | {o2.lname}")