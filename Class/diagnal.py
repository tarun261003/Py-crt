def diagnal_sum(m,Ind):
    sum=0
    if Ind==0:
        for i in range(len(m)):
            sum+=m[i][i]
        return sum
    if Ind==-1:
        k=len(m)-1
        for i in range(len(m)):
            sum+=m[i][k]
            k-=1
        return sum
m=[[1,2,3],[4,5,6],[7,8,9]]
print(diagnal_sum(m,0))
print(diagnal_sum(m,-1))
print(abs(diagnal_sum(m,0)-diagnal_sum(m,-1)))