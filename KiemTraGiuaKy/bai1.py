from itertools import permutations

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [str(i) for i in range(1, n + 1)]

    perm = sorted(permutations(arr), reverse=True)
    print(len(perm))

    for i in perm:
        print(''.join(i), end=' ')

    print()
