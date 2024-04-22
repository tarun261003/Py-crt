#diamond pattern
n=int(input('Enter the size of pattern:'))
for i in range(1,n):
    print('*'*i,end='\n')
for i in range(n,0,-1):
    print('*'*i,end='\n')