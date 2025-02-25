counter = 0


def inc_counter(value=1):
    """
    Increments value

    :param int value: Increment counter by value
    """
    global counter
    counter += value


def dec_counter(value=1):
    """
    Decrements value

    :param int value: Decrement counter by value
    """
    global counter
    counter -= value


inc_counter(5)
print(counter)
inc_counter(2)
print(counter)
dec_counter()
print(counter)
