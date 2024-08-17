import math


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


t = int(input())
while t > 0:
    n = int(input())
    dem = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            dem += 1
    if is_prime(dem):
        print("YES")
    else:
        print("NO")
    t -= 1
