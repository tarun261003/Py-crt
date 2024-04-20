n=int(input('Enter the size:'))*2
for i in range(n-1,0,-2):
    print(' '*(n-i),end='')
    for j in range(i):
        print('*',end=' ')
    print()