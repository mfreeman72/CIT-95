# Maze Game
#
# A simple maze-like dungeon crawling game

# Import needed functions
from random import randrange
import random
import os

# Define compass
compass = ["             ^             ", "             N             ", "             |             ",
           "    <  W --- o --- E  >    ", "             |             ", "             S             ",
           "             v             ", "                           "]


# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to generate each room on the map
def generate_room(north_wall_visible, west_wall_visible, room_visible, item):
    room = ["", "     ", ""]
    room[0] = "+---+" if north_wall_visible or room_visible else "+   +"
    room[1] = "| " + item + " |" if room_visible else "|" + room[1][1:] if west_wall_visible else "     "
    room[2] = "+---+" if room_visible else "+   +"
    return room


# Create class for in-game map and map objects and methods
class Map:
    # Initialize game variables
    grid = []
    row = []
    maze_x = 0
    maze_y = 0
    maze_z = 0
    player_x = 0
    player_y = 0
    prev_x = 0
    prev_y = 0
    level = randrange(10)
    player_strength = 100
    armor_strength = 0
    money_amount = 0
    rock_amount = 0
    sword_strength = 0
    jewel_amount = 0

    # Initialize new room constructor
    def __init__(self):
        self.new_room = None

    # Method to build the map out of visible and invisible rooms
    def generate_map(self):
        north_wall = False
        west_wall = False
        for y in range(0, self.maze_y):
            for x in range(0, self.maze_x):
                if y > 0:
                    north_wall = self.grid[x][y - 1]['visible']
                if x > 0:
                    west_wall = self.grid[x - 1][y]['visible']
                self.new_room = generate_room(north_wall, west_wall, self.grid[x][y]['visible'], self.grid[x][y]['item'])
                count = 0
                for i in self.new_room:
                    self.row[(y * 2) + count] = self.row[(y * 2) + count][:x * 4] + i
                    count += 1

    # Method to display fully built map
    def display_map(self):
        clear_screen()
        temp_item = self.grid[self.player_x][self.player_y]['item']
        self.grid[self.player_x][self.player_y]['item'] = "i"
        self.grid[self.player_x][self.player_y]['visible'] = True
        self.generate_map()
        total_rows = len(self.row) / 1.5
        print("Level Map:")
        for i in range(0, int(total_rows + 1)):
            if i <= 6:
                print(compass[i], self.row[i])
            else:
                print(compass[7], self.row[i])
        print("\n-----------------------------------------")
        print("Inventory:")
        if self.rock_amount > 0:
            print(f"   Things you can throw: {self.rock_amount}")
        if self.sword_strength > 0:
            print(f"   Sword Strength: {self.sword_strength}%")
        if self.armor_strength > 0:
            print(f"   Armor Strength: {self.armor_strength}%")
        if self.money_amount > 0:
            print(f"   Money: ${self.money_amount}")
        if self.jewel_amount > 0:
            print(f"   Jewels: {self.jewel_amount}")
        print("-----------------------------------------")
        print("\n-----------------------------------------")
        if self.player_strength < 0:
            self.player_strength = 0
        print(f"Player strength: {int(self.player_strength)}%")
        if self.grid[self.player_x][self.player_y]['creature'] != " " and int(self.grid[self.player_x][self.player_y]['creature_strength']) > 0:
            print(f"{self.grid[self.player_x][self.player_y]['creature']} strength: {int(self.grid[self.player_x][self.player_y]['creature_strength'])}%")
        print("-----------------------------------------")
        self.grid[self.player_x][self.player_y]['item'] = temp_item

    # Method to place items to find randomly on map
    def place_items(self):
        num_items = randrange(self.maze_y * self.maze_x) / 3
        for i in range(0, int(num_items)):
            item_type = randrange(5)
            rand_x = randrange(self.maze_x)
            rand_y = randrange(self.maze_y)
            match item_type:
                case 0:
                    self.grid[rand_x][rand_y]['item'] = "o"
                case 1:
                    self.grid[rand_x][rand_y]['item'] = "!"
                case 2:
                    self.grid[rand_x][rand_y]['item'] = "8"
                case 3:
                    self.grid[rand_x][rand_y]['item'] = "$"
                case 4:
                    self.grid[rand_x][rand_y]['item'] = "*"

    # Method to place creatures randomly on map
    def place_creatures(self):
        num_creatures = randrange(self.maze_y * self.maze_x) / 3
        for i in range(0, int(num_creatures)):
            creature_type = randrange(5)
            strength = randrange(101)
            rand_x = randrange(self.maze_x)
            rand_y = randrange(self.maze_y)
            match creature_type:
                case 0:
                    self.grid[rand_x][rand_y]['creature'] = "Golem"
                    self.grid[rand_x][rand_y]['creature_strength'] = int(strength / 2)
                case 1:
                    self.grid[rand_x][rand_y]['creature'] = "Dragon"
                    self.grid[rand_x][rand_y]['creature_strength'] = int(strength)
                case 2:
                    self.grid[rand_x][rand_y]['creature'] = "Snake"
                    self.grid[rand_x][rand_y]['creature_strength'] = int(strength / 5)
                case 3:
                    self.grid[rand_x][rand_y]['creature'] = "Zombie"
                    self.grid[rand_x][rand_y]['creature_strength'] = int(strength / 3)
                case 4:
                    self.grid[rand_x][rand_y]['creature'] = "Sprite"
                    self.grid[rand_x][rand_y]['creature_strength'] = int(strength / 4)

    # Method to place exit to next level randomly on map
    def place_exit(self):
        self.grid[randrange(self.maze_x)][randrange(self.maze_y)]['item'] = "/"

    # Method to place initial player position on new map
    def place_player(self):
        return randrange(self.maze_x), randrange(self.maze_y)

    # Method to initialize a new map level
    def init(self):
        self.grid = []
        self.row = []
        self.maze_x = randrange(5) + 6
        self.maze_y = randrange(5) + 6
        self.maze_z = randrange(5) + 6
        for x in range(0, self.maze_x):
            self.grid.append([])
            for y in range(0, self.maze_y):
                self.grid[x].append({'visible': False, 'item': " ", 'creature': " ", 'creature_strength': 0})
        for y in range(0, self.maze_y):
            self.row.append("")
            self.row.append("")
            self.row.append("")
            for x in range(0, self.maze_x):
                self.new_room = generate_room(False, False, False, " ")
                count = 0
                for i in self.new_room:
                    self.row[(y * 2) + count] = self.row[(y * 2) + count][:x * 4] + i
                    count += 1
        self.place_items()
        self.place_creatures()
        self.place_exit()
        self.player_x, self.player_y = self.place_player()
        while self.grid[self.player_x][self.player_y]['item'] == "/" \
                and self.grid[self.player_x][self.player_y]['creature'] != " ":
            self.player_x, self.player_y = self.place_player()


