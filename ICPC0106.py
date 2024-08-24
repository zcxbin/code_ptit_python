co_so_16 = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100",
            "1101", "1110", "1111"]
co_so_8 = ["000", "001", "010", "011", "100", "101", "110", "111"]
co_so_4 = ["00", "01", "10", "11"]

t = int(input())

while t > 0:
    n = int(input())
    s = input()
    convertNumber = ""

    if n == len(co_so_16):  # Check for base 16
        for i in range(0, len(s), 4):
            tmp = s[i:i + 4]
            convertNumber += str(co_so_16.index(tmp))
    elif n == len(co_so_8):  # Check for base 8
        for i in range(0, len(s), 3):
            tmp = s[i:i + 3]
            convertNumber += str(co_so_8.index(tmp))
    elif n == len(co_so_4):  # Check for base 4
        for i in range(0, len(s), 2):
            tmp = s[i:i + 2]
            convertNumber += str(co_so_4.index(tmp))
    else:
        convertNumber = str(n)

    print(convertNumber)
    t -= 1
