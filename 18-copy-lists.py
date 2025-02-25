my_list = [10, 'abc', True]

# OPTION 1
copy_of_my_list = my_list[:]

# # OPTION 2
# copy_of_my_list = my_list.copy()

# # OPTION 3
# copy_of_my_list = list(my_list)

copy_of_my_list.append(100)
print(my_list)
print(copy_of_my_list)
print(id(my_list) == id(copy_of_my_list))
print(id(my_list))
print(id(copy_of_my_list))
