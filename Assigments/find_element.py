def find_tuple_element(t,key):
    return key in t
tup=eval(input('Enter the tuple:'))
key=eval(input('Enter the key element:'))
print(find_tuple_element(tup,key))