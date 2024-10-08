# main.py

import math_utils

try:
    number = int(input("Nhập một số tự nhiên: "))
    print(f"Giai thừa của {number} là {math_utils.factorial(number)}")
except ValueError as e:
    print(e)
