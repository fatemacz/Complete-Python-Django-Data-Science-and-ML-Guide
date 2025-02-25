# 1. Creating a timer using "while" loop
import time

seconds_qty = 5

while seconds_qty > 0:
    print(f"Timer: {seconds_qty} seconds remaining...")
    seconds_qty -= 1
    time.sleep(1)

print("Timer is up!")


# 2. Asking user for the username in the "while" loop
username = ""

while not username:
    entered_username = input("Please enter your username: ")
    if len(entered_username) > 3:
        username = entered_username
    else:
        print("Username is too short. Must be more than 3 characters!")

print(f"Welcome, {username}")


# 3. Asking for user input to start or load the game in the "while" loop
selected_option = 0

while selected_option not in range(1, 4):
    print("Menu:")
    print("1. Start the game")
    print("2. Load saved game")
    print("3. Quit")
    try:
        selected_option = int(input("Please enter your choice (1-3): "))
    except ValueError as e:
        print(e)
        print("Try to select option once again")

if selected_option == 1:
    print("Starting the game...")
if selected_option == 2:
    print("Loading the game...")
if selected_option == 3:
    print("Quitting...")
