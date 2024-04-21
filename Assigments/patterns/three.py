#diamond pattern
def get_number(num):
    n='0'+num if num[0]=='1' else '1'+num
    return n 
n=int(input('Enter the size of pattern:'))
temp=''
for i in range(1,n+1):
    if not temp:
        temp='1'
        print(temp)
        continue
    temp=get_number(temp)
    print(temp)