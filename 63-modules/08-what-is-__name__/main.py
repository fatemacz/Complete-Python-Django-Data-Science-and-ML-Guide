import other

print("MODULE NAME: MAIN")

# print(dir())
# print(__name__)
# print(type(__name__))

print('MAIN', __name__)
print('MAIN', __name__ == '__main__')

if __name__ == '__main__':
    print('MAIN:', 'ONLY IF RUN DIRECTLY')
