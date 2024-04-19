if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    X=[i for i in range(x+1)]
    Y=[i for i in range(y+1)]
    Z=[i for i in range(z+1)]
    final=[[i,j,k] for i in X for j in Y for k in Z if i+j+k!=n]
    # for i in X:
    #     for j in Y:
    #         for k in Z:
    #             if i+j+k!=n:
    #                 final.append([i,j,k])
print(final)