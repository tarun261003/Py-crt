def lonelyinteger(a):
    res=0
    for i in a:
        res^=i
    return res
a=[1]
print(lonelyinteger(a))