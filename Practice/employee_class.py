class employee:
    company = "Microsoft"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    def details(self):
        print(f"Employee name {self.name} and Salary {self.salary} Work at {self.company}")
    
emp1 = employee("karan",400000)
emp4 = employee("vedant",600000)

emp1.details()
emp4.details()
