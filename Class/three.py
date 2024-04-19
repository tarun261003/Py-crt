def sum_of_unique(li):
    temp=list(set(li))
    return temp,sum(temp)
li=eval(input('Enter the list:'))
print(f'The unique elements are:{sum_of_unique(li)[0]}')
print(f'The sum of unique elements are:{sum_of_unique(li)[1]}')