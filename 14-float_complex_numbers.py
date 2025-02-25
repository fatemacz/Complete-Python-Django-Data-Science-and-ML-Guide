# Floats
# ----------------------------
average_rating = 4.00
print(average_rating.is_integer())  # True

average_rating = 4.65
print(average_rating.is_integer())  # False

print(round(average_rating))  # 5

# import math
# print(math.floor(average_rating))  # 4
print(int(average_rating))  # 4

print(float(100))  # 100.0

print(dir(average_rating))
print(average_rating.__divmod__(4))  # (1.0, 0.65)
print(average_rating.__mod__(2))  # 0.65

# Complex Numbers (real + imaginary)
# ----------------------------
# In Python, a complex number is represented as a pair of real numbers,
# where the first part is the real part and the second part is the imaginary part, followed by ‘j’ or ‘J’.
# Python has built-in support for complex numbers, which allows them to be defined and manipulated directly.
complex_a = 2 + 4j
complex_b = 5 + 7j

sum_complex = complex_a + complex_b
print(sum_complex)  # (7+11j)
print(type(sum_complex))  # <class 'complex'>

print(sum_complex.real)  # 7.0
print(sum_complex.imag)  # 11.0

# Ref: https://www.geeksforgeeks.org/complex-numbers-in-python-set-1-introduction/
# Ref: https://www.geeksforgeeks.org/complex-numbers-python-set-2-important-functions-constants/
# Ref: https://www.geeksforgeeks.org/complex-numbers-in-python-set-3-trigonometric-and-hyperbolic-functions/
