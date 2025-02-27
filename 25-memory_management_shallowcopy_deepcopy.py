# ----------------------------
# 1. Memory management in Python
# ----------------------------

# 1.1. Immutable objects with the same object (value) are stored in the same memory address
# ----------------------------
my_number = 10  # 10 in this case is an int object
print(f"my_number: {my_number} with id: {id(my_number)}")

other_number = 10  # other_number references the same memory address as my_number because of the same object (value)
print(f"other_number: {other_number} with id: {id(other_number)}")

print(f"int object: 10 with id: {id(10)}")
print()


# 1.2. Immutable objects with different object (value) are stored in different memory addresses
# ----------------------------
first_number = 10  # 10 in this case is an int object
second_number = first_number  # Immutable objects referencing same memory address
print(f"first_number: {first_number} with id: {id(first_number)}")
print(f"second_number: {second_number} with id: {id(second_number)}")
print()

second_number += 5  # 15 - new memory address
third_number = 15  # third_number references the same memory address as second_number because of the same object (value)
fourth_number = 10  # fourth_number references the same memory address as first_number because of the same object (value)
print(f"first_number: {first_number} with id: {id(first_number)}")
print(f"fourth_number: {fourth_number} with id: {id(fourth_number)}")
print(f"second_number: {second_number} with id: {id(second_number)}")
print(f"third_number: {third_number} with id: {id(third_number)}")
print()


# 1.3. Mutable objects with the same value are stored in the different memory address
# ----------------------------
# list
# ----------------------------
my_list = [1, 2, 3]
print(f"my_list         : {my_list} with id: {id(my_list)}")

# my_list_copy_ref references the same memory address as my_list
my_list_copy_ref = my_list
print(f"my_list_copy_ref: {my_list_copy_ref} with id: {id(my_list_copy_ref)}")

# my_list_copy is a new list with the same value, but different memory address
my_list_copy = my_list.copy()
print(f"my_list_copy    : {my_list_copy} with id: {id(my_list_copy)}")

# same value, but different memory address
other_list = [1, 2, 3]
print(f"other_list      : {other_list} with id: {id(other_list)}")

print(f"[1, 2, 3]       : [1, 2, 3] with id: {id([1 , 2, 3])}")
print()

my_list_copy_ref.append(4)
my_list_copy.append(5)
print(f"my_list         : {my_list} with id: {id(my_list)}")
print(f"my_list_copy_ref: {my_list_copy_ref} with id: {id(my_list_copy_ref)}")
print(f"my_list_copy    : {my_list_copy} with id: {id(my_list_copy)}")


# ----------------------------
# dict
# ----------------------------
my_dict = {"name": "Aye", "age": 30}
print(f"my_dict         : {my_dict} with id: {id(my_dict)}")

# my_dict_copy_ref references the same memory address as my_dict
my_dict_copy_ref = my_dict
print(f"my_dict_copy_ref: {my_dict_copy_ref} with id: {id(my_dict_copy_ref)}")

# my_dict_copy is a new dict with the same value, but different memory address
my_dict_copy = my_dict.copy()
print(f"my_dict_copy    : {my_dict_copy} with id: {id(my_dict_copy)}")

# same value, but different memory address
my_other_dict = {"name": "Aye", "age": 30}
print(f"my_other_dict   : {my_other_dict} with id: {id(my_other_dict)}")
print()

my_dict_copy_ref["reference"] = "updated"
my_dict["original"] = "updated"
my_dict_copy["copy"] = "updated"
my_other_dict["other"] = "updated"
print(f"my_dict         : {my_dict} with id: {id(my_dict)}")
print(f"my_dict_copy_ref: {my_dict_copy_ref} with id: {id(my_dict_copy_ref)}")
print(f"my_dict_copy    : {my_dict_copy} with id: {id(my_dict_copy)}")
print(f"my_other_dict   : {my_other_dict} with id: {id(my_other_dict)}")


# ----------------------------
# set
# ----------------------------
my_set = {10, 20, 30}
print(f"my_set         : {my_set} with id: {id(my_set)}")

# my_set_copy_ref references the same memory address as my_set
my_set_copy_ref = my_set
print(f"my_set_copy_ref: {my_set_copy_ref} with id: {id(my_set_copy_ref)}")

