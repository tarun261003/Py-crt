n=int(input('Enter the size of the rectangle:'))
for i in range(n):
    for j in range(i+1):
        print(j+1,end=' ')
    print()   