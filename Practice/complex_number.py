class sample: 
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2

    def __add__(self,obj):
        return complex((self.n1 + obj.n1) , (self.n2 + obj.n2))

    def __mul__(self,obj):
        return complex((self.n1 * obj.n1) , (self.n2 * obj.n2))
    
o1 = sample(2,3)
o2 = sample(4,6)

print(o1+o2)
print(o1*o2)
