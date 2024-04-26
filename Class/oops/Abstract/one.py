from abc import ABC,abstractmethod
from math import pi
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Recatangle(Shape):
    def area(self,l,b):
        return l*b
class Circle(Shape):
    def area(self,radius):
        return pi*radius*radius
if __name__=="__main__":
    l,b=map(int,input('Enter the l and b of rectangle:').split())
    r=Recatangle()
    print(f'Area of the given rectangle is {r.area(l,b)}')
    r1=int(input('Enter the radius of circle:'))
    c=Circle()
    print('The area of the given circle is %.3f'%(c.area(r1)))