def sum_of_odds(li):
    l1=[i for i in li if i%2!=0]
    return l1,sum(l1)
if __name__=="__main__":
    li=eval(input('Enter the list:'))
    print(f'The odd numbers are:{sum_of_odds(li)[0]}')
    print(f'The sum of odd numbers are:{sum_of_odds(li)[1]}')