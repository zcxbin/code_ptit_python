for _ in range(int(input())):
    n = int(input())
    x, y, z = map(int, input().split())
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        dp[i] = min(dp[i - 1] + x, dp[i // 2] + z if i % 2 == 0 else dp[(i + 1) // 2] + y + z)

    print(dp[n])
