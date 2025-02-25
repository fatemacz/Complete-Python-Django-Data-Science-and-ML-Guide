# 1. Adding keys or modifying values of the keys: order matters for the keys. The last key-value pair will overwrite the previous one.
person = {"name": "John", "age": 23}

# other_person = person.copy()
# other_person['age'] = 30

other_person = {**person, "age": 30, "occupation": "teacher"}

print(person)
print(other_person)
print(id(person) == id(other_person))


# 2. Merging two dictionaries: order matters for the keys. The last key-value pair will overwrite the previous one.
default_settings = {"theme": "light", "font_size": 16}
user_settings = {"font_size": 20, "show_avatar": True}

# merged_settings = {**default_settings, **user_settings}

merged_settings = default_settings | user_settings  # Python 3.9+

print(merged_settings)
