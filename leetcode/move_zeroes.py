L=eval(input('Enter the list of elements:'))
for i in L:
    if i==0:
        L.remove(i)
print(L)