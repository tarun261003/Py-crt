def get_num(n,i,j):
    size=2*n-1
    return n-min(i,j,size-i-1,size-j-1)
<<<<<<< HEAD
n=int(input('Enter the size of the pattern:'))
for  i in range(2*n-1):
=======
n=int(input('Enter the size:'))
for i in range(2*n-1):
>>>>>>> 5b915369a1396b786d17ec176a553dffc1898525
    for j in range(2*n-1):
        print(get_num(n,i,j),end=' ')
    print()