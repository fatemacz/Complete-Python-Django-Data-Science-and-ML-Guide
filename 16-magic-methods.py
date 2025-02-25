print(dir(str))


print(str.__doc__)
print(bool.__doc__)


my_num = 10
other_num = 20

print(help(my_num.__eq__))

print(my_num.__eq__(other_num))
print(my_num == other_num)

print(help(my_num.__add__))
