import math

def checkSNT(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def reverseNumber(n):
    newNumber = 0
    while n > 0:
        digit = n % 10
        newNumber = newNumber * 10 + digit
        n = n // 10
    return newNumber

t = int(input())
while t > 0:
    n = int(input())
    result = set()
    for i in range(2, n):
        reversed_i = reverseNumber(i)
        if i != reversed_i and checkSNT(i) and checkSNT(reversed_i) and reversed_i < n:
            pair = tuple(sorted((i, reversed_i)))
            if pair not in result:
                result.add(pair)
                print(f"{i} {reversed_i}", end=" ")
    print()
    t -= 1
