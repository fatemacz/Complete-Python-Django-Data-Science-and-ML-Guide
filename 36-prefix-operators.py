# Operator and Left/Right Operands (variables, values, etc.)
# ---------------------------------------------------------
# Binary operators: (Infix: two operands)
# ----------------------
# Arithmetic operators: +, -, *, /
# Assignment operators: =
# Comparison operators: ==, !=, >, <, >=, <=
# Logical operators: and, or, not
# Identity (object equality) operators: is, is not
# Membership operators: in, not in
# Bitwise operators: &, |, ^, ~, <<, >>

# ----------------------
# Unary operators: (Prefix: only one operand)
# ----------------------
# +, -, not
# ----------------------

# For Priority of Operators: Do Grouping of operators
# ---------------------------------------------------------

a = 5


# ---------------------------------------------------------
# 1. Prefix unary "-" operator
# ---------------------------------------------------------
my_num = -10

print(my_num)
print(-my_num)


# ---------------------------------------------------------
# 2. Prefix unary "+" operator
# ---------------------------------------------------------
my_num = -10.3

print(my_num)
print(+my_num)


# ---------------------------------------------------------
# 3. Prefix unary "+" operator with booleans
# ---------------------------------------------------------
my_num = False

print(my_num)
print(+my_num)


# ---------------------------------------------------------
# 4. Prefix unary "not" operator
# ---------------------------------------------------------
my_name = "Aye"

print(my_name)
print(not my_name)
print(not not my_name)
print(bool(my_name))


# ---------------------------------------------------------
# 5. Prefix unary "not" operator with non-empty list
# ---------------------------------------------------------
my_list = [1, 2]
print(not my_list)


# ---------------------------------------------------------
# 6. Prefix unary "not" operator with empty list
# ---------------------------------------------------------
my_list = []
print(not my_list)


# ---------------------------------------------------------
# Task
# ---------------------------------------------------------
set_a = {1, 2, 3}
set_b = {1, 2, 3}
print(set_a == set_b)
print(set_a.__eq__(set_b))
print(set_a is set_b)
