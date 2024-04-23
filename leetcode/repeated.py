def get_subs(s):
    return sorted([s[i:j] for  i in range(len(s)+1) for j in range(i+1,len(s)+1)],key=len)
def check_sub(sub):
    for i in subs:
        for j in range(len(i)+1):
            if i*j==s:
                print(i*j)
                return True
    return False
s=input('Enter the string :')
subs=get_subs(s)
subs.remove(s)
print(check_sub(subs))