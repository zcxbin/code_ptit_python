t = int(input())

while t > 0:
    s = input()
    s += " "
    length = len(s)
    res = -1
    x = 0
    for i in range(0, length - 1):
        if s[i].isdigit():
            x = x * 10 + int(s[i])
            if s[i + 1].isalpha():
                res = max(res, x)
                x = 0
    print(max(res, x))
    t -= 1

