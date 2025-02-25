import sys

print(sys.argv)
print(sys.version_info)
print(sys.version)

if len(sys.argv) < 3:
    raise IOError("You must provide username and password!")

# username = sys.argv[1]
# password = sys.argv[2]
# print(username, password)

_, username, password = sys.argv
print(username, password)
