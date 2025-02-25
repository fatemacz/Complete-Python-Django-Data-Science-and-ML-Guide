# 1. Generator size is small
from sys import getsizeof

squares_gen = (num * num for num in range(10_000_000))

print(getsizeof(squares_gen))  # 208

print(type(squares_gen))  # <class 'generator'>

squares_list = [num * num for num in range(10_000_000)]

print(getsizeof(squares_list))  # 89095160

print(type(squares_list))  # <class 'list'>


# 2. Iteration over the generator continues where it was stopped
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