# Create an initial game map
game_map = Map()

# Define lists of text to be randomly used
not_understood = ["\nTry that again.", "\nI'm not sure you understood the question.",
                  "\nPerhaps we should go over this again?", "\nWut?", "Do I need to speak more clearly?",
                  "\nThat was not the answer I was expecting."]
lets_go = ["\nGreat! I thought you might.", "\nOf course you should!", "\nWell, get up then!",
           "\nAnd the quest begins...", "\nRight-o! Let's go!"]
snooze = ["\n{snore} You wake up again. Nothing has changed.", "\nDo you really think that will help?",
          "\nYou take forever to fall asleep, and it's not for long. You're still in the dungeon.",
          "\nYou can't sleep. There are... noises... in the distance."]
dead_message = ["\nOuch. You're dead now.", "\nIt's good to be alive. Unfortunately, you aren't.", "\nDead. Buh-bye.",
                "\nDid you really think you could take that guy?! Now you're a goner!", "\nWhoopsie! You're dead."]
creature_found = ["\nUh oh! There's a mean looking creature here!",
                  "\nWhat in the world is THAT?! It's some kind of creature, coming right for you!",
                  "\nHow about that? It's a bad guy!",
                  "\nMaybe we shouldn't have come this way. That creature looks awfully mean!"]
easy_fight = ["\nBut I think you can take him.", "\nPiece of cake!", "\nYou got this!", "\nGo for it, tiger!",
              "\nMake me proud!", "\nNo problem. This one's a pansy."]
equal_fight = ["\nYou might be able to take him, but be careful.", "\nI give this one about a 50/50 chance.",
               "\nYou might make it out alive, but I'm not placing any bets.", "\nLooks like a pretty even match-up."]
tough_fight = ["\nI suggest leaving this bad boy alone.", "\nThis doesn't look good.",
               "\nI'd place my wager on that guy.", "\nMy suggestion? RUN!", "\nGet outta here!"]
