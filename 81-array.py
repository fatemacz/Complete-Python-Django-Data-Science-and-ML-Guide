from array import array

# 1. Create array, add and remove elements
my_int_array = array('i', [10, 4, 3, 7, 9, 15])

print(my_int_array)
print(type(my_int_array))
print(dir(my_int_array))
print(my_int_array[2])
my_int_array.append(20)
print(my_int_array)
# my_int_array.append(10.5)
my_int_array.append(True)
print(my_int_array)
my_int_array.pop(0)
print(my_int_array)


# 2. Save array to the file and load from the file
my_int_array = array('i', [10, 4, 3, 7, 9, 15])

with open('my_array.bin', 'wb') as file:
    my_int_array.tofile(file)

imported_array = array('i')
with open('my_array.bin', 'rb') as file:
    imported_array.fromfile(file, 3)
    print(imported_array)
