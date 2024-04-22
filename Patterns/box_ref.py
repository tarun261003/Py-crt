def main():
    n = int(input())
    p = n
    for i in range(2 * n - 1):
        if i + 1 > n:
            dec = (n - 1) - ((i + 1) % n)
        else:
            dec = i
        inc = dec

        for j in range(2 * n - 1):
            if (2 * n - 1) - j <= inc:
                p += 1
            print(p, end=' ')

            if dec > 0:
                dec -= 1
                p -= 1
        print()

if __name__ == "__main__":
    main()
