mod = 10 ** 9 + 7


def power_pow(a, b):
    if b == 1:
        return a
    if b % 2 == 1:
        return power_pow(a, b - 1) * a % mod
    p = power_pow(a, b // 2)
    return p * p % mod


def cal(n, k):
    if k <= 1:
        return k
    ex = 0
    while k // 2 ** ex != 1:
        ex += 1
    return power_pow(n, ex) + cal(n, k - (2 ** ex))


for t in range(int(input())):
    n, k = map(int, input().split())
    print(cal(n, k) % mod)
