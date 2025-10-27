'''
=> type definition generally refers to how you specify, create, or annotate types. Since Python is dynamically typed, you don’t have to define types explicitly, but you can for clarity, debugging, and static analysis.
'''

x: int = 10     # integer  
y: float = 3.14     # float  
name: str = "Karan" # string  
flag: bool = True   # boolean  
items: list = [1, 2, 3]
data: dict = {"a": 1}

# Here, the : type is a type hint.

def sample(name:str , age: int) -> str:
    return f"my name is {name} and i am {age}"

# name: str → expects a str
# age: int → expects an int
# -> str → function returns a str

print(sample("karan",20))



