def anagram_check(s1,s2):
    if len(s1)!=len(s2):
        return False
    l1,l2=list(s1),list(s2)
    l1.sort()
    l2.sort()
    return l1==l2
if __name__=="__main__":
    s1=input('Enter string 1:')
    s2=input('Enter string 2:')
    result="Yes, it is anagram" if anagram_check(s1,s2) else "No,it is not anagram."
    print(result)