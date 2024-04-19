def get_divbythree(li):
    return [i for i in li if i%3==0]
li=eval(input('Enter the list:'))
print(get_divbythree(li))