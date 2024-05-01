def find_element(l,target):
    l.sort()
    low=0
    high=len(l)-1
    mid=0
    while low<=high:
        mid=(low+high)//2
        if l[mid]==target:
            return mid
        elif l[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return "Not found"
l=list(map(int,input().split()))
target=int(input())
print(find_element(l,target))