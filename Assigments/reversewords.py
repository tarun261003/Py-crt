def reverse_words(s):
    return ' '.join([i for i in s.split()[::-1]])
if __name__=="__main__":
    s=input('Enter the string:')
    print(f'The string with reversed words is :{reverse_words(s)}')