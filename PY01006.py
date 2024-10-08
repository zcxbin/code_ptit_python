t = int(input())
while t > 0:
    n = input().strip()
    dem = 0
    check = True
    for i in n:
        if i != '4' and i != '7':
            check = False
    if check:
        print('YES')
    else:
        print('NO')
    t -= 1
