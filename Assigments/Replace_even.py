def replace_evens(li):
    temp=[i if i%2!=0 else 0 for i in li]
    return temp
if __name__=="__main__":
    li=eval(input('Enter the list:'))
    print(replace_evens(li))