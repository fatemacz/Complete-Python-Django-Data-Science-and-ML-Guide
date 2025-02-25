# 1. Tuple unpacking
employee_info = ("Jane Doe", 32, "Junior Developer")

employee_name, employee_age, employee_position = employee_info

# employee_name = employee_info[0]
# employee_age = employee_info[1]
# employee_position = employee_info[2]

print(employee_name, employee_age, employee_position)


# 2. Creating a new tuple
color = (225, 128, 10)

red, green, blue = color
print(red)
print(green)
print(blue)

red = 100
blue = 20

color = (red, green, blue)
print(color)


# 3. List of tuples
user_credentials = [
    ("user1", "password_one"),
    ("user2", "password_two"),
    ("user3", "password_three")
]

user1, user2, user3 = user_credentials

print(user1)
print(user2)
print(user3)

user1_username, user1_password = user1
user2_username, user2_password = user2
user3_username, user3_password = user3

print(user1_username, user1_password)
print(user2_username, user2_password)
print(user3_username, user3_password)


# 4. Error - unpacking more elements
person = ('Bob', 25)

# ValueError: not enough values to unpack (expected 3, got 2)
name, age, city = person

print(name)
print(age)
print(city)


# 5. No error
person = ('Bob', 25)

name, age, *other = person

print(name)
print(age)
print(other)


# 6. Gathering middle elements
school_grades = (80, 75, 35, 20, 90)

first, *middle, last = school_grades

print(first)
print(middle)
print(last)


# 7. Gathering remaining elements
school_grades = (80, 75, 35, 20, 90)

first, second, *remaining = school_grades

print(first)
print(second)
print(remaining)


# 8. Placeholder variable
comment = ("This is a great course", 'bob_202', 120, 4.7)

_, username, _, course_rating = comment

print(username)
print(course_rating)
