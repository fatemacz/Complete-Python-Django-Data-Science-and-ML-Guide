# 1. Zip object creation and its conversion to a list
# --------------------------------------------
products = ["phone", "tablet", "laptop"]
# quantities = [343, 13, 74]
quantities = (343, 13, 74)
products_qtys = zip(products, quantities)  # order matters

print(products_qtys)
print(type(products_qtys))

products_qtys_list = list(
    products_qtys
)  # converting the zip object to a list of tuples
print(products_qtys_list)


# 2. Iteration over the zip object
# --------------------------------------------
# zip object is an iterator, which means that it can be iterated over only once.
# If you want to iterate over it multiple times, you need to convert it to a list or tuple first.
products = ["phone", "tablet", "laptop"]
quantities = (343, 13, 74)
tags = "asd"

products_qtys = zip(products, quantities, tags)

# During the loop, the iterator is consumed, and after that point it's empty.
for product in products_qtys:
    print(product)  # nothing is printed, because the iterator is exhausted
    print(product[0])  # IndexError: tuple index out of range

products_qtys_list = list(products_qtys)
print(products_qtys_list)  # []  # itertor is exhausted

# # --------------------------------------------
# products = ["phone", "tablet", "laptop"]
# quantities = (343, 13, 74)
# tags = "asd"

# products_qtys = zip(products, quantities, tags)
# products_qtys_list_1 = list(
#     products_qtys
# )  # The first time you convert it to a list, the iterator is consumed, and after that point it's empty.
# products_qtys_list_2 = list(products_qtys)  # []  # itertor is exhausted

# print(
#     products_qtys_list_1
# )  # [('phone', 343, 'a'), ('tablet', 13, 's'), ('laptop', 74, 'd')]
# print(products_qtys_list_2)  # [] # itertor is exhausted
# # --------------------------------------------


# 3. Conversion of the zip object to a dictionary
# --------------------------------------------
products = ["phone", "tablet", "laptop"]
quantities = [343, 13]
# tags = "asd"

# products_qtys = zip(products, quantities, tags) # ValueError: dictionary update sequence element #0 has length 3; 2 is required
products_qtys = zip(products, quantities)

products_qtys_dict = dict(products_qtys)
print(products_qtys_dict)


# 4. Enumerate object
# --------------------------------------------
products = ["phone", "tablet", "laptop"]
products_enumerate = enumerate(products)  # enumerate object

print(products_enumerate)
print(type(products_enumerate))

for product in products_enumerate:
    print(product)
    # print(type(product)) # tuple
    print(product[1])

list_products_enumerate = list(
    products_enumerate
)  # converting the enumerate object to a list of tuples
print(list_products_enumerate)  # [] # itertor is exhausted
