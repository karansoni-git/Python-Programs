class two_D:
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def show2d(self):
        print(f"dimension i :{self.i} and j : {self.j}")


class three_D(two_D):
    def __init__(self,i,j,k):
        self.k = k
        super().__init__(i,j)

    def show3d(self):
        print(f"dimension i :{self.i} and j : {self.j} and k : {self.k}")


t_d = two_D(10,20)
t_d.show2d()

th_d = three_D(40,50,60)
th_d.show2d()
th_d.show3d()