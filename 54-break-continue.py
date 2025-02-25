# 1. Breaking the "while" loop
user_password = "admin123"
password = ""

while password != user_password:
    print("Enter 'quit' in order to exit from login")
    password = input("Please enter your password: ")
    if password == "quit":
        print("Quitting...")
        break

if password == user_password:
    print("Login successful!")
else:
    print("Login failed")


# 2. Breaking the "for in" loop
my_list = [10, 5, 2, 100, 35]

for num in my_list:
    if num == 2:
        break
    print(num)


# 3. "break" and "continue" in the loop
current_usernames = ["bogdan123", "bob1", "alice75"]

while True:
    username = input("Please enter desired username: ")

    if username in current_usernames:
        print("Username is already taken. Try again")
        continue  # This will skip the rest of the code and go back to the beginning of the loop

    current_usernames.append(username)
    break  # This will break the while loop

print("User registration complete.")
print(current_usernames)
