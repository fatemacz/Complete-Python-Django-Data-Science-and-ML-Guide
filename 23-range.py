my_range = range(10)
print(type(my_range))  # <class 'range'>
print(my_range)  # range(0, 10)
print(my_range[2])  # 2
print()

print(list(my_range))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(tuple(my_range))  # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(set(my_range))  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(
    dict(my_range)
)  # TypeError: cannot convert dictionary update sequence element #0 to a sequence


# 1. Ranges with start, stop and step
# range_with_float_step = range(1, 100, 2.5) # TypeError: 'float' object cannot be interpreted as an integer
odd_nums = range(1, 100, 2)
even_nums = range(0, 101, 2)

print(list(odd_nums))
print(list(even_nums))

reverse_range = range(10, 0, -2)
print(list(reverse_range))

# 2. Index and count methods of the ranges
odd_nums = range(1, 100, 2)

print(odd_nums.index(51))
print(odd_nums.count(50))
print(odd_nums.count(51))

print(odd_nums.start)
print(odd_nums.stop)
print(odd_nums.step)


# 3. Range with start and stop
my_range = range(5, 8)
print(list(my_range))
print(my_range.start)
print(my_range.stop)
print(my_range.step)


# 4. Conversion of the range to list, tuple or set
odd_nums = range(1, 100, 2)

print(list(odd_nums))
print(tuple(odd_nums))
print(set(odd_nums))
print(dict(odd_nums))  # TypeError
