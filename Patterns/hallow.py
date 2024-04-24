def get_num(n,i,j):
    if i==0 or i==n-1 or j==0 or   j==n-1:
        return '*'
    else:
        return ' '
n=int(input('Enter the size of the pattern:'))
for i in range(n):
    for j in range(n):
        print(get_num(n,i,j),end='')
    print()