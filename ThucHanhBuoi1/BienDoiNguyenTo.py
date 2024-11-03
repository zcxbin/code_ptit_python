from math import sqrt

n = 123456
nt, Prime = [], [1] * n
Prime[0] = Prime[1]
for i in range(2, int(sqrt(n)) + 1):
    if Prime[i]:
        for j in range(i, n // i):
            Prime[i * j] = 0
for i in range(n):
    if Prime[i]:
        nt.append(i)
n, a = int(input()), list(map(int, input().split()))
M = 0
for i in a:
    m = nt[-1]
    for j in nt:
        m = min(m, abs(j - i))
    M = max(M, m)
print(M)
