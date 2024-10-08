for i in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    s = 0
    for i in range(0, n - 2):
        l = i + 1
        r = len(nums) - 1
        x = nums[i]
        while l < r:
            if x + nums[l] + nums[r] == 0:
                s += 1
                l += 1
            elif x + nums[l] + nums[r] < 0:
                l += 1
            else:
                r -= 1
    print(s)
