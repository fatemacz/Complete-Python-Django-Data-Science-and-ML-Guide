c = True


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


def my_fn():
    a = 20
    b = True
    print(a)  # 20
    print(b)  # True


my_fn()  # 20, True
print(a)  # 10
print(b)  # NameError: name 'b' is not defined


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
