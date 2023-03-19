# fileSearch.py
# mF 10/20/22
#
#  In this code challenge you will search an email file and list all the senders of all email messages. Email format
#  is prefix@domain. For example: firstlast99@gmail.com -- firstlast99 is the prefix and gmail.com is the domain. For
#  this program, you will call the prefix@domain the sender. Your Python program will use split() to parse the
#  prefix and domain and a Python dictionary to tabulate the number of email messages received from each prefix. For
#  this code challenge, consider prefix segments to uniquely identify each sender. Output your dictionary in many
#  ways: natural state (this could be any order and could be changed by your program (not by you)), values sorted
#  by value, keys sorted by keys, items sorted by vale and key, ascending and descending.
#  Advanced: Produce output that tabulates prefix@domain (does not parse into two parts) sends and use the
#  dictionary get() method to replace the if/else stmt. Explain how the get() method works and saves you from
#  writing code!
#

# References
#   https://www.w3schools.com/python/python_ref_file.asp
#   https://www.w3schools.com/python/python_ref_string.asp
#   https://www.w3schools.com/python/python_lists.asp
#   https://www.w3schools.com/python/python_lists_methods.asp
#   https://www.w3schools.com/python/python_dictionaries.asp
#   https://www.w3schools.com/python/ref_dictionary_get.asp
#   https://docs.python.org/3/tutorial/datastructures.html
#   https://www.w3schools.com/python/gloss_python_check_if_dictionary_item_exists.asp

#-----------------------------------------------------------------------------------------------------------------------
# Below are my additions to the program. This should run first. Once this part is exited, the original section will show.
#-----------------------------------------------------------------------------------------------------------------------

# Create a "contact list"
contact_list = []

