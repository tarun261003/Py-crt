L=int(input('Enter the "L" value:'))
R=int(input('Enter the "R" value'))
X=0
for i in range(L,R+1):
    X^=i
result="Even" if X%2==0 else "Odd"
print(result)