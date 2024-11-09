from math import gcd

for _ in range(int(input())):
    x = int(input())
    print('YES') if gcd(x, int(str(x)[::-1])) == 1 else print('NO')


