def return_number(i,j):
    if i==0 or i==2*n-2 or j==0 or   j==2*n-2:
        return n

    elif i==n-1 and j==n-1:
        return 1
    else:
        return '*'
n=int(input('Enter the size:'))
for i in range(2*n-1):
    for j in range(2*n-1):
        print(return_number(i,j),end=' ')
    print()