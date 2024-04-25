class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)
    def is_square(self):
        return self.length==self.width
rec=Rectangle(5,5)
print(f"Area of the Rectange is {rec.area()}")
print(f'Perimeter of the rectangle is {rec.perimeter()}')
print(f'The given rectangle is {"Square" if rec.is_square() else "Rectangle"}')
