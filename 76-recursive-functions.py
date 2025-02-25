import math


def calc_factorial(num: int):
    if type(num) is not int:
        raise TypeError("Number must be integer")
    if num <= 0:
        raise ValueError("Number must be positive")
    if num == 1:
        return 1
    return num * calc_factorial(num - 1)


print(calc_factorial(10))
# print(calc_factorial('abc'))  # TypeError: Number must be integer

print(math.factorial(10))  # 10 * 9 * 8 ... 2 * 1