# my_set_copy is a new set with the same value, but different memory address
my_set_copy = my_set.copy()
print(f"my_set_copy    : {my_set_copy} with id: {id(my_set_copy)}")

# same value, but different memory address
my_other_set = {10, 20, 30}
print(f"my_other_set   : {my_other_set} with id: {id(my_other_set)}")
print()

my_set_copy_ref.add(40)
my_set_copy.add(50)
my_other_set.add(60)
print(f"my_set         : {my_set} with id: {id(my_set)}")
print(f"my_set_copy_ref: {my_set_copy_ref} with id: {id(my_set_copy_ref)}")
print(f"my_set_copy    : {my_set_copy} with id: {id(my_set_copy)}")
print(f"my_other_set   : {my_other_set} with id: {id(my_other_set)}")


# ----------------------------
# 2. Shallow copy - The mutation of mutable objects in the copies: "reviews": [] and "pref": {} in this case
# ----------------------------
print("Shallow Copy")
print("-------------")
info = {
    "name": "Aye",
    "is_instructor": True,
    "reviews": [],
    "pref": {},
}
info_copy = info.copy()

print(f"info                 : {info} with id: {id(info)}")
print(f"info_copy            : {info_copy} with id: {id(info_copy)}")
print(f"info['reviews']      : {info['reviews']} with id: {id(info['reviews'])}")
print(
    f"info_copy['reviews'] : {info_copy['reviews']} with id: {id(info_copy['reviews'])}"
)
print(f"info['pref']         : {info['pref']} with id: {id(info['pref'])}")
print(f"info_copy['pref']    : {info_copy['pref']} with id: {id(info_copy['pref'])}")
print()

info_copy["reviews"].append("Great course!")
info_copy["pref"]["food"] = "burger"

info["reviews"].append("Thanks!")
info["pref"]["sports"] = "football"

print(f"info                 : {info} with id: {id(info)}")
print(f"info_copy            : {info_copy} with id: {id(info_copy)}")
print(f"info['reviews']      : {info['reviews']} with id: {id(info['reviews'])}")
print(
    f"info_copy['reviews'] : {info_copy['reviews']} with id: {id(info_copy['reviews'])}"
)
print(f"info['pref']         : {info['pref']} with id: {id(info['pref'])}")
print(f"info_copy['pref']    : {info_copy['pref']} with id: {id(info_copy['pref'])}")
print()


# ----------------------------
# 3. Deepcopy - Avoiding mutation of mutable objects in the copies: "reviews": [] and "pref": {} in this case
# ----------------------------
from copy import deepcopy

print("Deep Copy")
print("-------------")
info = {
    "name": "Aye",
    "is_instructor": True,
    "reviews": [],
    "pref": {},
}
info_deepcopy = deepcopy(info)

print(f"info                     : {info} with id: {id(info)}")
print(f"info_deepcopy            : {info_deepcopy} with id: {id(info_deepcopy)}")
print(f"info['reviews']          : {info['reviews']} with id: {id(info['reviews'])}")
print(
    f"info_deepcopy['reviews'] : {info_deepcopy['reviews']} with id: {id(info_deepcopy['reviews'])}"
)
print(f"info['pref']             : {info['pref']} with id: {id(info['pref'])}")
print(
    f"info_deepcopy['pref']    : {info_deepcopy['pref']} with id: {id(info_deepcopy['pref'])}"
)
print()

info_deepcopy["reviews"].append("Great course!")
info_deepcopy["pref"]["food"] = "burger"

info["reviews"].append("Thanks!")
info["pref"]["sports"] = "football"

print(f"info                     : {info} with id: {id(info)}")
print(f"info_deepcopy            : {info_deepcopy} with id: {id(info_deepcopy)}")
print(f"info['reviews']          : {info['reviews']} with id: {id(info['reviews'])}")
print(
    f"info_deepcopy['reviews'] : {info_deepcopy['reviews']} with id: {id(info_deepcopy['reviews'])}"
)
print(f"info['pref']             : {info['pref']} with id: {id(info['pref'])}")
print(
    f"info_deepcopy['pref']    : {info_deepcopy['pref']} with id: {id(info_deepcopy['pref'])}"
)
print()
