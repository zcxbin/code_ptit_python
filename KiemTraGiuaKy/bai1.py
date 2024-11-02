def largest_smaller_number(s):
    digits = list(s)
    n = len(digits)

    for i in range(n - 1, 0, -1):
        if digits[i] < digits[i - 1]:
            break
    else:
        return -1

    for j in range(n - 1, i - 1, -1):
        if digits[j] < digits[i - 1]:
            digits[i - 1], digits[j] = digits[j], digits[i - 1]
            break

    digits[i:] = sorted(digits[i:], reverse=True)
    result = ''.join(digits)
    return result if result[0] != '0' else -1


T = int(input())
for _ in range(T):
    N = input()
    result = largest_smaller_number(N)
    print(result)
