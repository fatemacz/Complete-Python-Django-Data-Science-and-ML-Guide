# --------------------
# 1. Required parameters and keyword arguments
# --------------------
def product_price_info(product_title, product_price):
    print(f"{product_title} costs {product_price}$")


# product_price_info("Bottle of water", 2)
product_price_info(product_title="Bottle of water", product_price=2)


# --------------------
# 2. Gathering all keyword arguments into a dictionary
# --------------------
def product_price_info(**product):
    print(product)


product_price_info(
    product_title="Bottle of water", product_price=2, product_availability=True
)


# --------------------
# 3. Accessing values of the dictionary in the function
# --------------------
def product_price_info(**product):
    print(f"{product['product_title']} costs {product['product_price']}$")


product_price_info(product_title="Bottle of water", product_price=2)


# --------------------
# 4. Assigning values from the dictionary to the variables
# --------------------
def product_price_info(**product):
    """
    keyword arguments: product_title, product_price
    """
    title = product["product_title"]
    price = product["product_price"]
    print(f"{title} costs {price}$")


product_price_info(product_title="Bottle of water", product_price=2)


# --------------------
# Task-1
# --------------------
def merge_lists_to_dict(**kwargs):
    return dict(zip(kwargs["dict_keys_list"], kwargs["dict_values_list"]))


keys_list = ["name", "age", "city"]
values_list = ["Alice", 25, "New York"]
print(merge_lists_to_dict(dict_keys_list=keys_list, dict_values_list=values_list))
# {'name': 'Alice', 'age': 25, 'city': 'New York'}

print(merge_lists_to_dict(keys_list, dict_values_list=values_list))
# TypeError: merge_lists_to_dict() takes 0 positional arguments but 1 was given


# --------------------
# Task-2
# --------------------
def update_car_info(**kwargs):
    kwargs["is_available"] = True
    return kwargs


print(update_car_info(brand="Mazda", price=6000))