# Create an object class for contact information and how to manage it
class Contact():
    # Initialize the number of total contacts in the list
    TOTAL_CONTACTS = 0

    # Initialize object variables
    def __init__(self):
        self.first_name = ""
        self.middle_name = ""
        self.last_name = ""
        self.address1 = ""
        self.address2 = ""
        self.city = ""
        self.state = ""
        self.zip = ""
        self.country = ""
        self.home_phone = ""
        self.work_phone = ""
        self.cell_phone = ""
        self.email = ""

    # Getter methods
    def get_first_name(self):
        return self.first_name
    def get_middle_name(self):
        return self.middle_name
    def get_last_name(self):
        return self.last_name
    def get_name(self):
        if self.middle_name == "" and self.last_name == "":
            return self.first_name
        elif self.middle_name == "":
            return self.first_name + " " + self.last_name
        else:
            return self.first_name + " " + self.middle_name + " " + self.last_name
    def get_address(self):
        city_state_zip = ""
        if self.city != "":
            city_state_zip = self.city
        if self.state != "" and self.city != "":
            city_state_zip += ", " + self.state + " "
        else:
            city_state_zip += self.state
        if self.zip != "":
            city_state_zip += self.zip
        return [self.address1,self.address2,city_state_zip,self.city,self.state,self.zip,self.country]
    def get_home_phone(self):
        return self.home_phone
    def get_work_phone(self):
        return self.work_phone
    def get_cell_phone(self):
        return self.cell_phone
    def get_email(self):
        return self.email

    # Setter methods
    def set_first_name(self,name):
        self.first_name = name
    def set_middle_name(self,name):
        self.middle_name = name
    def set_last_name(self,name):
        self.last_name = name
    def set_name(self, name):
        name_split = name.split()
        self.first_name = name_split[0]
        if len(name_split) == 2:
            self.last_name = name_split[1]
        if len(name_split) == 3:
            self.middle_name = name_split[1]
            self.last_name = name_split[2]
    def set_address(self, address1, address2, city, state, zip, country):
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.zip = zip
        self.country = country
    def set_home_phone(self,phone):
        self.home_phone = phone
    def set_work_phone(self,phone):
        self.work_phone = phone
    def set_cell_phone(self,phone):
        self.cell_phone = phone
    def set_email(self,email):
        self.email = email

    # Methods to increment and decrement the total number of contacts
    def increment_contacts():
        Contact.TOTAL_CONTACTS+=1
    def decrement_contacts():
        Contact.TOTAL_CONTACTS -= 1

    # Method to show a contact's full info
    def show(self, number):
        # Numbers each contact, so that it can be selected when using menu options
        print("\nContact number", number, ":")

        # Check for data in each object variable and only show those that contain information
        if self.get_name() != "":
            print("Name: ", self.get_name())
        temp_address = [self.get_address()[0],self.get_address()[1],self.get_address()[2],self.get_address()[6]]
        if not all(item == "" for item in temp_address):
            print("Address: ")
            for item in temp_address:
                if not item == "":
                    print("  ", item)
        if self.get_home_phone() != "":
            print("Home Phone: ", self.get_home_phone())
        if self.get_work_phone() != "":
            print("Work Phone: ", self.get_work_phone())
        if self.get_cell_phone() != "":
            print("Cell Phone: ", self.get_cell_phone())
        if self.get_email() != "":
            print("E-Mail Address: ", self.get_email())

    # Method to edit a contact's info
    def edit(self,number):
        # Show the contact that is being edited
        print("\nEditing...")
        contact_list[number].show(number+1)

        # Editing instructions
        print("\nLeave blank to keep current value, or enter - to remove\n")

        # For each object variable, set up a temp input variable
        temp = input("First name (current: " + self.get_first_name() +"): ")

        # Check for a - input and remove any existing data from that object variable
        if temp == "-":
            self.set_first_name("")

        # Check for input and replace the value
        elif temp != "":
            self.set_first_name(temp)
        temp = input("Middle name (current: " + self.get_middle_name() + "): ")
        if temp == "-":
            self.set_middle_name("")
        elif temp != "":
            self.set_middle_name(temp)
        temp = input("Last name (current: " + self.get_last_name() +"): ")
        if temp == "-":
            self.set_last_name("")
        elif temp != "":
            self.set_last_name(temp)
        temp_address = self.get_address()
        temp = input("Street address (current: " + temp_address[0] + "): ")
        if temp == "-":
            temp_address[0] = ""
        elif temp != "":
            temp_address[0] = temp
        temp = input("Street address (optional second line - current: " + temp_address[1] + "): ")
        if temp == "-":
            temp_address[1] = ""
        elif temp != "":
            temp_address[1] = temp
        temp = input("City (current: " + temp_address[3] + "): ")
        if temp == "-":
            temp_address[3] = ""
        elif temp != "":
            temp_address[3] = temp
        temp = input("State (current: " + temp_address[4] + "): ")
        if temp == "-":
            temp_address[4] = ""
        elif temp != "":
            temp_address[4] = temp
        temp = input("Zip (current: " + temp_address[5] + "): ")
        if temp == "-":
            temp_address[5] = ""
        elif temp != "":
            temp_address[5] = temp
        temp = input("Country (current: " + temp_address[6] + "): ")
        if temp == "-":
            temp_address[6] = ""
        elif temp != "":
            temp_address[6] = temp
        self.set_address(temp_address[0],temp_address[1],temp_address[3],temp_address[4],temp_address[5],temp_address[6])
        temp = input("Home Phone (current: " + self.get_home_phone() + "): ")
        if temp == "-":
            self.set_home_phone("")
        elif temp != "":
            self.set_home_phone(temp)
        temp = input("Work Phone (current: " + self.get_work_phone() + "): ")
        if temp == "-":
            self.set_work_phone("")
        elif temp != "":
            self.set_work_phone(temp)
        temp = input("Cell Phone (current: " + self.get_cell_phone() + "): ")
        if temp == "-":
            self.set_cell_phone("")
        elif temp != "":
            self.set_cell_phone(temp)
        temp = input("E-Mail address (current: " + self.get_email() + "): ")
        if temp == "-":
            self.set_email("")
        elif temp != "":
            self.set_email(temp)

    # Method to add a new contact
    def add(self):
        # Adding instructions
        print("Adding new contact...\n\nAny unknown information can be left blank\n")

        # Directly place user input into each object variable
        self.set_first_name(input("First name: "))
        self.set_middle_name(input("Middle name: "))
        self.set_last_name(input("Last name: "))
        self.set_address(input("Street address: "),input("Street address (optional second line): "),input("City: "),input("State: "),input("Zip: "),input("Country: "))
        self.set_home_phone(input("Home Phone: "))
        self.set_work_phone(input("Work Phone: "))
        self.set_cell_phone(input("Cell Phone: "))
        self.set_email(input("E-Mail address: "))

        # Increment the total number of contacts in list
        Contact.increment_contacts()

# Function to delete a contact
def delete(number):
    print("\nDeleting...")

    # Show the selected contact
    contact_list[number].show(number+1)

    # Ask to be sure the user wants to delete this contact, and loop until a yes or no response is received
    response = ""
    while response != "yes" and response != "no":
        response = input("\nAre you sure you want to edit this contact (yes/no)? ")

        # If yes is entered, delete the requested contact list object
        if response == "yes":
            del contact_list[number]

            # Decrement the total number of contacts in list
            Contact.decrement_contacts()

