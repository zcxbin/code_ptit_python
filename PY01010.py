for t in range(int(input())):
    nums = input()
    if nums[:2] == nums[:-2]:
        print("YES")
    else:
        print("NO")

