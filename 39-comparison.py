# 1. Comparison operators for integers
a = 7
b = 10

print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
print(a == b)
print(a != b)


# 2. Comparison operators for lists and corresponding magic methods
a = [1, 2]
b = [1, 2]

print(id(a))
print(id(b))

print(a > b)
# a.__gt__
print(a >= b)
# a.__ge__
print(a < b)
# a.__lt__
print(a <= b)
# a.__le__
print(a == b)
# a.__eq__
print(a != b)
# a.__ne__


# 3. Comparison operators in the conditional statements
name = "Alice"

if len(name) > 4:
    print("Name is longer than 4 characters")

name = "Bob"

if len(name) > 4:
    print("Name is longer than 4 characters")


# 4. Comparison operator and built-in sum function
my_nums = (10, 3, 20, 6)

print(sum(my_nums))

if sum(my_nums) > 20:
    print("Sum is greater than 20")


# 5. Checking if list is already sorted using equality operator and built-in sorted function
my_nums = [10, 3, 5, 20]

if my_nums == sorted(my_nums):
    print("List my_nums is already sorted!")

other_nums = [3.5, 5.10, 7.75, 10.05]

if other_nums == sorted(other_nums):
    print("List other_nums is already sorted")

print(id(other_nums) == id(sorted(other_nums)))
