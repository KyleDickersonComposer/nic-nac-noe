import random

# Determine which player has the "x" pieces.
# "x" pieces go first.
def determine_who_goes_first(player1, player2):
    if random.choice([0, 1]) == 0:
        player1.pieces = 'x'
        player2.pieces = 'y'
    else:
        player1.pieces = 'y'
        player2.pieces = 'x'

class Player():
    def __init__(self):
        self.pieces = "TBD"
# Game menu contents:
# Default rulesets are displayed.
while True:
    #TODO add a bot that randomly places things.
    print("Would you like to play a standard ruleset or make your own?\n")
    ans = input("Enter <custom> for a custom rule set or enter <standard> for the standard ruleset.\n")
    ans.lower()

    if ans == "custom":
        break
    elif ans == "standard":
        #Setup a standard rules game.
        break
    else:
        continue

def new_game(ruleset, player1, player2):
    #TODO Implement newgame function.
    pass
    
# Num of rows/cols.
n = input("Enter the number of rows and columns desired.\n")
print(n)

# Powerups per turn.
number_of_powerups = input("Enter the number of powerups per player turn.\n")

# Num of pieces placed per turn.
number_of_pieces_placed_per_turn  = input("Enter the number of pieces you wish to place per player turn.\n")

# Game procedure:
    # Players alternate turns after x's go first.
    # Players place their piece(s).
    # If player wins during turn break and show win screen.

# Build grid of n x n size.



help = """\n
  +--------------------------------+
10|  a  b  c  d  .  .  .  .  .  .  |
9 |  .  b  .  .  .  .  .  .  .  .  |
8 |  .  .  c  .  .  .  .  .  .  .  |
7 |  .  .  .  d  .  .  .  .  .  .  |
5 |  .  .  .  .  .  .  .  .  .  .  |
6 |  .  .  .  .  .  .  .  .  .  .  |
4 |  .  .  .  .  .  .  .  .  .  .  |
3 |  .  .  .  .  .  .  .  .  .  .  |
2 |  .  .  .  .  .  .  .  .  .  .  |
1 |  .  .  .  .  .  .  .  .  .  .  |
  +--------------------------------+
    1  2  3  4  5  6  7  8  9  10 
"""


# ANSI escape codes for text colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
END = "\033[0m"  # Reset color to default

# Print text in different colors
print(RED + "This text is red." + END)
print(GREEN + "This text is green." + END)
print(YELLOW + "This text is yellow." + END)
print(BLUE + "This text is blue." + END)

print(help)

help = help.replace("a", RED + "\\" + END)
help = help.replace("b", RED + "\\" + END)
help = help.replace("c", RED + "\\" + END)
help = help.replace("d", RED + "\\" + END)
  
print(help)

# Display updated gameboard for every piece placed.
# Then, show game recap and "Play Again?" prompt.
# Powerup implementation.
    # Powerups have a grid position and an activation pattern
    # Individual types of powerups are subclasses of a baseclass Powerup that has members: grid position and activation pattern. Each powerup has its own pattern. The patterns are: "/", "\", "|", and "-"
    # Powerups determine their position pseudo-randomly. And, they check if there are spots available before they are placed. They check to see if they overlap other pieces or not before placed.
    # Powerups are triggered when a players places their piece ontop of it. Their pieces will not be destroyed, but the opposite type of pieces will be.
    # Optionally, the players can decide to enable a special rule that makes powerup activations destory both types of piecees and other powerups caught in the activation zone.
    # could add a red trail of the same powerup type along the path of the activation to visually show where the activation happened. This activation should be removed after next piece is placed. The smoke would also have to not hit a certain player as well. 

# Lists will be pretty good for holding the various types of data that need to be held for this program. They can hold powerups and they can hold empty or they can hold pieces.

# Win condition implementation.
    # Just do the simple n^2 check foreach of the possible match possibilities.

# TODO Data Structure for Grid and Pieces

# TODO Powerups Animation

# TODO Powerups Activation

# TODO Game Logic 

# TODO Grid Display

# TODO Powerups Spawner
