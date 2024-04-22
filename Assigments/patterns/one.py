#diamond pattern
n=int(input('Enter the size of pattern:'))*2
for i in range(1,n,2):
    print(' '*(n-(i+1)),end='')
    print('* '*i)
for i in range(n-1,-1,-2):
    print(' '*(n-(i+1)),end='')
    print('* '*i)