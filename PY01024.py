def dist_2(n):
    for i in range(0, len(n) - 1):
        if abs((int(n[i]) - int(n[i + 1]))) != 2:
            return False
    return True


for i in range(int(input())):
    n = input()
    sumIdx = 0
    sumIdx += sum(int(i) for i in n)
    if sumIdx % 10 == 0 and dist_2(n):
        print("YES")
    else:
        print("NO")