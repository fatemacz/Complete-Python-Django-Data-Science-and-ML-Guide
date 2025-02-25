# -------------------------
# Example 1
# -------------------------
def other_func():
    print("This is other function")


def func_with_callback(callback_func):
    print("This is the main function")
    callback_func()


func_with_callback(other_func)


# -------------------------
# Example 2
# -------------------------
def print_number_info(number):
    if number % 2 == 0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")


def process_numbers(numbers, callback_func):
    for number in numbers:
        callback_func(number)


nums = [1, 2, 3, 4, 5]
process_numbers(nums, print_number_info)
