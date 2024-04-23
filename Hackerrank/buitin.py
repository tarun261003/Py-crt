import string
l=string.ascii_lowercase
u=string.ascii_uppercase
d=string.digits
s=input('Enter the string:')
lower=[]
upper=[]
digits=[]
odd=[]
eve=[]
for i in s:
    if i in l:
        lower.append(i)
    elif i in u:
        upper.append(i)
    elif i.isdigit():
        if int(i)%2==0:
            eve.append(i)
        elif int(i)%2!=0:
            odd.append(i)
digits=sorted(odd)+sorted(eve)
lower.sort()
upper.sort()
lower.extend(upper)
lower.extend(digits)
print(''.join(lower))