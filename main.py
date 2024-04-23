import math
# Powerup implementation.
    # Powerups have a grid position and an activation pattern
    # Individual types of powerups are subclasses of a baseclass Powerup that has members: grid position and activation pattern. Each powerup has its own pattern. The patterns are: "/", "\", "|", and "-"
    # Powerups determine their poition pseudo-randomly. And, they check if there are spots available before they are placed. They check to see if they overlap other pieces or not before placed.
    # Powerups are triggered when a players places their piece ontop of it. Their pieces will not be destroyed, but the opposite type of pieces will be.
    # Optionally, the players can decide to enable a special rule that makes powerup activations destory both types of piecees and other powerups caught in the activation zone.
    # could add a red trail of the same powerup type along the path of the activation to visually show where the activation happened. This activation should be removed after next piece is placed. The smoke would also have to not hit a certain player as well. 

# TODO Powerups Animation

# TODO Powerups Activation

# TODO Game Logic 

# TODO Grid Display
# ANSI escape codes for text colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PINK = "\x1b[38;5;205m"
CYAN = "\x1b[36m"
END = "\033[0m"  # Reset color to default

# Create empty grid.

pieces = [" . ", " X ", " O ", YELLOW + " / " + END, BLUE + " \\ " + END, PINK + " | " + END, CYAN + " - " + END]

def win_check(grid):
    #TODO Horizontal Check
    pass

    
    #TODO Vertical Check
    #TODO Diagonal Check Downward
    #Todo Diagonal Check Upward

while True:
    # Num of rows/cols.
    try:
        n = int(input("Enter the number of rows and columns desired. Must be a value between 3-52\n"))
    except:
        continue
    if 3 <= n <= 53:
        print()
        break

def pieces_to_place_per_player_turn():
    return round(math.log(n**2,3))

pieces_per_turn = pieces_to_place_per_player_turn()

# Nested loop comprehension to create the 2D matrix for the grid.
canonical_grid_state = [[pieces[0] for _ in range(n)] for _ in range(n)]

canonical_grid_state[0][0] = pieces[4]
canonical_grid_state[n-1][n-1] = pieces[4]

# Display the grid.
def display_grid(grid_state):
    for i in range(n):
        # Print number prefix per row.
        print("{}".format(alphabet[i]), end = "  ")
        for j in range(0, n):
            print(grid_state[i][j], end = "  ")

        print("\n")
    print("   ", end = "")
    for i in range(n):
        print("{:2d}".format(i + 1), end = "   ")
    print("\n")

# Spacing for x axis names.
# Values for x axis names.
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Print x axis names per grid unit.
def scroll_screen():
    for _ in range(500):
        print()

turn_switch = True

def alternate_turns():
    global turn_switch

    turn_switch = not turn_switch

    if turn_switch:
        return pieces[2]  # Return the piece for the new turn
    else:
        return pieces[1]  # Return the piece for the new turn

# TODO Modify grid State
def modify_grid(alpha_index, numeral_index, grid, piece):
    # Add overlap checks
    grid[alphabet.index(alpha_index)][numeral_index - 1] = piece


while True:
    display_grid(canonical_grid_state)
    
    while True:
        # ANSI code to clear the screen.

        #TODO Implement bounds checking.
        valid_alpha_chars = alphabet[:n]
        location = (input("Place your piece. \n"))

        location = location.split()

        l_len = len(location)

        if l_len < 2:
            print("Not enough arguments", "For example: A 1")
            continue
        elif l_len > 2:
            print("Too many arguments", "For example: A 1")
            continue

        alpha_val = location[0]
        numeral_val = location[1]

        if not alpha_val in valid_alpha_chars:
            print("Not a valid alpha input", "For example: A 1")
            continue

        numeral_val = int (numeral_val)
        
        if  numeral_val < 1 or numeral_val > n:
            print("Number should be between 1 and {}".format(n), "val:", numeral_val)
            continue

        modify_grid(alpha_val, numeral_val,  canonical_grid_state, alternate_turns())

        win_check(canonical_grid_state)

        print('\033[H\033[J')
        scroll_screen()
        display_grid(canonical_grid_state)
