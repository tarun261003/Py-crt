def concat(t1,t2):
    return tuple(list(t1)+list(t2))
if __name__=="__main__":
    tup1=eval(input('Enter tuple1:'))
    tup2=eval(input('Enter tuple 2:'))
    print(f'The concatenated tuple is {concat(tup1,tup2)}')