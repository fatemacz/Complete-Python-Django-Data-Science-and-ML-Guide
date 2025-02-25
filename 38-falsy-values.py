# 1. Falsy values
print(bool(0))
print(bool(0.0))
print(bool(0j))

print(bool(None))
print(bool(False))

print(bool(''))

print(bool([]))
print(bool({}))
print(bool(()))
print(bool(set()))
print(bool(range(0)))


# 2. Truthy values
print(bool(10))
print(bool(3.6))
print(bool(3j))

print(bool(True))

print(bool('abc'))

print(bool([1, 2]))
print(bool({'a': 'abc'}))
print(bool((3, 5)))
print(bool({10, 20}))
print(bool(range(100)))


# 3. No need to compare "len" of the sequence to 0
my_dict = {'a': 10, 'b': [1, 2]}

if len(my_dict) > 0:
    print("Dictionary is not empty")


# 4. No need to use "len" of the sequence
my_dict = {'a': 10, 'b': [1, 2]}

if len(my_dict):
    print("Dictionary is not empty")


# 5. No need to convert to "bool" explicitly
my_dict = {'a': 10, 'b': [1, 2]}

if bool(my_dict):
    print("Dictionary is not empty")


# 6. Implicit conversion to "bool"
my_dict = {'a': 10, 'b': [1, 2]}

if my_dict:
    print("Dictionary is not empty")

if not my_dict:
    print("Dictionary is empty")

if my_dict.get('b'):
    print("Key 'b' in the dictionary has value")
