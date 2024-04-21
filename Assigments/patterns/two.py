#diamond pattern
n=int(input('Enter the size of pattern:'))
for i in range(n):
    print('*'*i,end='\n')
for i in range(n,-1,-1):
    print('*'*i,end='\n')