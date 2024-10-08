for test in range(int(input())):
    res = ""
    encode = input()
    for i in range(0, len(encode), 2):
        res += encode[i] * int(encode[i+1])

    print(res)


