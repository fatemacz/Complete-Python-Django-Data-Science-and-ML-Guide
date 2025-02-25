c = True
e = False


def mult(a, b):
    c = a * b
    d = True
    print(dir())
    return c


print(mult(100, 30))
print(dir())


# -------------------------
# Scopes
# -------------------------
a = 10
c = 15


def my_fn():
    a = 20
    b = True
    print(a)  # 20
    print(b)  # True
    print(c)  # 15


my_fn()  # 20, True, 15
print(a)  # 10
print(b)  # NameError: name 'b' is not defined
print(c)  # 15


# -------------------------
# Scope Chain
# -------------------------
a = 10


def my_fn():
    def inner_fn():
        def inner_inner_fn():
            print(a)

        inner_inner_fn()

    inner_fn()


my_fn()


# -------------------------
# Creating global variables from within a function
# -------------------------
def my_fn():
    global a
    a = 5


my_fn()
print(a)  # 5


# -------------------------
# Using global variable in a function
# -------------------------
a = 10


def my_fn():
    global a
    a = 20


my_fn()
print(a)  # 20


# # -------------------------
# a = 10
# print(f"a inside global scope    : {a} with id: {id(a)}")


# def my_fn():
#     global a
#     print(f"a inside b4 update       : {a} with id: {id(a)}")
#     a = 20
#     print(f"a inside after update    : {a} with id: {id(a)}")


# my_fn()
# print(f"a inside after func call : {a} with id: {id(a)}")
# print(a)  # 20
