# Word Guess
# mF 13sept22
# -------------------------------
# Simple "Hangman"-style guessing game.
# For best results, run from a stand-alone console, and not the console included in PyCharm. The clear_screen function
# only works in the stand-alone environment. In PyCharm, you get an error ("TERM environment variable not set.")

# Import needed functions
import random
import requests
import os

# Download dictionary file as a word source -- From comment at https://stackoverflow.com/questions/6386308/http-requests-and-json-parsing-in-python and linked GitHub site
dict_download = requests.get("https://raw.githubusercontent.com/adambom/dictionary/master/dictionary.json").json()

# Initialize variables
guess = ""
hide_word = ""
remaining_guesses = 0
retry = "yes"
word = ""


# Function to clear screen -- Found at https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Check guesses function
def check_guess(word, guess, hide_word):
    # Check for single-letter guesses vs. full words
    if len(guess) != 1:

        # Check if full-word guess is correct
        if word == guess:

            # Change the hidden word line to the guessed word
            hide_word = guess
            return hide_word, True
        else:
            return hide_word, False
    else:
        good = False

        # Check each letter against single-letter guess
        for x in range(len(word)):

            # Change characters in hidden word line to match correct guesses
            if word[x] == guess:
                hide_word = hide_word[:x] + guess + hide_word[x + 1:]
                good = True

        # Return modifications to hidden word line and if guess is correct
        return hide_word, good


# Create a header that clears the screen, puts a welcome text, and shows how many letters are in the word
def welcome(word):
    # Clear the screen
    clear_screen()

    # Welcome text in bold (\033[1m) and underlined (\033[4m) (\033[0m) = end text style attributes
    print("\n\033[1m\033[4mWelcome to Word Guess!\033[0m\n")

    # Show word length
    print("The word you are guessing is", len(word), "letters long.\n")


# Loop until the player chooses not to play anymore
while retry.lower()[0] == "y":

    # Select new word and definition from dictionary
    word, definition = random.choice(list(dict_download.items()))
    word = word.lower()

    # Set up hidden word string
    for x in range(len(word)):
        if word[x] == " ":
            hide_word = hide_word[:x] + " "
        elif word[x] == "-":
            hide_word = hide_word[:x] + "-"
        else:
            hide_word = hide_word[:x] + "_"

    # Start game
    guess_record = []

    # welcome header
    welcome(word)

    # Instructions
    print("You will get a number of tries to guess the word or letters in the word.")
    print("Incorrect guesses decrease the number of guesses you have left.")
    print("However, correct guesses and repeated guesses do not decrease your guess count.\n")

    # Select number of guesses
    while remaining_guesses == 0:
        try:
            remaining_guesses = int(input("Enter how many guesses you want up to 15 (default = word length): ") or len(word))
        except:
            print("Your response must be an integer. Try again.")
            remaining_guesses = 0
        if remaining_guesses > 15:
            print("More than 15 guesses is too easy. Try again.")
            remaining_guesses = 0

    # Refresh header
    welcome(word)
    print("\n")

    # Loop while the player still has guesses left
    while remaining_guesses > 0:
        # Display hidden word lines and any guessed letters, and remaining guesses left
        print("Current guesses:", hide_word, " Guesses left:", remaining_guesses)

        # Get user input -- can be either a single letter or a word
        guess = input("Guess a letter or word: ")

        # Call function to check guess against actual word
        hide_word, good_guess = check_guess(word, guess.lower(), hide_word)

        welcome(word)

        # Test if guess is correct and inform player
        if guess in guess_record:
            print("You've already guessed that. Try again.\n")
        elif good_guess:
            guess_record.append(guess)
            print("Correct guess!\n")
        else:
            guess_record.append(guess)
            print("Nope. Incorrect guess.\n")
            remaining_guesses -= 1

        # Test for end of game conditions
        if remaining_guesses == 0:
            print("\nSorry. You lost this round.")
        elif hide_word == word:
            print("\nYOU WON!")
            remaining_guesses = 0

    # End of game
    # Show word
    print("\nThe word was:", word)

    # Show definition of the word
    print("Its definition is:", definition)

    # Ask if user wants to play again
    retry = input("\nWould you like to play again (yes/no)? ")
