import random

# float
print(random.random())
print(random.uniform(10.5, 11.6))


# int
print(random.randint(100, 1000))
print(random.randint(0, 1000))


# shuffle
my_list = [1, 2, 3, 4, 5, 6, 7]
print(my_list)
random.shuffle(my_list)
print(my_list)
random.shuffle(my_list)
print(my_list)


# choice
print(random.choice('Bogdan'))
print(random.choice((1, 3, 10)))
# print(random.choice({'a': 10, 'b': True}))
print(random.choice(['a', True, None]))


# choices (elements might be repeated)
print(random.choices([1, 2, 3, 4, 5], k=5))
print(random.choices('abcdef', k=10))


# create password (not recommended)
print(''.join(random.choices('ABCDEF0123456789', k=12)))


# sample (unique elements)
print(random.sample([1, 2, 3, 4, 5], k=5))
print(random.sample([1, 2, 3, 4, 5], k=3))
# print(random.sample([1, 2, 3, 4, 5], k=10))  # ValueError: Sample larger than population or is negative
print(''.join(random.sample('ABCDEF0123456789', k=12)))
print(random.sample([1, 1, 1, 1], k=3))
print(random.sample(range(1_000_000), k=10))
