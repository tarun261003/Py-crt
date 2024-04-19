import sys

def sum_multiples_of_3_and_5(n):
    n -= 1  # Adjust to exclude n itself from the range
    n3 = n // 3  # Number of multiples of 3 below n
    n5 = n // 5  # Number of multiples of 5 below n
    n15 = n // 15  # Number of multiples of 15 (LCM of 3 and 5) below n
    sum_3 = 3 * n3 * (n3 + 1) // 2  # Sum of multiples of 3
    sum_5 = 5 * n5 * (n5 + 1) // 2  # Sum of multiples of 5
    sum_15 = 15 * n15 * (n15 + 1) // 2  # Sum of multiples of 15
    print(sum_3,sum_5)
    return sum_3 + sum_5 - sum_15  # Subtract the common multiples counted twice

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(sum_multiples_of_3_and_5(n))
