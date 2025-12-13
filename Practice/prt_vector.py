class sample:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
    
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
o = sample(5,7,10)
print(o)