cave_description = [
    "\nThis room has stone walls, some kind of moldy smell, and... whatever that thing in the corner is.",
    "\nThis dungeon looks about the same as any other, and smells like it, too.",
    "\nWhat do you expect? It looks like a classic fantasy-genre dungeon.",
    "\nI was expecting it to be a little cleaner in here, personally.", "\nWhew! Someone forgot to call the maid!",
    "\nYeah, just your basic four walls and four doors."]
rock = ["\nThere are some rocks here.", "\nIt looks like someone left their pile of rocks.",
        "\nSome rocks are scattered around the room.", "\nIt's a handy-dandy rock pile!"]
sword = ["\nThere's an old sword leaning against the wall.", "\nA rusty sword is lying on the floor.",
         "\nWant a sword? 'Cause I see a sword.", "\nA sword! What a great find!"]
armor = ["\nSome rusty armor is here.",
         "\nThere is a skeleton wearing armor. Maybe you can take the armor. It's not doing that guy any good.",
         "\nThere's some ugly old armor. Not great. Not bad.", "\nIt looks like someone dropped some armor in here."]
money = ["\nA bag of money is on the floor.", "\nLooks like someone hit the jackpot! MONEY!",
         "\nNot that you've struck it rich or anything, but there's some money right there.",
         "\nSome coins are lying in the corner of the room."]
jewel = ["\nOooo! A shiny jewel is on the floor!", "\nMaybe that jewel in the corner might help you!",
         "\nThis jewel on the floor looks well-polished.",
         "\nYou might want to pick up that jewel over there, just saying."]
dead_end = [
    "\nYou open the door, and there's just more wall. Can't go that way.",
    "\nThat door is locked tight, and I don't think you're strong enough to break it.",
    "\nOn the other side of the door, there is an impassable gaping chasm. Can't go that way.",
    "\nThere is no way to go any further in that direction."]


# Function for creature battles
def creature_battle():
    battle = ""
    print(random.choice(creature_found))
    if int(game_map.grid[game_map.player_x][game_map.player_y]['creature_strength']) < int(game_map.player_strength / 2):
        print(random.choice(easy_fight))
    elif int(game_map.grid[game_map.player_x][game_map.player_y]['creature_strength']) < int(game_map.player_strength):
        print(random.choice(equal_fight))
    else:
        print(random.choice(tough_fight))
    while battle.lower() != "run" \
            and battle.lower() != "r" \
            and battle.lower() != "negotiate" \
            and battle.lower() != "n" \
            and battle.lower() != "fight" \
            and battle.lower() != "f":
        print(f"You are facing a {int(game_map.grid[game_map.player_x][game_map.player_y]['creature_strength'])}% strength {game_map.grid[game_map.player_x][game_map.player_y]['creature']}.")
        battle = input("\nDo you want to fight, negotiate, or run? ")
        if battle.lower() == "run" or battle.lower() == "r":
            game_map.player_x = game_map.prev_x
            game_map.player_y = game_map.prev_y
            game_map.display_map()
        if battle.lower() == "fight" or battle.lower() == "f":
            if game_map.sword_strength > 0:
                game_map.grid[game_map.player_x][game_map.player_y]['creature_strength'] -= ((game_map.player_strength + game_map.sword_strength) / 10)
                game_map.sword_strength -= 5
                if game_map.sword_strength < 0:
                    game_map.sword_strength = 0
                game_map.display_map()
                print("\nYou strike the", game_map.grid[game_map.player_x][game_map.player_y]['creature'])
            elif game_map.rock_amount > 0:
                game_map.grid[game_map.player_x][game_map.player_y]['creature_strength'] -= ((game_map.player_strength + 10) / 10)
                game_map.rock_amount -= 1
                game_map.display_map()
                print("\nYou throw a rock at the", game_map.grid[game_map.player_x][game_map.player_y]['creature'])
            else:
                game_map.grid[game_map.player_x][game_map.player_y]['creature_strength'] -= (game_map.player_strength / 10)
                game_map.player_strength -= 2
                game_map.display_map()
                print("\nYou punch the", game_map.grid[game_map.player_x][game_map.player_y]['creature'])
            if int(game_map.grid[game_map.player_x][game_map.player_y]['creature_strength']) > 0:
                game_map.player_strength -= (2 + game_map.grid[game_map.player_x][game_map.player_y]['creature_strength'] / 10)
                game_map.display_map()
                print("\nThe", game_map.grid[game_map.player_x][game_map.player_y]['creature'], "strikes back!")
        if battle.lower() == "negotiate" or battle.lower() == "n":
            if game_map.grid[game_map.player_x][game_map.player_y]['creature'] == "Dragon":
                demand = randrange(5)
                if game_map.jewel_amount < demand:
                    game_map.player_strength -= (2 + game_map.grid[game_map.player_x][game_map.player_y]['creature_strength'] / 10)
                    game_map.display_map()
                    print("\nYou negotiate with the Dragon.")
                    print("The Dragon demands", demand, "jewels!")
                    print("Uh oh! You don't have that many jewels.")
                    print("\nThe Dragon attacks!")
                else:
                    game_map.jewel_amount -= demand
                    game_map.grid[game_map.player_x][game_map.player_y]['creature'] = " "
                    game_map.grid[game_map.player_x][game_map.player_y]['creature_strength'] = 0
                    game_map.display_map()
                    print("\nYou negotiate with the Dragon.")
                    print("The Dragon demands", demand, "jewels!")
                    print("The Dragon is satisfied, takes your jewels, and flies away.")
            else:
                game_map.player_strength -= (2 + game_map.grid[game_map.player_x][game_map.player_y]['creature_strength'] / 10)
                game_map.display_map()
                print("\nYou can't negotiate with a", game_map.grid[game_map.player_x][game_map.player_y]['creature'], "!")
                print("\nThe", game_map.grid[game_map.player_x][game_map.player_y]['creature'], "attacks!")
        if int(game_map.grid[game_map.player_x][game_map.player_y]['creature_strength']) <= 0:
            print(f"You've vanquished the {game_map.grid[game_map.player_x][game_map.player_y]['creature']}! Good for you!")
            game_map.grid[game_map.player_x][game_map.player_y]['creature'] = " "
            game_map.grid[game_map.player_x][game_map.player_y]['creature_strength'] = 0
            # game_map.display_map()


