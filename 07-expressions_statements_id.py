# the result of an expression is the """value"""
# 5 + 3                 # expression, result is 8
# a > b                 # expression, result is True or False
# 'Hello ' + 'World'    # expression, result is 'Hello World'
# my_func(10, 5)        # expression, result is the return value of the function

# ----------------------------

# statement perform """actions"""
my_name = "Aye"  # statement, assigning the value to new variable

# conditional statement
if my_name:  # expression, result is True
    print(my_name)  # statement, printing the message

import datetime  # statement, importing the module

# ----------------------------

# id() function
# id() function returns the memory address of the object
# id() function is used to check if two variables refer to the same object
# id() function is used to check if the object is mutable or immutable

my_name = "Aye"
print(id(my_name))

# reference to the same memory address
my_num = 777
print(id(my_num))

other_num = my_num
print(id(other_num))

print(id(my_num) == id(other_num))
print()

# new memory address
my_val = 10
print(id(my_val))

my_val = "Test"
print(id(my_val))
print()

# existing memory address
my_lst = [1, 2, 3]
print(id(my_lst))

my_lst.append(4)
print(id(my_lst))
print()

# new memory address
my_lst = [4, 5]
print(id(my_lst))


# ----------------------------
# Names in Python (variable names)
# ----------------------------
# snake_case            - Variable, Function, Method, Module
# CamelCase/ PascalCase - Class, (Exception)
# my-package            - Package
# CONSTANT_VARIABLE     - Constant variable

# ----------------------------
