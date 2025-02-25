from pathlib import Path

# 1. File must be closed after each operation
file_path = 'my_file.txt'

file = open(file_path, 'w')

print(file)
print(type(file))

file.write("First line\n")
file.write("Second line\n")

file.close()

file = open(file_path)

print(file.read())


# 2. "with" statement closes the file automatically
file_path = 'my_file.txt'

with open(file_path, 'w') as file:
    file.write("First line\n")
    file.write("Second line\n")

with open(file_path) as file:
    print(file.read())


# 3. "readlines" reads the file into the list of strings
file_path = 'my_file.txt'

with open(file_path, 'w') as file:
    file.write("First line\n")
    file.write("Second line\n")

with open(file_path) as file:
    for line in file.readlines():
        print(line.strip())


# 4. "readline" is good for big files as it reads the file line by line
file_path = 'my_file.txt'

with open(file_path, 'w') as file:
    file.write("First line\n")
    file.write("Second line\n")

with open(file_path) as file:
    while True:
        line = file.readline()
        if not line:
            break
        print(line.strip())


# 5. Append to the file and delete file at the end
file_path = Path('my_file.txt')

with open(file_path, 'w') as file:
    file.write("First line\n")
    file.write("Second line\n")

with open(file_path) as file:
    print(file.read())

with open(file_path, 'a') as file:
    file.write("Third line\n")

with open(file_path) as file:
    print(file.read())

if file_path.exists():
    file_path.unlink()