# Set the quit_game boolean to False
quit_game = False

# Initialize the first game map
game_map.init()

# Clear the screen and introduce the story
clear_screen()
print("It is an eerie, foggy, moonless night.")
print("As you go to bed, you hear what sounds like wolves.")
print("As you fall asleep, you think you hear strange chanting voice echoing in the distance.")
print("\nSuddenly, you awaken to find yourself in a dark, musty cave...")
print("or maybe it's a dungeon. It's hard to tell in the dark.")
print("The only light you have is an old, rusty lantern that sits in the corner.")

# Ask the player to continue in a silly way
answer = ""
while answer.lower() != "explore" and answer.lower() != "e":
    answer = input("\nDo you want to explore, or try to go back to sleep? Type 'explore' or 'sleep' to continue the adventure: ")
    if answer.lower() == "sleep" or answer.lower() == "s":
        print(random.choice(snooze))
    elif answer.lower() == "explore" or answer.lower() == "e":
        game_map.display_map()
        print(random.choice(lets_go))
    else:
        print(random.choice(not_understood))

# Loop while player has strength left and hasn't quit the game
while game_map.player_strength > 0 and quit_game is not True:
    # Initialize response variables
    direction = ""
    answer = ""
    # Display a random description for the current cave/room
    description = random.choice(cave_description)
    print(description)
    # Check for an item in the room, report it, and if necessary get appropriate response from player
    match game_map.grid[game_map.player_x][game_map.player_y]['item']:
        # Rocks (depicted as "o")
        case "o":
            print(random.choice(rock))
            while answer.lower() != "yes" \
                    and answer.lower() != "y" \
                    and answer.lower() != "no" \
                    and answer.lower() != "n":
                answer = input("Do you want to pick up these rocks (yes/no)? ")
                if answer.lower() == "yes" or answer.lower() == "y":
                    number = randrange(5)
                    if game_map.rock_amount + number > 25:
                        print("You can't carry any more rocks.")
                    else:
                        game_map.rock_amount += number
                        game_map.grid[game_map.player_x][game_map.player_y]['item'] = " "
                    game_map.display_map()
        # Sword (depicted as "!")
        case "!":
            print(random.choice(sword))
            number = randrange(100)
            if number > game_map.sword_strength:
                while answer.lower() != "yes" \
                        and answer.lower() != "y" \
                        and answer.lower() != "no" \
                        and answer.lower() != "n":
                    answer = input("Do you want to pick up the sword (yes/no)? ")
                if answer.lower() == "yes" or answer.lower() == "y":
                    game_map.sword_strength = number
                    game_map.grid[game_map.player_x][game_map.player_y]['item'] = " "
                    game_map.display_map()
            else:
                print("\nThe sword you have is better than this one. Let's just leave that there.")
        # Armor (depicted as "8")
        case "8":
            print(random.choice(armor))
            number = randrange(100)
            if number > game_map.armor_strength:
                while answer.lower() != "yes" \
                        and answer.lower() != "y" \
                        and answer.lower() != "no" \
                        and answer.lower() != "n":
                    answer = input("Do you want to take the armor (yes/no)? ")
                if answer.lower() == "yes" or answer.lower() == "y":
                    game_map.armor_strength = number
                    game_map.grid[game_map.player_x][game_map.player_y]['item'] = " "
                    game_map.display_map()
            else:
                print("\nThe armor you have is better than this. Let's just leave that there.")
        # Money (depicted as "$")
        case "$":
            print(random.choice(money))
            number = randrange(10)
            while answer.lower() != "yes" \
                    and answer.lower() != "y" \
                    and answer.lower() != "no" \
                    and answer.lower() != "n":
                answer = input("Do you want to take the money (yes/no)? ")
            if answer.lower() == "yes" or answer.lower() == "y":
                game_map.money_amount += number
                game_map.grid[game_map.player_x][game_map.player_y]['item'] = " "
                game_map.display_map()
        # Jewel (depicted as "*")
        case "*":
            print(random.choice(jewel))
            while answer.lower() != "yes" \
                    and answer.lower() != "y" \
                    and answer.lower() != "no" \
                    and answer.lower() != "n":
                answer = input("Do you want to take the jewel (yes/no)? ")
            if answer.lower() == "yes" or answer.lower() == "y":
                game_map.jewel_amount += 1
                game_map.grid[game_map.player_x][game_map.player_y]['item'] = " "
                game_map.display_map()
    # Staircase/exit (depicted as "/")
        case "/":
            print("You see a staircase going up!")
            while answer.lower() != "yes" \
                    and answer.lower() != "y" \
                    and answer.lower() != "no" \
                    and answer.lower() != "n":
                answer = input("Do you want to go up to the next level (yes/no)? ")
            if answer.lower() == "yes" or answer.lower() == "y":
                game_map.level -= 1
                if game_map.level == 0:
                    clear_screen()
                    print("You seem to have reached the end of the adventure!")
                    print("You suddenly wake up in your bed. Was it all a dream?")
                    print("A slight, rusty, sword-like glint shines from behind the curtain.")
                    print("Maybe you should just ignore that and believe it was just a dream...")
                    break
                game_map.init()
                game_map.display_map()
                print(random.choice(cave_description))
        # Nothing
        case " ":
            print("You see nothing special here.")
    # If there is a creature in the room, initiate the creature_battle scenario
    if game_map.grid[game_map.player_x][game_map.player_y]['creature'] != " ":
        creature_battle()
    # Otherwise, ask the player for a direction to go from here
    else:
        # Loop until an appropriate direction is given
        while direction.lower() != "north" \
                and direction.lower() != "n" \
                and direction.lower() != "south" \
                and direction.lower() != "s" \
                and direction.lower() != "east" \
                and direction.lower() != "e" \
                and direction.lower() != "west" \
                and direction.lower() != "w" \
                and direction.lower() != "quit" \
                and direction.lower() != "q":
            direction = input("\nWhere would you like to go? Type north, south, east, or west: ")

        # Move player positions to appropriate room location, checking for dead-ends, or quit response
        match direction.lower():
            case "quit" | "q":
                break
            case "north" | "n":
                if game_map.player_y == 0:
                    print(random.choice(dead_end))
                else:
                    game_map.prev_y = game_map.player_y
                    game_map.player_y -= 1
                    game_map.display_map()
            case "south" | "s":
                if game_map.player_y == game_map.maze_y - 1:
                    print(random.choice(dead_end))
                else:
                    game_map.prev_y = game_map.player_y
                    game_map.player_y += 1
                    game_map.display_map()
            case "east" | "e":
                if game_map.player_x == game_map.maze_x - 1:
                    print(random.choice(dead_end))
                else:
                    game_map.prev_x = game_map.player_x
                    game_map.player_x += 1
                    game_map.display_map()
            case "west" | "w":
                if game_map.player_x == 0:
                    print(random.choice(dead_end))
                else:
                    game_map.prev_x = game_map.player_x
                    game_map.player_x -= 1
                    game_map.display_map()

# If game ends with player running out of strength, print random death message
if game_map.player_strength <= 0:
    print()
    print(random.choice(dead_message))
