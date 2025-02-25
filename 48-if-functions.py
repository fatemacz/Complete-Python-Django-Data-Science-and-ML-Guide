# 1. "if else" in the function and single return
def calc_discounted_price(price: float, is_member: bool):
    if is_member:
        discount = price * 0.1  # 10% discount
    else:
        discount = price * 0.05  # 5% discount
    return price - discount


res_price = calc_discounted_price(price=1000, is_member=True)
print(res_price)


# 2. "if" in the function and multiple returns
def calc_discounted_price(price: float, is_member: bool):
    if is_member:
        return price - price * 0.1  # 10% discount

    return price - price * 0.05  # 5% discount


res_price = calc_discounted_price(price=1000, is_member=True)
print(res_price)


# 3. "if elif else" in the function and single return
def get_letter_grade(grade):
    if grade >= 90:
        letter_grade = 'A'
    elif grade >= 80:
        letter_grade = 'B'
    elif grade >= 70:
        letter_grade = 'C'
    elif grade >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
    return letter_grade


print(get_letter_grade(70))


# 4. "if" in the function and multiple returns
def get_letter_grade(grade):
    if grade >= 90:
        return 'A'
    if grade >= 80:
        return 'B'
    if grade >= 70:
        return 'C'
    if grade >= 60:
        return 'D'

    return 'F'


print(get_letter_grade(30))
