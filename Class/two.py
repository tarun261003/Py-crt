def get_mediain(li):
    if len(li)%2!=0:
        return li[len(li)//2]
    else:
        return (li[len(li)//2]+li[len(li)//2-1])/2
li=list(map(int,input('Enter the list with spaces').split()))
print(f'The median of {li} is {get_mediain(li)}')