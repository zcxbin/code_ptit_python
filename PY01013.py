def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1


for i in range(int(input())):
    [a, b] = list(map(int, input().split()))
    UCLN = gcd(a, b)
    res = 0
    while UCLN > 0:
        res += UCLN % 10
        UCLN //= 10
    if isPrime(res):
        print("YES")
    else:
        print("NO")
