import timeit

# 1. Plus operator
my_name = "Bogdan"
my_hobby = "running"
time = 8

info = my_name + " likes " + my_hobby + " at " + str(time) + " o'clock"
print(info)

# 2. f-string (new way: 3.6+) : fastest
my_name = "Bogdan"
my_hobby = "running"
time = 8

info = f"{my_name} likes {my_hobby} at {time} o'clock"
print(info)

# 3. format string method (old way: 2.7 - 3.0)
my_name = "Bogdan"
my_hobby = "running"
time = 8

info = "{} likes {} at {} o'clock".format(my_name, my_hobby, time)
print(info)

# 4. string interpolation (oldest way)
info = "%s likes %s at %s o'clock" % (my_name, my_hobby, time)
print(info)

# ----------------------------
# Performance Test
# ----------------------------
# '+' operator
format_time = timeit.timeit(
    'my_name + " likes " + my_hobby + " at " + str(time) + " o\'clock"',
    globals=globals(),
    number=1000000,
)
print(f"'+' operator: {format_time:.6f} seconds")

# str.format()
format_time = timeit.timeit(
    '"{} likes {} at {} o\'clock".format(my_name, my_hobby, time)',
    globals=globals(),
    number=1000000,
)
print(f"str.format(): {format_time:.6f} seconds")

# % string interpolation is faster than str.format()
format_time = timeit.timeit(
    '"%s likes %s at %s o\'clock" % (my_name, my_hobby, time)',
    globals=globals(),
    number=1000000,
)
print(f"% string interpolation: {format_time:.6f} seconds")

# f-string is the fastest
format_time = timeit.timeit(
    'f"{my_name} likes {my_hobby} at {time} o\'clock"',
    globals=globals(),
    number=1000000,
)
print(f"f-string: {format_time:.6f} seconds")
