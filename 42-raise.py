# -----------------
# Example 1 - Raise an exception in a function
# -----------------
def divide_nums(number, divisor):
    if isinstance(number, str):
        raise TypeError("Function Raise: number cannot be a string!")
    if isinstance(divisor, str):
        raise TypeError("Function Raise: divisor cannot be a string!")
    if divisor == 0:
        raise ZeroDivisionError("Function Raise: divisor cannot be zero!")
        # raise Exception("Function Raise: divisor cannot be zero!") # can be used as well if you want to catch all exceptions. (not recommended)
    return number / divisor


# print("Program starts...")
# print(divide_nums(10, 0))
# print("Program continues...")

print("Program starts...")
try:
    result = divide_nums(10, 0)
    # result = divide_nums("10", 0)
    # result = divide_nums(10, 4)
# except TypeError as e:  # Skip as the exception is raised in the function
#     print(e)
# except ZeroDivisionError as e:  # Skip as the exception is raised in the function
#     print(e)
except Exception as e:  # General exception class catches all exceptions
    print(e)
else:
    print(f"No Error! Result: {result}.")

print("Program continues...")


# -----------------
# Example 2 - Raise an exception in a function
# -----------------
def contains_at_symbol(email):
    return "@" in email


def register_user(email: str, age: int):
    if not isinstance(email, str):
        raise TypeError("Email must be a string")

    if not isinstance(age, int):
        raise TypeError("Age must be an integer")

    if not contains_at_symbol(email):
        raise ValueError("Invalid email. Email must contain @ sign")

    # Register user...
    print("User was registered successfully")
    return {"email": email, "age": age}


try:
    registered_user = register_user("abc@abc.com", 10)
    print(registered_user)
except (TypeError, ValueError) as e:
    print(e)
