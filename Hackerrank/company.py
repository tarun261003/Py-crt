def return_frequency(s):
    d={}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i]+=1
    temp={}
s=input('Enter the string:')
d1=return_frequency(s)
keys=list(d1.keys())
vals=list(d1.values())
vals.sort()
sorted_dic={i :d1[i] for i in vals}
print(sorted_dic)