# Function to import e-mail addresses from mbox-short.txt into the contact list
def import_mbox():
    print("\nImporting e-mail addresses from mail box...\n")

    # Open the file.
    filename = "mbox-short.txt"

    # Assign a file handle variable to open the file into
    file_handle = open(filename)

    # Iterate through each line
    for line in file_handle:
        # Check for "From " in the first 5 characters of the line
        if (line[0:5] == "From "):
            # Split the line by space, and place the second string (should be the e-mail address) into the email variable
            email = line.split()[1]

            # Check if this is a repeated e-mail address
            repeat = False
            for i in range(len(contact_list)):
                if contact_list[i].get_email() == email:
                    repeat = True

            # If not a repeat, add a new entry to the contact list
            if not repeat:
                # Show what's being imported
                print("Importing ",email)

                # Append a new object element to the list
                contact_list.append(Contact())

                # Set the object's email variable to the new email address
                contact_list[Contact.TOTAL_CONTACTS].set_email(email)

                # Increment the total number of contacts in the list
                Contact.increment_contacts()

# Function to show the entire contact list data
def show_all_contacts():
    # Iterate through entire contact list
    for i in range(len(contact_list)):
        # Call the show method for each contact
        contact_list[i].show(i+1)

#Function to dislay the menu
def display_menu():
    print("\nContacts Menu:\n")
    print("1. Show all contacts")
    print("2. Edit contact")
    print("3. Add new contact")
    print("4. Delete contact")
    print("5. Import e-mail addresses from mailbox file")
    print("6. Quit\n")

# Main program

# Clear the menu input
menu_input = 0

# Loop after each function/method call until "Quit" is selected
while menu_input != 6:
    # Display the menu
    display_menu()

    # try-catch in case of a non-integer input
    try:
        # Get user input for menu items
        menu_input = int(input("Enter a menu option: "))

        # Route function calls according to user input
        match menu_input:
            case 1:
                # Show all contacts
                show_all_contacts()
            case 2:
                # Get which contact the user wants to edit and call the edit method for that object
                index = int(input("\nEnter a contact number to edit: "))-1
                contact_list[index].edit(index)
            case 3:
                # Append a new object instance to the contact list and call the add method for that object
                contact_list.append(Contact())
                contact_list[Contact.TOTAL_CONTACTS].add()
            case 4:
                # Get which contact the user wants to delete and delete that object (if the user agrees)
                index = int(input("Enter a contact number to delete: "))-1
                delete(index)
            case 5:
                # Import the e-mail addresses from mbox-short.txt
                import_mbox()
            case 6:
                # Quit the program
                print("\nExiting program...\n\n")
            case _:
                # Watch for any integer that's not 1 through 6 and restart the loop
                print("Invalid response!")
    except ValueError:
        # Watch for any non-integer input and restart the loop
        print("Invalid response!")

#-----------------------------------------------------------------------------------------------------------------------
# Below is the rest of the original assignment. It will run after the above program exits the menu loop. I have added my
# answers to the questions below each TODO.
#-----------------------------------------------------------------------------------------------------------------------

# Open a file, read the file line by line and search for lines that begin with "From " (note the space after
# "From"). Lines that begin with "From:" (note the colon after "From" ) do not contain the sender.
#   1) Count the number of found lines and output the count.
#   2) Use split() to parse the line into separate words.
#   3) Use the second word as the email sender.
#   4) Output the email sender.
#   5) Use split('@') to parse the prefix and domain
#   6) Output the email sender's prefix and domain
#   7) Use a Python dictionary to count the number of messages from each sender
#   8) Demonstrate tuples in a dictionary

# Open the file.
file_name = "mbox-short.txt"
my_file_handle = open(file_name)

# set accumulator to 0
# TODO: What is an accumulator and how are they used?
# An accumulator is a variable that is incremented for each item it is counting, eventually representing the total number of items
count = 0
# Read the file line by line.
# TODO: Where did my_file_handle come from? How was it created? What is it? What is my_line?
# my_file_handle represents the opened file, as defined in the above line, "my_file_handle = open(file_name)".
# my_line is the variable that is reading each line from the file in my_file_handle.
for my_line in my_file_handle:
    # TODO: What does [0:5] mean? What is this decision control structure checking?
    # [0:5] gets only the first 5 characters from the string my_line.
    # This decision control structure checks to see if the first 5 characters in my_line is the same as the string "From ".
    if (my_line[0:5] == "From "):
        # TODO: What are the elements of a list? What does split() do?
        # The elements of a list are individual pieces of data stored in an array-like structure.
        # split() divides up a string at either the spaces or other defined character markers (in this case, @)
        # and places each piece of separated data into a list stored in the given variable.
        my_list_of_words = my_line.split()
        print("dir(list):")
        # TODO: What is x[1] here?
        # This gets the first separated string after "From", which should be the e-mail address.
        print(my_list_of_words[1])
        # TODO: What is happening here?
        # This is splitting the e-mail address into the prefix and domain, so that "address@domain.com" becomes
        # "address" and "domain.com"
        two_parts = my_list_of_words[1].split('@')
        print(two_parts)
        prefix = two_parts[0]
        domain = two_parts[1]
        print(prefix)
        print(domain)
        # TODO: Why don't we use count++?
        # count++ would result in a syntax error, because python doesn't use the ++ increment operator. However, count+=1 would work here.
        count = count + 1

