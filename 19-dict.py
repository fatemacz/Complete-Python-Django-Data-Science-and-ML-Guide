# 1. Working with keys and values in the dictionary
my_bike = {"brand": "Custom", "price": 2000}

# print(my_bike.__doc__)

# # Error when accessing non-existing key
# print(my_bike["color"])  # KeyError: 'color'    # KeyError: 'color'

print(my_bike.get("color"))  # None
print(my_bike.get("color", "black"))  # black as default value


print(my_bike["brand"])
my_bike["color"] = "red"
print(my_bike)


my_string = "abcd"
my_dict = dict(
    my_string
)  # ValueError: dictionary update sequence element #0 has length 1; 2 is required


my_list = ["a", 10, "b", 20]
my_dict = dict(
    my_list
)  # ValueError: dictionary update sequence element #0 has length 1; 2 is required


my_list = [["a", 10], ["b", 20]]  # <OR> my_list = [("a", 10), ("b", 20)]
my_dict = dict(my_list)
print(my_dict)


# 2. Changing value of specific key
my_bike = {"brand": "Custom", "price": 2000}

print(my_bike)
my_bike["price"] = 3000
print(my_bike)


# 3. Getting all keys from the dictionary
my_bike = {"brand": "Custom", "price": 2000}

keys = my_bike.keys()  # dict_keys object
print(type(keys))
print(keys)

keys = list(my_bike.keys())  # list object
print(type(keys))
print(keys)


# 4. Getting pairs of keys and values from the dictionary
my_bike = {"brand": "Custom", "price": 2000}
items = my_bike.items()
print(type(items))  # dict_items object
print(items)


# 5. Copying the dictionary
my_bike = {"brand": "Custom", "price": 2000}

other_bike = my_bike.copy()

other_bike["color"] = "red"
print(my_bike)
print(other_bike)


# 6. "get" method vs square brackets notation for accessing key values
my_bike = {"brand": "Custom", "price": 2000}

print(my_bike.get("color", "black"))
print(my_bike["brand"])


my_list = [("a", 10), ("b", 20)]

print(dict(my_list))

# 7. Deleting key from the dictionary
my_bike = {"brand": "Custom", "price": 2000}
print(my_bike)  # {'brand': 'Custom', 'price': 2000}
val = my_bike.pop("price")
print(my_bike)  # {'brand': 'Custom'}
print(val)  # 2000

# 8. Deleting key from the dictionary
my_bike = {"brand": "Custom", "price": 2000}
print(my_bike)  # {'brand': 'Custom', 'price': 2000}
del my_bike["price"]
print(my_bike)  # {'brand': 'Custom'}


# 9. Nested dictionaries
my_bike = {
    "brand": "Custom",
    "price": 2000,
    "engine": {"power": 100, "type": "electric", "manufacturer": "Bosch"},
}
print(my_bike["engine"]["power"])
