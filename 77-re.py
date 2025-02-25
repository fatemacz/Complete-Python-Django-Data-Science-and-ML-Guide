import re

# 1. Searching using re "search"
my_string = "My name is Bogdan."

res = re.search(r'^M.*Bogdan\.$', my_string)
print(res.span())
print(res.start())
print(res.end())
print(res)


# 2. Creating patterns using re "compile"
my_string = "My name is Bogdan."

my_pattern = re.compile(r'B....n')
print(my_pattern)
print(type(my_pattern))

print(my_pattern.search(my_string))
print(my_pattern.search("Hello, this is Boooon"))

print(my_pattern.match(my_string))
print(my_pattern.match('Boooon'))
print(my_pattern.match('Bogdan!!!'))

print(my_pattern.findall("My name is Bogdan. Hello Bogdan"))


# 3. Validating an email using re
def validate_email(email):
    email_regexp = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    email_pattern = re.compile(email_regexp)
    is_valid = bool(email_pattern.match(email))
    return email, is_valid


print(validate_email('bogdan@gmail.com'))  # Valid
print(validate_email('bogdangmail.com'))  # Invalid
print(validate_email('bogdan@gmailcom'))  # Invalid


# 4. Substitution using re "sub"
regexp = r'bad'

my_text = "Something bad is here. bad situation. bad words"

changed_text = re.sub(regexp, '*', my_text)
print(changed_text)


# 5. Splitting the string using re "split"
my_text = "This is    a very    long    not formatted    sentence"
print(my_text)

regexp = r'\s+'

words = re.split(regexp, my_text)
print(words)
print(' '.join(words))

print(my_text.split(' '))
