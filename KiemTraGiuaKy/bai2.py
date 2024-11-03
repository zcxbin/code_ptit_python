t = int(input())
for _ in range(1, t + 1):
    s1 = input().strip()
    s2 = input().strip()

    if sorted(s1) == sorted(s2):
        print(f"Test {_}: YES")
    else:
        print(f"Test {_}: NO")


