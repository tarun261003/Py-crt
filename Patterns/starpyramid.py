n=int(input('Enter the size:'))*2
for i in range(1,n,2):
    print(' '*(n-i),end='')
    for j in range(i):
        print('*',end=' ')
    print()     