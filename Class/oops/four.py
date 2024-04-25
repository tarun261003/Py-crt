# a=complex(4,5)
# b=6+7j
# print(a+b)
# print(a-b)
# print(a*b)
class Complex:
    def __init__(self,Z1,Z2):
        self.Z1=Z1
        self.Z2=Z2
    def add_complex(self):
        return self.Z1+self.Z2
    def subtract_complex(self):
        return self.Z1-self.Z2
    def product_complex(self):
        return self.Z1*self.Z2
if __name__=="__main__":
    a,b=map(int,input('Enter the Complex 1:').split())
    z1=complex(a,b)
    c,d=map(int,input('Enter the Complex 2:').split())
    z2=complex(c,d)
    com=Complex(z1,z2)
    print(f'The addition of "{z1}" and "{z2}" is "{com.add_complex()}"')
    print(f'The subtraction of "{z1}" and "{z2}" is "{com.subtract_complex()}')
    print(f'The product of "{z1}" and "{z2}" is "{com.product_complex()}"')