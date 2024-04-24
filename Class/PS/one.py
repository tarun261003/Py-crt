#Aproach Using List
'''
def return_consecutive(workload):
    start=False
    temp=[]
    cons=[]
    for i in workload:
        if i>6:
            start=True
        if i<6:
            start=False
            cons.append(temp)
            temp=[]
        if start:
            temp.append(i)
    cons.append(temp)
    return cons
n=int(input('Enter the No of working days:'))
workload=list(map(int,input().split()))
rating=0
print(len(max(return_consecutive(workload),key=len)))
'''

#approach without List
'''def solve(N,workload):
    max_cons=0
    cons=0
    for i in workload:
        if i>6:
            cons+=1
            max_cons=max(cons,max_cons)
        else:
            cons=0
    return max_cons
n=int(input('Enter the No of working days:'))
workload=list(map(int,input().split()))
print(f'Rating:{solve(n,workload)}')
'''