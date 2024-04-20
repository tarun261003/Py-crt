def cap(s):
    t=s.replace(' ','$')
    l=s.split()
    temp=[]
    for i in l:
        if i.isalnum():
            if i[0].isdigit():
                temp.append(i)
                continue
            else:
                temp.append(i.capitalize())
                continue
        try:
            temp.append(i.capitalize())
        except Exception as e:
            temp.append(i)
    str1=' '.join(temp)
    return str1
s=input('Enter:')
print(cap(s))