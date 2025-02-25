screen_res = (1920, 1080, 2160)
print(id(screen_res))
print(screen_res)

screen_res = (1920, 1080)
print(id(screen_res))
print(screen_res)

print(type(screen_res))
print(isinstance(screen_res, tuple))
print(id(screen_res))


print(screen_res.count(1080))
print(screen_res.index(1080))

screen_res_list = list(screen_res)
screen_res_list[0] = 1444
print(screen_res_list)

screen_res = tuple(screen_res_list)
print(screen_res)
print(id(screen_res))


screen_res = (1920, 1080)
screen_info = (True, "Samsung", 150)

screen_data = screen_res + screen_info
print(screen_data)
print(screen_res)
print(screen_info)

print(screen_data[0])
print(screen_data[-1])
print(len(screen_data))

# Mutable objects in tuple
# -------------------------
# Tuple is immutable, but it can contain mutable objects.
# This means that we can change the values of mutable objects inside the tuple.
# However, we cannot change the tuple itself.

users = ({"name": "Bogdan", "age": 30}, {"name": "John", "age": 25})
print(users)
print("tuple id: ", id(users))
print()
print("users[0]        : ", users[0])
print("users[0] id     : ", id(users[0]))
users[0]["age"] = 31
print("updated users[0]: ", users[0])
print("users[0] id     : ", id(users[0]))
print()
print(users)
print("tuple id: ", id(users))
