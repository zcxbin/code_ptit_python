n, m, k = map(int, input().split())
ke = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
def dfs(u):
    visited[u] = True
    for v in ke[u]:
        if not visited[v]:
            dfs(v)


for i in range(m):
    x, y = map(int, input().split())
    ke[x].append(y)
    ke[y].append(x)

dfs(k)

for i in range(1, n + 1):
    if not visited[i]:
        print(i)

