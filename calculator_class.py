import math

class calculator:
    def __init__(self,number):
        self.number = number
        self.square()
        self.cube()
        self.square_root()

    def square(self):
        print(f"square of {self.number} : {self.number**2}")
    
    def cube(self):
        print(f"cube of {self.number} : {self.number**3}")

    def square_root(self):
        print(f"square root of {self.number} : {round(math.sqrt(self.number),2)}")

    @staticmethod
    def greeting():
        print("Hello Python Code")

calculator.greeting()
print("\nfirst number : ")
num1 = calculator(10)
print("\nsecond number : ")
num2 = calculator(5)