t=int(input('Enter the no of test cases:'))
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()[:n]))
    count=0
    for i in range(n):
        for j in range(n):
            if i!=j:
                if arr[i]^j==arr[j]^i:
                    count+=1
    print(count)