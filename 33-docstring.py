def print_number_info(num):
    """
    Returns info regarding num, whether num is even or odd

    :param int num: Number to be evaluated
    :return str: Returns string which tells whether num is even or odd
    """
    if (num % 2) == 0:
        return "Num is even"
    else:
        return "Num is odd"


print(print_number_info(21))


# ----------------------------
# Explore the docstring of built-in functions
# ----------------------------
from math import acos


# ----------------------------
# Task: Create a function that multiplies two numbers
# ----------------------------
def multiply_numbers(a, b):
    """
    Multiplies two numbers

    :param int a: First number
    :param int b: Second number
    :return int: Returns the result of the multiplication
    """
    return a * b


print(multiply_numbers(2, 3))
