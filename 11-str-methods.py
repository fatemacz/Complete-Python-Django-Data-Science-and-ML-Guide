my_comment = "This is my short comment"
print(my_comment)
print(len(my_comment))
print(my_comment.count(" "))
print(my_comment.count("is"))
print(my_comment[0])
print(my_comment[:-1])
print(my_comment[2:])
print(my_comment[2:-10])
print(my_comment[2:9])
print(my_comment.find("short"))
print(my_comment.find("long"))
print(my_comment.find("long") == -1)
print(my_comment.split(" "))
print(my_comment.upper())
print(my_comment.lower())
print(dir(my_comment))

print(my_comment[::-1])

my_comment = my_comment.replace("short", "long")

print(my_comment)
print(id(my_comment))

my_comment = my_comment.title()
print(my_comment)
print(id(my_comment))

# print(dir())
# print(dir(__builtins__))
