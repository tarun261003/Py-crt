a=["flower","flow","flight"]
one=a[0]
subs=sorted([one[i:j] for i in range(len(one)) for j in range(i+1,len(one))],key=len)
print(subs)
