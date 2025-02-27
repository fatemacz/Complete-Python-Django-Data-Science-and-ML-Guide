# 1. function declaration
def hello(name):
    print(name)
    print("Hello, there!")
    print("Hi there")


hello("Aye")
print()
hello("Alice")


# 2. function parameters and arguments
def add_numbers(a, b):
    sum = a + b
    print(sum)


add_numbers(5, 2)
add_numbers(100, 50)
add_numbers(8, 10.5)


# 3. return statement
def multiply_numbers(a, b):
    result = a * b
    return result
    print("This line is not executed!")


result_of_multiplication = multiply_numbers(20, 5)
print(result_of_multiplication)

print(multiply_numbers(15, 2))

# 4. built-in functions
print(__name__)
print()
print(dir())
print()
print(dir(__builtins__))
print()
print(ArithmeticError)
