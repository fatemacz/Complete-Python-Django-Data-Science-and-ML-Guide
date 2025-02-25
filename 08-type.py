my_num = 777
print(type(my_num) == int)  # True

# ----------------------------
# immutable objects
# ----------------------------
print(type(int))
print(type(float))
print(type(str))
print(type(bool))
print(type(tuple))
print(type(None))

print()

# ----------------------------
# mutable objects
# ----------------------------
print(type(list))
print(type(dict))
print(type(set))


# object of user-defined class
class MyClass:
    pass


print(type(MyClass()))
