def convert_to_bin(dec):
    rem=[]
    while dec!=0:
        rem.append(dec%2)
        dec//=2
    return rem[::-1]
def count_set_bits(n):
    bin1=convert_to_bin(n)
    return bin1.count(1)
n=int(input('Enter the Number:'))
print(count_set_bits(n))