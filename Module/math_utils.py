# math_utils.py

def factorial(n):
    """
    Hàm tính giai thừa của một số tự nhiên n.

    Parameters:
    n (int): Số tự nhiên cần tính giai thừa.

    Returns:
    int: Giai thừa của n.
    """
    if n < 0:
        raise ValueError("Số n phải là số tự nhiên (n >= 0).")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
