def find_divisor(x, target):
    found = False
    left, right = 1, x
    while left < right:
        mid = (left + right) // 2
        if x // mid > target:
            left = mid + 1
        elif x // mid < target:
            right = mid - 1
        else:
            found = True
            right = mid
    if x // right == target:
        found = True
    return found, right


def check_all_divisors(arr, target):
    total = 0
    for num in arr:
        result = find_divisor(num, target)
        if not result[0]:
            return False, total
        total += result[1]
    return True, total


n = int(input())
a = list(map(int, input().split()))
minimum_value = min(a)

for i in range(minimum_value, 0, -1):
    result = check_all_divisors(a, i)
    if result[0]:
        print(result[1])
        break
