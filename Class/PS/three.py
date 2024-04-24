def return_frequency(s):
    d={}
    for i in s:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d
str1=input('Enter:')
d=return_frequency(str1)
print(d['z']*2==d['o'])