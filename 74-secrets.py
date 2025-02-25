import secrets
import string


# 1. Generating password of specific length
def generate_password(length: int):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(all_chars) for _ in range(length))
    return password


print(generate_password(5))
print(generate_password(10))
print(generate_password(20))

# print(string.digits)
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.punctuation)
#
# all_chars = string.ascii_letters + string.digits + string.punctuation
# print(all_chars)


# 2. Generating a CSRF token for user session
print(secrets.token_hex(8))
print(secrets.token_hex(16))
print(secrets.token_hex(24))


# 3. Generating URL safe token
print(secrets.token_urlsafe())
print(secrets.token_urlsafe(16))
# https://mywebsite.com/reset-password?token=Kny70ou4ijpyuJOOUrQSWjhY9nQ8hlewc_1PtVegY7Y


# 4. Generating OTP password
def generate_otp_password(length):
    digits = string.digits
    password = ''.join(secrets.choice(digits) for _ in range(length))
    return password


print(generate_otp_password(6))
print(generate_otp_password(4))
print(generate_otp_password(10))


# 5. Generate random password with requirements
# print(any(char.islower() for char in 'asdf2342'))
# print(any(char.isupper() for char in 'as2342'))
# print(any(char.isdigit() for char in 'asdf2342'))
# print(any(char in string.punctuation for char in 'asdf2342!?'))

counter = 0  # counts how many times we try to generate password


def generate_password(length: int):
    global counter
    counter += 1
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(all_chars) for _ in range(length))
    return password


# password must have at least one lowercase letter, one uppercase letter, one digit and one special symbolß


def generate_special_password(length: int):
    while True:
        p = generate_password(length)
        if any(c.islower() for c in p) and any(c.isupper() for c in p) and any(c.isdigit() for c in p) and any(
                c in string.punctuation for c in p):
            break
    return p


print(generate_special_password(4))
print(counter)
