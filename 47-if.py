# 1. if
def check_shipping_fee(weight):
    if weight <= 0:
        print("Invalid weight. Weight must be greater than zero")

    if 0 < weight <= 5:
        print("The shipping fee is 5$")

    if 5 < weight <= 15:
        print("The shipping fee is 10$")

    if weight > 15:
        print("The shipping fee is 20$")


check_shipping_fee(11.5)


# 2. if else
def check_shipping_fee(weight):
    if weight <= 0:
        print("Invalid weight. Weight must be greater than zero")
    else:
        print("Shipping fee is 5$")


check_shipping_fee(-100)


# 3. if elif else
def check_shipping_fee(weight):
    if weight <= 0:
        print("Invalid weight. Weight must be greater than zero")
    elif weight <= 5:
        print("The shipping fee is 5$")
    elif weight <= 15:
        print("The shipping fee is 10$")
    else:
        print("The shipping fee is 20$")


check_shipping_fee(100)


# 4. Hardcoded dividers (if elif else)
def check_divisibility(num):
    if num % 3 == 0 and num % 5 == 0:
        print("Number is divisible by 3 and 5")
    elif num % 3 == 0:
        print("Number is divisible only by 3")
    elif num % 5 == 0:
        print("Number is divisible only by 5")
    else:
        print("Number is not divisible by 3 or by 5")


check_divisibility(15)


# 5. Dividers as parameters (if elif else)
def check_divisibility(num: int, divider1: int, divider2: int):
    if num % divider1 == 0 and num % divider2 == 0:
        print(f"Number is divisible by {divider1} and {divider2}")
    elif num % divider1 == 0:
        print(f"Number is divisible only by {divider1}")
    elif num % divider2 == 0:
        print(f"Number is divisible only by {divider2}")
    else:
        print(f"Number is not divisible by {divider1} or by {divider2}")


check_divisibility(20, 4, 5)
