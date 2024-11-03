def power_mod(base, exp, mod):
    res = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    return res % mod


t = int(input())
for _ in range(t):
    a, b, c, d, mod = map(int, input().split())
    exp = power_mod(c, d, mod)
    base = power_mod(a, b, mod)
    res = power_mod(base, exp, mod)
    print(res)
