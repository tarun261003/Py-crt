def return_frequency(s1):
    d={}
    for i in s1:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d
def anagram_check(s1,s2):
    s1_d=return_frequency(s1)
    s2_d=return_frequency(s2)
    for i in s1_d:
        if s1_d[i]!=s2_d[i]:
            return False
    return True
s1=input('Enter string 1:')
s2=input('Enter string 2:')
result="Yes, it is anagram" if anagram_check(s1,s2) else "No,it is not anagram."
print(result)