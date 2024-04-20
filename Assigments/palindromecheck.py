def is_palindrome(s):
    t=s.lower()
    t=t.replace(' ','')
    return t==t[::-1]
if __name__=="__main__":
    s=input('Enter the string:')
    if is_palindrome(s):
        print(f'The given string "{s}" is palindrome.')
    else:
        print(f'The given string "{s}" is not a palindrome.')