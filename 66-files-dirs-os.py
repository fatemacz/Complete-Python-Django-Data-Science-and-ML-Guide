# NOTE: CREATE FEW FILES IN THE my_test_directory AFTER FIRST CODE RUN
import os

# Directory path
directory_path = 'my_test_directory'


# Check if directory exists
if not os.path.exists(directory_path):
    # Create directory
    os.mkdir(directory_path)
    print("Directory was created: ", directory_path)
else:
    print("Directory exists: ", directory_path)


# Creating path to the file
file_path = os.path.join(directory_path, 'my_file.txt')
print("File path: ", file_path)


# Getting parent directory
parent_dir = os.path.dirname(file_path)
print("Parent directory: ", parent_dir)


# Checking if the file is file path or dir path
is_file = os.path.isfile(file_path)
is_dir = os.path.isdir(directory_path)
print(f"{file_path} is file: ", is_file)
print(f"{directory_path} is directory: ", is_dir)


# Listing files in the directory
dir_files = os.listdir(directory_path)
print(f"Files in the directory {directory_path}: ")
print(dir_files)
for file in dir_files:
    print(file)


# Removing directory
if os.path.exists(directory_path):
    dir_files = os.listdir(directory_path)
    for file in dir_files:
        os.remove(os.path.join(directory_path, file))
    os.rmdir(directory_path)
    print(f"Directory {directory_path} was removed")
