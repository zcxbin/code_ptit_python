def Try(n, k):
    x = 2 ** (n - 1)
    if k == n:
        return chr(n - 1 + ord('A'))
    if k > x:
        return Try(n - 1, x - (k - x))
    return Try(n - 1, k)


for t in range(int(input())):
    n, k = map(int, input().split())
    print(Try(n, k))
