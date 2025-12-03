'''
=> __len__() is a special (dunder) method in Python.
-> It defines what happens when you call the built-in len() function on your object.

-> When you write len(obj), Python internally calls obj.__len__().
-> It must return an integer ≥ 0.
-> Used to make your custom class behave like a container (list, dict, etc.).
'''

class sample:
    def __init__(self,name):
        self.name = name
    
    def __len__(self):
        print(f"this object length is based on name variable length")
        return len(self.name)

o1 = sample("Karan Soni")
o2 = sample("Kushal patadiaya")
print(len(o1))
print()
print(len(o2))

