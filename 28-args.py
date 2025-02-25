# ----------------------------
# 1. Gathering all positional arguments into a tuple
# ----------------------------
def sort_nums(*args):
    print(args)
    print(type(args))  # <class 'tuple'>


sort_nums(10, 3, 15, 246, 23)


# ----------------------------
# 2. Iteration of the tuple with all positional arguments
# ----------------------------
def sort_nums(*nums):
    for num in nums:
        print(num)


sort_nums(10, 3, 15, 246, 23)


# ----------------------------
# 3. Sorting all positional arguments in the function
# ----------------------------
def sort_nums(*args):
    print(args)
    return sorted(args)


sorted_nums = sort_nums(10, 3, 15, 246, 23)
print(sorted_nums)

sorted_nums = sort_nums(377, 23, 3)
print(sorted_nums)
