my_nums = [10, 3, 100, 35]

print(dir(my_nums))
print(dir(__builtins__))

print(my_nums)
print(len(my_nums))
my_nums.pop(2)
print(my_nums)
print(len(my_nums))


my_nums = [10, 3, 100, 35]

my_nums.extend([34, 62])
print(my_nums)


my_nums = [10, 3, 100, 35, 100]
print(my_nums.index(100))


my_nums = [10, 3, 100, 35, 100]

my_nums.clear()
print(my_nums)
my_nums.append(50)
print(my_nums)


my_nums = [10, 3, 100, 35, 100]
other_nums = [351, 245, 425]

merged_nums = my_nums + other_nums
# merged_nums = my_nums.__add__(other_nums)
print(merged_nums)
print(my_nums)
print(other_nums)


my_nums = [10, 3, 100, 35, 100]

my_nums[2] = 0
print(my_nums)


my_list = [True, None, "abc", 10, 10.5, [1, 2], {"name": "Bogdan"}]
print(my_list)

# delete element from list
# -------------------------
# The del keyword is used to delete objects.
# In Python everything is an object, so the del keyword can also be used to delete variables, lists, or parts of a list etc.
list1 = [1, 2, 3]
print(list1)
del list1[1]
print(list1)

# using variables in lists
# ------------------------
fruit_1 = "apple"
fruit_2 = "banana"
fruit_3 = "cherry"
print("Fruit 1: ", fruit_1)
print("Fruit 1 ID: ", id(fruit_1))
print()

fruits = [fruit_1, fruit_2, fruit_3]
print("Fruit 1 assigned to List")
print(fruits)
print("Fruit 1 in List: ", fruits[0])
print("Fruit 1 ID in List: ", id(fruits[0]))
print()

fruit_1 = "kiwi"
print("Fruit 1 value changed")
print("Fruit 1: ", fruit_1)
print("Fruit 1 ID: ", id(fruit_1))
print()

print(fruits)
print("Fruit 1 in List: ", fruits[0])
print("Fruit 1 ID in List: ", id(fruits[0]))
print()

fruits = [fruit_1, fruit_2, fruit_3]
print("Fruit 1 reassigned to List")
print(fruits)
print("Fruit 1 in List: ", fruits[0])
print("Fruit 1 ID in List: ", id(fruits[0]))

print()
del fruit_1
print("Fruit 1 Deleted")
print(fruits)
print("Fruit 1 in List: ", fruits[0])
print("Fruit 1: ", fruit_1)
