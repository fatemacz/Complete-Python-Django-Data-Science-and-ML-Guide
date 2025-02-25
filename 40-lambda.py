# 1. Regular function returns a lambda function
def multiply_by(multiplier):
    return lambda x: x * multiplier


multiply_by_3 = multiply_by(3)

print(multiply_by_3(10))
print(multiply_by_3(50))

multiply_by_5 = multiply_by(5)

print(multiply_by_5(10))
print(multiply_by_5(50))


# 2. Sorting list of dictionaries
students = [
    {'name': 'John', 'score': 50},
    {'name': 'Alice', 'score': 20},
    {'name': 'Bob', 'score': 90}
]

# def sort_by_score(student):
#     return student['score']

students.sort(key=lambda student: student['score'], reverse=True)
print(students)


# 3. Filtering a list
my_nums = [3, 4, 10, 15, 20, 21]

even_nums = list(filter(lambda num: num % 2 == 0, my_nums))
print('Even numbers', even_nums)

odd_nums = list(filter(lambda num: num % 2 == 1, my_nums))
print('Odd numbers', odd_nums)
