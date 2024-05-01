t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    mod=list(filter(lambda x: x<=0,arr))
    if len(mod)<k:
        print('YES')
    else:
        print('NO')