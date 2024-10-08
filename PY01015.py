for test in range(int(input())):
    numbers = input()
    check = True
    for i in range(len(numbers) - 1):
        if int(numbers[i]) > int(numbers[i + 1]):
            check = False
            break

    if check:
        print("YES")
    else:
        print("NO")