print("\n\nThere were", count, "lines in the file with 'From ' as the first word!\n\n")

# Close the file so you can use it for your dictionary.
my_file_handle.close()

print("\n\n******** Python Dictionary Section ************\n\n")

# Open the file.
file_name = "mbox-short.txt"
my_file_handle = open(file_name)

# TODO: Use a Python dictionary to tabulate the number of messages from each sender
num_of_msgs = dict()

# Use the loop you created for prefix/domain parsing.
for my_line in my_file_handle:
   if (my_line[0:5] == "From "):
        my_list_of_words = my_line.split()
        two_parts = my_list_of_words[1].split('@')
        prefix = two_parts[0]
        domain = two_parts[1]
        print(prefix)
        print(domain)
        # add item to dictionary
        # check to see if prefix exists in the dictionary
        # syntax is: key in dictionary
        if (prefix in num_of_msgs):
            print(num_of_msgs[prefix], " ", prefix,  " exists as a key in this dictionary")
            # add one to the value representing the number of messages
            num_of_msgs[prefix] = num_of_msgs[prefix] + 1
        else:
            # create a new key in the dictionary with one message
            num_of_msgs[prefix] = 1

# Loop through the dictionary to find the sender with the most messages
big_count = None
big_word = None
# TODO: What other programming language can use two variables as loop control variables?
# Java
for my_key,my_val in num_of_msgs.items():
    if big_count is None or my_val > big_count:
        big_word = my_key
        big_count = my_val

print("\n Most messages is by...")
print(big_word, big_count)

# Output the dictionary.
print("\n The num_of_msgs dictionary is: ")
print(num_of_msgs)
# Output the dictionary sorted by keys
print("\n The sorted-by-keys num_of_msgs dictionary is: ")
print(sorted(num_of_msgs.keys()))
# Output the dictionary sorted by values
print("\n The sorted-by-values num_of_msgs dictionary is: ")
print(sorted(num_of_msgs.values()))

# Demonstrate tuples and dictionaries
print("\nTuples in a dictionary:\n")
print("Key-Value Pairs are:")
for (myKey, myVal) in num_of_msgs.items():
    print(myKey, myVal)
print("\n...and printed as tuples...")
my_tuples = num_of_msgs.items()
print(my_tuples)

# Close the file
my_file_handle.close()

# Advanced: Use prefix@domain as the sender and the get() method in dictionary
print("\n*********** Advanced ************\n")

# Open the file.
file_name = "mbox-short.txt"
my_file_handle = open(file_name)

num_of_msgs = dict()

# Use the loop you created for prefix/domain parsing.
for my_line in my_file_handle:
   if (my_line[0:5] == "From "):
        my_list_of_words = my_line.split()
        sender = my_list_of_words[1]
        # print(sender)
        # add item to dictionary
        # TODO: Explain how  this line of code works and how it replaces the code on lines 88-95.
        # This line finds the number of times the sender's prefix shows up, and for each, adds one to the number of messages for that sender's prefix
        # This replaces the code in 88-95 by being able to count the number of times a sender's prefix is detected without using an additional "if" statement
        num_of_msgs[sender] = num_of_msgs.get(sender, 0) + 1

# Loop through the dictionary to find the sender with the most messages
big_count = None
big_word = None
# TODO: What other programming language can use two variables as loop control variables?
# Java
for (my_key,my_val) in num_of_msgs.items():
    if big_count is None or my_val > big_count:
        big_word = my_key
        big_count = my_val

#print("\n Most messages is by...")
print(big_word, big_count)

# Output the dictionary.
print("\n The num_of_msgs dictionary is: ")
print(num_of_msgs)

# Output the dictionary keys sorted by keys
print("\n The sorted-by-keys num_of_msgs dictionary is: ")
print(sorted(num_of_msgs.keys()))

# Output the dictionary values sorted by values
print("\n The sorted-by-values num_of_msgs dictionary is: ")
print(sorted(num_of_msgs.values()))

# Output the dictionary's key-value pairs sorted by key
# Loop through the dictionary in sorted key order
# () around k,v are added for programming clarity
print("\n Sorted by key...")
for (k,v) in sorted(num_of_msgs.items()):
    print(k,v)

# Output the dictionary's key-value pairs sorted by descending value
# create a temporary list of your dictionary items in value, key order
print("\n Sorted by value...")
tmp_list = list()
for (k,v) in num_of_msgs.items():
    # Note you have reversed the value/key order.
    tmp_list.append((v,k))
tmp_list = sorted(tmp_list, reverse=True)
print(tmp_list)
print("\n")
# Print a list of tuples
for my_tuple in tmp_list:
    print(my_tuple)

# Close the file
my_file_handle.close()




