long_str = "This is a very long string"

long_str = "It's a great day today"
# long_str = 'It\'s a great day today'

long_str = "This is a " "very long " "string"
# long_str = "This is a " \
#             "very long " \
#             "string"

long_str = """This is to show a very, very,
    very, very, very, very, very,
 very, very, very, very, very, very,
very, very, very, very, very, very long string"""

# print(dir(long_str))

print(long_str)
print(type(long_str))
print(type(long_str) == str)
print(id(long_str))

long_str = "a b c"
print(long_str)
print(len(long_str))
print(id(long_str))
