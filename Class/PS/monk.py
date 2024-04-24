from math import gcd,prod,pow  
N=int(input())
L=list(map(int,input().split()))
F=prod(L)
G=gcd(*L)
Quo=pow(10,9)+7
print(int(pow(F,G)%Quo)) 