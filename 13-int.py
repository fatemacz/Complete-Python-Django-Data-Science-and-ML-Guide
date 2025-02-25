my_num = 1000
other_num = 100

res = my_num + other_num
print(res)

# ----------------------------
# Long Numbers
# ----------------------------
my_num = 1_000_000_000_000
other_num = 1_000

res = my_num / other_num
print(res)

my_num = 1_00_000_0  # position of underscore doesn't matter
print(my_num)

# ----------------------------
# Exponential Notation
# ----------------------------
my_num = 1e-2  # 1 * 10^-2
print(my_num)

my_num = 1e3  # 1 * 10^3
print(my_num)
# ----------------------------

input_str = input("Enter any number: ")
print(type(input_str))
try:
    input_num = int(input_str)
    print(type(input_num))
except ValueError:
    print("Not able to convert to int")

# ----------------------------
print(dir(my_num))
print(dir(__builtins__))

# ----------------------------
# Performance Test
# ----------------------------
import timeit

base = 1355
power = 245
# print(pow(base, power))
# print(base**power)

# built-in pow() function
format_time = timeit.timeit(
    "pow(base, power)",
    globals=globals(),
    number=1000000,
)
print(f"pow() function: {format_time:.6f} seconds")

# '**' operator - faster than pow()
format_time = timeit.timeit(
    "base**power",
    globals=globals(),
    number=1000000,
)
print(f"'**' operator: {format_time:.6f} seconds")
# ----------------------------
