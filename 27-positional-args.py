# ----------------------------
# 1. Matching quantity of the arguments and parameters
# ----------------------------
def my_fn(first, second):
    print(first)
    print(second)


my_fn(None, 10)  # OK


# ----------------------------
# 2. Arguments and parameters quantities mismatch
# ----------------------------
def my_fn(first, second):
    print(first)
    print(second)


my_fn(None)  # TypeError: my_fn() missing 1 required positional argument: 'second'


# ----------------------------
# 3. Default value for the parameter makes it optional
# ----------------------------
def my_fn(first, second=True):
    print(first)
    print(second)


my_fn(None)  # OK
# my_fn(None, 10)  # OK
# my_fn(None, 10, 15)  # TypeError: my_fn() takes from 1 to 2 positional arguments but 3 were given
