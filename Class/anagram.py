def anagram_check(s1,s2):
    if len(s1)!=len(s2):
        return False
    for i in s1:
        if i not in s2:
            return False
    return True
if __name__=="__main__":
    s1=input('Enter string 1:')
    s2=input('Enter string 2:')
    result="Yes, it is anagram" if anagram_check(s1,s2) else "No,it is not anagram."
    print(result)