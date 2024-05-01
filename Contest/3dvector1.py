class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def print_vector(self):
        print(tuple([self.x,self.y,self.z]))
t=int(input())
for _ in range(t):
    t=list(map(int,input().split()))
    obj=Vector(*t)
    obj.print_vector()