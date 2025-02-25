# ---------------------
# 1. Generator size is small
# ---------------------
# can create a generator using parentheses
# generator is smaller in size compared to a list or tuple (less memory usage)

from sys import getsizeof

squares_gen = (num * num for num in range(10_000_000))  # parentheses

print(getsizeof(squares_gen))  # 200

print(type(squares_gen))  # <class 'generator'>

# ---------------------
squares_list = [num * num for num in range(10_000_000)]  # square brackets

print(getsizeof(squares_list))  # 89095160

print(type(squares_list))  # <class 'list'>

# ---------------------
# convert generator to tuple
squares_tuple = tuple(num * num for num in range(10_000_000))

print(getsizeof(squares_tuple))  # 80000040

print(type(squares_tuple))  # <class 'tuple'>


# ---------------------
# 2. Iteration over the generator continues where it was stopped
# ---------------------
squares_gen = (num * num for num in range(100_000_000))

for num in squares_gen:
    print(num)
    if num == 100:
        break

print("START SECOND ITERATION")

for num in squares_gen:
    print(num)
    if num == 225:
        break
