# ----------------------------
# 1. Keyword arguments in the function call
# ----------------------------
def comments_info(comments_qty, day):
    print(f"{comments_qty} comments were posted on {day}")


# Positional arguments
comments_info(10, "Friday")

# Keyword arguments
comments_info(comments_qty=50, day="Monday")
comments_info(day="Monday", comments_qty=50)

# Mixed arguments
comments_info(20, day="Sunday")  # OK. Positional first
# comments_info(20, comments_qty=50)            # TypeError: comments_info() got multiple values for argument 'comments_qty'

# comments_info(comments_qty=50, "Monday")      # SyntaxError: positional argument follows keyword argument
# comments_info(day='Sunday', 20)               # SyntaxError: positional argument follows keyword argument


# ----------------------------
# 2. Keyword arguments can't be gathered into the args tuple
# ----------------------------
# if there is only *arg parameter for the function, you are not allowed to use any keyword arguments
def comments_info(*args):
    print(f"{args[0]} comments were posted on {args[1]}")


# Positional arguments
comments_info(10, "Friday")

# Keyword arguments
# comments_info(comments_qty=50, day="Monday")   # TypeError: comments_info() got an unexpected keyword argument 'comments_qty'
# comments_info(day="Monday", comments_qty=50)   # TypeError: comments_info() got an unexpected keyword argument 'day'

# Mixed arguments
# comments_info(50, day="Monday")                # TypeError: comments_info() got an unexpected keyword argument 'day'
# comments_info(comments_qty=50, "Monday")       # SyntaxError: positional argument follows keyword argument


# ----------------------------
# 3. Gathering all keyword arguments into a dictionary
# ----------------------------
def comments_info(**kwargs):
    print(kwargs)
    print(type(kwargs))  # <class 'dict'>

    print(f"{kwargs['comments_qty']} comments were posted on {kwargs['day']}")

    # For non-existing key, use get() method to return default value and avoid KeyError
    # print(f"Special Note: {kwargs['special_note']}")  # KeyError: 'special_note'
    print(f"Special Note: {kwargs.get('special_note', 'N/A')}")


# Keyword arguments
comments_info(comments_qty=50, day="Monday", extra="")  # OK. Order doesn't matter
# comments_info(day="Monday", comments_qty=50)  # OK. Order doesn't matter

# Positional arguments
# comments_info(10, "Friday")              # TypeError: comments_info() takes 0 positional arguments but 2 were given

# Mixed arguments
# comments_info(20, day="Sunday")          # TypeError: comments_info() takes 0 positional arguments but 1 was given
# comments_info(comments_qty=50, "Monday") # SyntaxError: positional argument follows keyword argument


# # ----------------------------
# def comments_info(**kwargs):
#     print(kwargs)
#     print(type(kwargs))  # <class 'dict'>

#     info = f"{kwargs['comments_qty']} comments were posted " f"on {kwargs['day']}"
#     # info = (
#     #     f"{kwargs['comments_qty']} comments were posted "
#     #     f"on {kwargs['day']}"
#     # ) # Same as above, without 'comma', python will concatenate the strings
#     return info


# info = comments_info(comments_qty=10, day="Friday")
# print(info)
