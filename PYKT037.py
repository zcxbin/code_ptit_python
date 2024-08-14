coSo = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

t = int(input())

while t > 0:
    n, heCoSo = map(int, input().split())
    s = ""

    while n > 0:
        s += coSo[n % heCoSo]
        n //= heCoSo
    print(s[::-1])
    t -= 1
