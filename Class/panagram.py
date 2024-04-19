import string
alphabets=string.ascii_lowercase
print(alphabets)
senntence=input('Enter the sentence:').lower()
print(all(i in senntence for i in alphabets))