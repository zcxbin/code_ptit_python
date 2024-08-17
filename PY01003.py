t = int(input())

for i in range(t):
    n = int(input())
    dem = 1
    while n > 10 ** dem:
        remainder = n % 10 ** dem

        if remainder >= 5 * 10 ** (dem - 1):
            n += 10 ** dem

        n -= remainder
        dem += 1
        # print(f"{n} {remainder}")
    print(n)

"""
Input
7
15
14
5
99
12345678
44444445
1445

Output
20
10
5
100
10000000
50000000
2000
"""