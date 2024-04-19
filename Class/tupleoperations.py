def add_key(l,k):
    sum=0
    for i in l:
        sum+=i[k]
    return sum
def return_maxtup(l):
    li=[]
    for i in l:
        li.append(max(i))
    return tuple(li)
if __name__=="__main__":
    L=eval(input('Enter the list of tuples:'))
    print(f"The sum of first indices is {add_key(L,0)}")
    print(f"The sum of Second indices is {add_key(L,1)}")
    print(f'The maximum elements of the tuples are:{return_maxtup(L)}')