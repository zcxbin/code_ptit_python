t = int(input())

a = []

def checkNumber(n):
    for i in n:
        if int(i) % 2 == 1:
            return False
    return True


num = 2

while num <= 888:
    if checkNumber(str(num)):
        tmp = str(num)
        a.append(int(tmp + tmp[::-1]))
    num += 2


while t > 0:
    n = int(input())
    for x in a:
        if x >= n:
            break
        else:
            print(x, end=' ')
    print()
    t -= 1
