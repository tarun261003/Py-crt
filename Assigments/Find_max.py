def find_max(li):
    max=li[0]
    for i in li:
        if i>max:
            max=i
    return max
if __name__=="__main__":
    li=eval(input('Enter the list:'))
    print(f'The maximum is {find_max(li)}')