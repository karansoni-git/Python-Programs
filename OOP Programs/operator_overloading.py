class c1:
    def __init__(self,number):
        self.number = number

    def __add__(self,obj):
        return self.number + obj.number
    
    def __sub__(self,obj):
        return self.number - obj.number

    def __mul__(self,obj):
        return self.number * obj.number
    
    def __truediv__(self,obj):
        return self.number / obj.number

    def __floordiv__(self,obj):
        return self.number // obj.number
    
o1 = c1(60)
o2 = c1(21)

print("__add__ : " , o1 + o2)
print("__sub__ : " , o1 - o2)
print("__mul__ : " , o1 * o2)
print("__truediv__ : " , o1 / o2)
print("__floordiv__ : " , o1 // o2)