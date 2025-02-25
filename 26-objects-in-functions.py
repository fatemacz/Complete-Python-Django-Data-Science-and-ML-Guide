# ----------------------------
# 1. Mutable object as function arguments
# ----------------------------
def print_fruits_info(person_name, fruits):
    fruits.pop()  # remove the last element

    for fruit in fruits:
        print(f"{person_name} likes {fruit}")


my_name = "Bogdan"
favorite_fruits = ["oranges", "apples", "bananas"]
print(favorite_fruits)

print_fruits_info(my_name, favorite_fruits)
print(favorite_fruits)


# # ----------------------------
# def print_fruits_info(person_name, fruits):
#     print(f"fruits inside function: {fruits} with id: {id(fruits)}")

#     print("Removing the last element from fruits")
#     fruits.pop()  # remove the last element
#     print(f"fruits inside function: {fruits} with id: {id(fruits)}")
#     for fruit in fruits:
#         print(f"{person_name} likes {fruit}")


# my_name = "Bogdan"
# favorite_fruits = ["oranges", "apples", "bananas"]
# print(f"favorite_fruits b4 func call: {favorite_fruits} with id: {id(favorite_fruits)}")

# print_fruits_info(my_name, favorite_fruits)
# print(
#     f"favorite_fruits after func call: {favorite_fruits} with id: {id(favorite_fruits)}"
# )


# ----------------------------
# 2. Immutable objects as function arguments
# ----------------------------
def print_fruits_info(person_name, fruits):
    person_name = "Alice"
    fruits.pop()

    for fruit in fruits:
        print(f"{person_name} likes {fruit}")


favorite_fruits = ["oranges", "apples", "bananas"]
my_name = "Bogdan"
print(my_name)

print_fruits_info(my_name, favorite_fruits)
print(my_name)


# # ----------------------------
# def print_fruits_info(person_name, fruits):
#     print(f"person_name inside function: {person_name} with id: {id(person_name)}")

#     print("Changing the value of person_name")
#     person_name = "Alice"  # new memory address
#     print(f"person_name inside function: {person_name} with id: {id(person_name)}")
#     print()

#     fruits.pop()
#     for fruit in fruits:
#         print(f"{person_name} likes {fruit}")


# favorite_fruits = ["oranges", "apples", "bananas"]
# my_name = "Bogdan"
# print(f"my_name b4 func call: {my_name} with id: {id(my_name)}")

# print_fruits_info(my_name, favorite_fruits)
# print(f"my_name after func call: {my_name} with id: {id(my_name)}")


# ----------------------------
# 3. Making a copy of them mutable object in the function
# ----------------------------
# ***It is not recommended to change external objects inside the function.***
def print_fruits_info(person_name, fruits):
    fruits_copy = fruits.copy()  # new memory address
    fruits_copy.pop()

    for fruit in fruits_copy:
        print(f"{person_name} likes {fruit}")

    return fruits_copy


my_name = "Bogdan"
favorite_fruits = ["oranges", "apples", "bananas"]
print(favorite_fruits)
new_favorite_fruits = print_fruits_info(my_name, favorite_fruits)
print(new_favorite_fruits)
print(favorite_fruits)


# # ----------------------------
# def print_fruits_info(person_name, fruits):
#     print(f"fruits inside function      : {fruits} with id: {id(fruits)}")

#     fruits_copy = fruits.copy()  # create a copy of mutable object
#     print(f"fruits_copy inside function : {fruits_copy} with id: {id(fruits_copy)}")

#     print("Removing the last element from fruits_copy")
#     fruits_copy.pop()
#     print(f"fruits_copy inside function : {fruits_copy} with id: {id(fruits_copy)}")
#     for fruit in fruits_copy:
#         print(f"{person_name} likes {fruit}")


# my_name = "Bogdan"
# favorite_fruits = ["oranges", "apples", "bananas"]
# print(f"favorite_fruits b4 func call: {favorite_fruits} with id: {id(favorite_fruits)}")
# print_fruits_info(my_name, favorite_fruits)
# print(
#     f"favorite_fruits after func call: {favorite_fruits} with id: {id(favorite_fruits)}"
# )


# ----------------------------
# Task
# ----------------------------
def merge_lists_to_dict(list_1, list_2):
    return dict(zip(list_1, list_2))


keys_list = ["name", "age", "city"]
values_list = ["Alice", 25, "New York"]
print(merge_lists_to_dict(keys_list, values_list))
# Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
