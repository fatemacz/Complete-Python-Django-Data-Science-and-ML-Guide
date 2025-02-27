import json

# 1. list -> JSON array
my_nums = [10, 100, 5, 20]
my_nums_json = json.dumps(my_nums)
print(my_nums_json)
print(type(my_nums_json))


# 2. tuple -> JSON array
my_nums = (10, 100, 5, 20)
my_nums_json = json.dumps(my_nums)
print(my_nums_json)
print(type(my_nums_json))


# # 3. set -> JSON (not possible)
# my_nums = {10, 100, 5, 20}
# my_nums_json = json.dumps(my_nums)
# # TypeError: Object of type set is not JSON serializable


# 4. dict -> JSON object
my_post = {
    "title": "My post",
    "content": "Post content",
    "likes_qty": 25,
    "author": {"username": "Aye123", "email": "b@gmail.com"},
    "metadata": (5, 7, 20),
}
my_post_json = json.dumps(my_post)
print(my_post_json)
print(type(my_post_json))


# 5. JSON object -> dict
my_post_dict = json.loads(my_post_json)
print(my_post_dict)
print(type(my_post_dict))
print(my_post_dict["likes_qty"])


# 6. JSON array -> list
my_list = json.loads('[10, "abc", null, [1, 2], {"name": "Aye"}]')
print(my_list)


# # 7. dict with function (not possible)
# def sum_fn(a, b):
#     return a + b
#
#
# my_math = {
#     'title': "Math dict",
#     'sum': sum_fn
# }
#
# my_math_json = json.dumps(my_math)
# # TypeError: Object of type function is not JSON serializable


# 8. Format dictionary using JSON
my_dict = {"name": "Aye", "is_instructor": True}

print(my_dict)

my_dict_json = json.dumps(my_dict, indent=2)

file = open("test.txt", "w")
file.write(my_dict_json)
