class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self,b):
        return list([self.x+b.x,self.y+b.y,self.z+b.z])
    def __sub__(self,b):
        return list([self.x-b.x,self.y-b.y,self.z-b.z])
t=int(input())
for _ in range(t):
    l=list(map(int,input().split()))
    v1=Vector(*l[:3])
    v2=Vector(*l[3:])
    sum=v1+v2
    dif=v1-v2
    print(f'({sum[0]},{sum[1]},{sum[2]})',end=' ')
    print(f'({dif[0]},{dif[1]},{dif[2]})')