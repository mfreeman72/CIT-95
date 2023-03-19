# BigAndSmall Numbers Game Python Program
# Code Challenge 02
# CIT-95

# Import Section
# Importing datetime for storing when user played
from datetime import datetime

largest = None
smallest = None

# TODO: Advanced 02) Use a Python list instead of two arrays

user_int_list = [999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999]
user_str_list = ["0000000000001", "00000000000002", "0000000000003", "0000000000004", "0000000000005"]
num_of_try = 0

# Variable Initialization Section

# create flag variable
clean_input = True

# Introduce game
print("Welcome to Big and Small\n")
print("Enter any set of numbers. After 20 entries, or after typing 'done', the game will end.\n")
print("You will then be shown the biggest and smallest numbers you entered, as well as any invalid input.\n\n")

# Enter name
name = input("Please enter your name: ")

# Prompt user for input
num = input("Enter a number or type 'done': ")

#Initialize largest and smallest variables
largest = num
smallest = num
num_of_try = 0
num_of_user_strs = 0

# This loop will run until a break statement.
while (True):
    clean_input = True
    if (num == "done" or num_of_try == 20):
        break

    # TODO: Advanced 03) Create this program without needing the try/except block
    if (not num.isnumeric()):
        print("Invalid input")
        clean_input = False
        user_str_list[num_of_user_strs] = num
        num_of_user_strs += 1

    if (clean_input):
        num = int(num)
        if (int(num) > int(largest)):
            largest = num
        if (int(num) < int(smallest)):
            smallest = num
        user_int_list[num_of_try] = int(num)

    num_of_try = num_of_try + 1
    num = input("Enter a number or type 'done': ")

print("\nYour largest number was ", largest)
print("Your smallest number was ", smallest)

# TODO: Advanced 01) Output the user-input arrays without the unused elements i.e. 999, 0000000000004.
print("\nUser input was: ")
for item in user_int_list:
    if (item != 999):
        print(item)
print("\n\n")
print("Invalid user input was: ")
for item in user_str_list:
    if (item[0:11] != "00000000000"):
        print(item)
print("\n\n")

# TODO: Advanced 04) Use persistent storage (File I/O) to store user data -- who played the game and when, what was
#                    their big and small number

# Appending user data to "past_games.txt" file
now = datetime.now()
output = name + " -- " + now.strftime("%Y-%m-%d %H:%M:%S") + " -- Largest: " + str(largest) + " -- Smallest: " + str(smallest) + "\n"

try:
    add_game_to_file = open("past_games.txt","a")
    add_game_to_file.write(output)
    add_game_to_file.close()

except Exception as err:
    print("Could not open file:",err)

# Show previous user data from "past_games.txt" file
try:
    with open("past_games.txt","r") as read_past_games:
        game_data = "\nPast games:\n-----------"
        while game_data != "":
            print(game_data)
            game_data = read_past_games.readline()

except Exception as err:
    print("Could not open file:",err)
