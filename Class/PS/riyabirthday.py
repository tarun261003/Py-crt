t=int(input('No of testcases:'))
for i in range(t):
    n=int(input())
    print((n*(2*n-1))%(10**9+7))      