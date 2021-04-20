class C2dVec:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j
        print(self.icap ,self.jcap)

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

class C3dVec(C2dVec):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k
        print(self.icap ,self.jcap,self.kcap)
    
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
    
    
v2d = C2dVec(1, 3)
v3d = C3dVec(1, 9, 7)
# print(v2d)
# print(v3d)
