def count_multiples(li,num):
    return len([i for i in li if i%num==0])
if __name__=="__main__":
    li=eval(input('Enter the list:'))
    num=int(input('Enter the number:'))
    print(f'The number of elements that are divisible by {num} is :{count_multiples(li,num)}')