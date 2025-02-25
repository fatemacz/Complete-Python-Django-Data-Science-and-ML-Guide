# --------------------
# 1. Regular function returns a lambda function
# --------------------
# Lambda is a small anonymous function.
# A lambda function can take any number of parameters, but can only have one expression.
# Implicitly return the result of the expression

# lambda parameters: expression
# e.g:  lambda a, b: a * b


def multiply_by(multiplier):
    return lambda x: x * multiplier


multiply_by_3 = multiply_by(3)

print(multiply_by_3(10))
print(multiply_by_3(50))

multiply_by_5 = multiply_by(5)

print(multiply_by_5(10))
print(multiply_by_5(50))

# --------------------


def greeting(greet):
    return lambda name: f"{greet}, {name}!"  # Return a lambda function


greet_hello = greeting("Hello")
# print(greet_hello)
print(greet_hello("Alice"))

greet_hi = greeting("Hi")
# print(greet_hi)
print(greet_hi("Bob"))

# --------------------


def multiply_the_sum(multiplier: int):
    return lambda *numbers: sum(numbers) * multiplier  # Return a lambda function


sum_multiplier_3 = multiply_the_sum(3)
print(sum_multiplier_3(100, 200, 300))
print(sum_multiplier_3(10, 20))

sum_multiplier_5 = multiply_the_sum(5)
print(sum_multiplier_5(50, 100, 150))


# --------------------
# 2. Sorting list of dictionaries
# --------------------
students = [
    {"name": "John", "score": 50},
    {"name": "Alice", "score": 20},
    {"name": "Bob", "score": 90},
]


# def sort_by_score(student):
#     print(student["score"])
#     return student["score"] # lambda student: student["score"]


# students.sort(key=sort_by_score, reverse=True)
# print(students)

students.sort(key=lambda student: student["score"], reverse=True)
print(students)


# --------------------
# 3. Filtering a list
# --------------------
my_nums = [3, 4, 10, 15, 20, 21]

# def is_even(num):
#     return num % 2 == 0 # lambda num: num % 2 == 0

# def is_odd(num):
#     return num % 2 != 0 # lambda num: num % 2 != 0

# even_nums = list(filter(is_even, my_nums))
# print("Even numbers", even_nums)

# odd_nums = list(filter(is_odd, my_nums))
# print("Odd numbers", odd_nums)

even_nums = list(filter(lambda num: num % 2 == 0, my_nums))
print("Even numbers", even_nums)

odd_nums = list(filter(lambda num: num % 2 != 0, my_nums))
print("Odd numbers", odd_nums)
