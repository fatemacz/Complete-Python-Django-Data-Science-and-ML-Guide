def contains_at_symbol(email):
    return '@' in email


def register_user(email: str, age: int):
    if not isinstance(email, str):
        raise TypeError("Email must be a string")

    if not isinstance(age, int):
        raise TypeError("Age must be an integer")

    if not contains_at_symbol(email):
        raise ValueError("Invalid email. Email must contain @ sign")

    # Register user...
    print("User was registered successfully")
    return {'email': email, 'age': age}


try:
    registered_user = register_user('abc@abc.com', 10)
    print(registered_user)
except (TypeError, ValueError) as e:
    print(e)
