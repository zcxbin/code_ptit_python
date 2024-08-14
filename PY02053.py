n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

# print(arr)
k = int(input())

nuaTren, nuaDuoi = 0, 0

for i in range(n):
    for j in range(n):
        # print(i, j)
        if j > n - i - 1:
            nuaDuoi += arr[i][j]
        elif j < n - i - 1:
            nuaTren += arr[i][j]

if abs(nuaTren - nuaDuoi) <= k:
    print('YES')
else:
    print('NO')

print(abs(nuaTren - nuaDuoi))
