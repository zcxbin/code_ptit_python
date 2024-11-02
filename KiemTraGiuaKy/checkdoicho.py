def mind(s, i):
    ans = i
    for j in range(i + 1, len(s)):
        if s[j] < s[i] and (ans == i or s[ans] < s[j]):
            ans = j
    return ans if s[ans] < s[i] else -1

for _ in range(int(input())):
    s = input()
    n = len(s)
    ans = '-1'
    for i in range(n - 1, -1, -1):
        ind = mind(s, i)
        if ind > -1:
            ans = s[:i] + s[ind] + s[i + 1:ind] + s[i] + s[ind + 1:]
            if ans[0] != '0':
                break
            ans = '-1'
    print(ans)
