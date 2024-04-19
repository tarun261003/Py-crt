def max_of_three(arr):
    temp=sorted(arr,reverse=True)
    print('largest number is:',temp[0])
    sum=0
    for i in temp:
        sum+=i
    print('The sum is:',sum)
arr=list(map(int,input().split()))
max_of_three(arr) 