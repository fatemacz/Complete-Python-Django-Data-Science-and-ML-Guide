# unorder collection of unique elements
# set is mutable, unordered, unindexed, iterable
# set is collection of unique elements
my_set = {10, 5, 5, 100, 10, 20}

print(my_set)
print(type(my_set))
print(isinstance(my_set, set))
print(len(my_set))
print(id(my_set))
print()

my_set.add(30)
print(my_set)
print(id(my_set))
print()

my_set.remove(5)
print(my_set)
print(id(my_set))
print()

my_set[0]  # TypeError: 'set' object is not subscriptable


my_list = [10, 5, 5, 100, 10, 20]
print(my_list.__getitem__(3))

my_str = "asdfasdfads"
print(my_str.__getitem__(6))


my_set = set()  # empty set, not with {}
print(my_set)
print(type(my_set))


# Mutable objects in set
# ----------------------
# Set is mutable, but it cannot contain mutable objects.
my_set = {
    {"name": "Aye", "age": 30},
    {"name": "John", "age": 25},
}  # TypeError: unhashable type: 'dict'
my_set = {{1, 2, 3}, {4, 5, 6}}  # TypeError: unhashable type: 'set'
my_set = {[1, 2, 3], [4, 5, 6]}  # TypeError: unhashable type: 'list'
my_set = {10, True, "abc", [1, 2]}  # TypeError: unhashable type: 'list'

my_set = {(1, 2, 3), (4, 5, 6)}  # OK, tuple is immutable
print(my_set)
print

# Deleting element from set
# -------------------------
del my_set[0]  # TypeError: 'set' object doesn't support item deletion
