# Ternary Expression:
#       Expression1 if Condition else Expression2


# 1. Assigning result of the ternary expression to a variable
user_is_active = True

user_status_string = "Active" if user_is_active else "Inactive"
print(user_status_string)


# 2. Returning result of the ternary expression from the function
def convert_status_to_str(is_active):
    return "Active" if is_active else "Inactive"


user_is_active = True

user_status = convert_status_to_str(user_is_active)
print(user_status)


# 3. Checking discount eligibility in the function using ternary operator
def check_discount_eligibility(is_member):
    discount = 0.1 if is_member else 0.05
    return discount


customer_membership = False
discount_percentage = check_discount_eligibility(customer_membership)
print(discount_percentage)


# 4. Process data in the function if needed using ternary operator
def process_data(data):
    processed_data = data if data is not None else []
    # Process data...
    return processed_data


received_data = None
data = process_data(received_data)
print(data)


# 5. Calculate grades in the function using ternary operator
def get_letter_grade(score):
    letter_grade = (
        "A"
        if score >= 90
        else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
    )

    return letter_grade


print(get_letter_grade(95))
print(get_letter_grade(75))
print(get_letter_grade(60))
print(get_letter_grade(50))
