def is_special_number(n, d):
    str_n = str(n)
    d_str = str(d)

    if d_str not in str_n:
        return False

    for i in range(len(str_n)):
        if str_n[i] == d_str:
            if i % 2 == 0:
                return False

    return True


m, d = map(int, input().split())
cnt = 0
a, b = map(int, input().split())
for i in range(a, b + 1):
    if is_special_number(i, d):
        if i % m == 0:
            cnt = (cnt + 1) % (10 ** 9 + 7)

print(cnt)
