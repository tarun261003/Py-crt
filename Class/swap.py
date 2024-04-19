def swap_list(lst):
    L=list(lst)
    t=[]
    for i in L:
        if len(i)!=2:
            t.append(i)
        t.append(i[::-1])
    return t
L=eval(input('Enter the list of elements:'))
l=swap_list(L)
print(l)