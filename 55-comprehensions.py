# -------------------------
# For In Expressions (Comprehensions)
# -------------------------
#       Expression for Element in Sequence if Condition


# -------------------------
# 1. List comprehension
# -------------------------
nums = [10, 2, 5, 100]

squared_nums = [num * num for num in nums]

print(nums)
print(squared_nums)


even_nums = [num for num in nums if num % 2 == 0]

print(even_nums)


# -------------------------
# 2. Dictionary comprehension
# -------------------------
fruits = ["banana", "mandarin", "orange", "apple"]

fruits_length = {fruit: len(fruit) for fruit in fruits}
print(fruits_length)

# {
#     'banana': 6,
#     'mandarin': 8,
#     ...
# }


# -------------------------
# 3. Tuple comprehension
# -------------------------
names = ["Bogdan", "Alice", "Bob"]

# Using only parentheses will be a generator
names_lengths = tuple(len(name) for name in names)

print(names_lengths)


# -------------------------
# 4. Tuple to list using comprehension
# -------------------------
coordinates = (120, 240, 500)

coordinates_list = [coordinate * 2 for coordinate in coordinates]
print(coordinates_list)


# -------------------------
# 5. zip object to a dictionary using comprehension
# -------------------------
grades = (80, 95, 65)
subjects = ["Science", "Math", "Physics"]

grade_dict = {subject: grade - 10 for subject, grade in zip(subjects, grades)}
print(grade_dict)


# -------------------------
# 6. Dictionary to a list using comprehension
# -------------------------
person = {"name": "Bogdan", "favorite_num": 777, "is_instructor": True}

person_str_values = [value for value in person.values() if type(value) == str]
print(person_str_values)


# -------------------------
# 7. Dictionary to a dictionary using comprehension
# -------------------------
stocks = {"GOOGL": 1500, "AMZN": 3000, "AAPL": 300}

doubled_stocks = {k: v * 2 for k, v in stocks.items() if v >= 500}
print(doubled_stocks)


# -------------------------
# 8. Chaining "for in" expressions
# -------------------------
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [num for sublist in nested_list for num in sublist]
print(flattened_list)


# -------------------------
next_nested_list = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
next_flattened_list = [
    num
    for first_layer in next_nested_list  # [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
    for second_layer in first_layer  # [[1, 2, 3], [4, 5, 6]] -> [1, 2, 3], [4, 5, 6]
    for num in second_layer  # [1, 2, 3] -> 1, 2, 3
]
print(next_flattened_list)
