# BigAndSmall Numbers Game Python Program
# Code Challenge 02
# CIT-95

# Import Section
# TODO: Basic 01)
#  Import the NumPy Python library to help with arrays. You may nave to install the numpy package before
#  importing the library (in PyCharm...File/Settings/Python Project/Python Interpreter/Search for NumPy/Click Install)
import numpy as np

# Variable Declaration Section
# TODO: Basic 02)
#   1) Create two variables of data type NoneType. Name them: largest and smallest. They will eventually hold
#      the values of the largest and smallest input numbers. The NoneType defines a null value. Note this is not the
#      same as empty string, False, or zero. You cannot perform arithmetic on a null value, so these two variables must
#      change their data type before being used to hold the largest and smallest input numbers.
#   2) Create an array to hold the user's input. Name the array: user_int_array[] and initialize it with
#      20 elements - all with the value: 999.
#   3) Create a variable named num_of_try to keep track of the current loop iteration. You will need this variable
#      to fill in your user input array by overwriting the 999 with user input. Initialize this variable to 0.
#   4) Create an array to hold the user's non-int inputs named: user_string_array[] and initialize it with five
#      elements. This limits your program to five non-int input items from your user.

largest = None
smallest = None
user_int_array = np.array([999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999])
num_of_try = 0
user_str_array = np.array(["0000000000001", "00000000000002", "0000000000003", "0000000000004", "0000000000005"])


# Variable Initialization Section
#   The loop control variable and other control variables must be initialized outside the loop
#   to get the BigAndSmall Numbers Game properly started.
# TODO: Basic 03)
#   Create a flag variable named: cleanInput to signal that user input may proceed. Thinking about the program
#   specs, you will notice that the game must continue after receiving an invalid (not an integer) input from the
#   user. The Boolean flag variable named cleanInput will maintain the input state of the game. If the input state of
#   the game is True, then input may continue. If the input state of the game is False (because your program detected
#   a user input value that was not an int), your program must report this (print("Invalid Input")) and resume asking
#   another number. Fill user_input_array with 20 elements of 999. Because you are using a static array, and not a list, you will
#   use this array to hold the user's input values for output when your program ends.

# create flag variable
clean_input = None

# The cleanInput variable is used to skip to the end of the loop
# (but not break out of the loop). It is initialized to True and
# will become False when an input exception is caught.
# TODO: Initialize clean_input to True.
clean_input = True

# TODO: Basic 04)
#   Tell your user how your BidAndSmall Numbers game works. Say what "done" does and mention the maximum number of
#   numbers your game can handle (this is 20!).
print("\n\n Thanks for playing the BigAndSmall Numbers game. Enter up to 20 integers and enter done to")
print("   stop the game. To test exception handling, enter a couple strings e.g. 'hello' and 'there.'\n\n")

# num is our loop control variable. Loop control variables must be initialized,
# checked, and changed. The first prompt for a number from the user is made outside
# the loop to properly initialize the loop control variable named num
# This variable is also used to store the input integer.
# TODO: Prompt the user for a number and store the number into the variable named num.
num = input("Enter a number (\"done\" to stop): ")

# Both largest and smallest are assigned the value of num. They now have a value
# other than their initialized value of NoneType.
# TODO: initialize largest and smallest with the variable num (user input). Initialize num_of_try to 0.
largest = num
smallest = num
num_of_try = 0
num_of_user_strs = 0

# This loop will run until a break statement.
while (True):
    # Reset cleanInput to true so we can properly restart the input process.
    clean_input = True
    if (num == "done" or num_of_try == 20):
        break
    try:
        (isinstance(int(num),int))
    except:
        print("Invalid input")
        # Do not break here -- just note an invalid input action and move to the end of the loop
        # using the cleanInput flag.
        clean_input = False
        # Store the non-int input for later output
        user_str_array[num_of_user_strs] = num
        # increment num_of_user_strs to advance to the next element in user_str_array
        num_of_user_strs += 1

    if (clean_input):
        num = int(num)
        # print(num)
        if (int(num) > int(largest)):
            largest = num
        if (int(num) < int(smallest)):
            smallest = num
        user_int_array[num_of_try] = int(num)

    # We are at the end of the loop and this is where we
    #   add an element to our array,
    #   increment num_of_try, and
    #   change the loop control variable by asking for another input num!

    # increment num_of_try so you can advance to the next array element
    num_of_try = num_of_try + 1
    num = input("Enter a number (\"done\" to stop): ")

# We broke out of our loop because user input was "done." Output the largest and smallest to the user,
# and output the user input arrays.
#
# TODO: Advanced 01) Output the user-input arrays without the unused elements i.e. 999, 0000000000004.
# TODO: Advanced 02) Use a Python list instead of two arrays
# TODO: Advanced 03) Create this program without needing the try/except block
# TODO: Advanced 04) Use persistent storage (File I/O) to store user data -- who played the game and when, what was
#                    their big and small number
print()
print("************************************************************************************************")
print("****** Thank you for playing the Bid and Small Numbers game! Your results are below ************")
print("************************************************************************************************\n")
print("Largest number is ", largest)
print("Smallest number is ", smallest)

print("\nUser input was: ")
for item in user_int_array:
    print(item)
print("\n\n")
print("Invalid user input was: ")
for item in user_str_array:
    print(item)
print("\n\n")
