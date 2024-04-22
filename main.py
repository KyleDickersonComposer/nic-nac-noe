# Win condition implementation.
    # Just do the simple n^2 check foreach of the possible match possibilities.

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

# Create empty board.

pieces = [" . ", " X ", " O ", YELLOW + " / " + END, BLUE + " \\ " + END, PINK + " | " + END, CYAN + " - " + END]


def win_check():
    #TODO Horizontal Check
    #TODO Vertical Check
    #TODO Diagonal Check Downward
    #Todo Diagonal Check Upward
    pass

while True:
    # Num of rows/cols.
    try:
        n = int(input("Enter the number of rows and columns desired. Must be a value between 3-52\n"))
    except:
        continue
    if 3 <= n <= 53:
        print()
        break

# Nested loop comprehension to create the 2D matrix for the grid.
canonical_grid_state = [[pieces[0] for _ in range(n)] for _ in range(n)]

# Display the grid.
def display_grid(grid_state):
    for i in range(n , 0 , -1):
        # Print number prefix per row.
        print("{:2d}".format(i), end = "  ")
        for j in range(0, n):
            print(grid_state[i - 1][j - 1], end = "  ")

        print("\n")
    print("     ", end = "")
    for i in range(n):
        print("{}".format(alphabet[i]), end = "    ")
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

# TODO Modify Board State
def modify_grid(alpha_index, numeral_index, grid, piece):
    print(numeral_index)
    print(alpha_index)
    grid[numeral_index][alphabet.index(alpha_index) - 1] = piece


while True:
    
    while True:
        # ANSI code to clear the screen.
        print('\033[H\033[J')
        scroll_screen()
        display_grid(canonical_grid_state)

        #TODO Implement bounds checking.
        valid_alpha_chars = alphabet[:n]
        location = (input("Place your piece. For example: A 1\n"))

        location = location.split()

        l_len = len(location)
        print (l_len)

        if l_len < 2:
            continue
        elif l_len > 2:
            continue

        print("here")
        alpha_val = location[0]
        numeral_val = location[1]


        if not alpha_val in valid_alpha_chars:
            continue

        try:
            numeral_val = int (numeral_val) and numeral_val != 0
        except:
            continue

        print("why not work")

        if type(location[0]) == str and type(int(location[1])) == int:
            print("first check")
            print(alpha_val,numeral_val, "1")
            print(alpha_val[:n])

            if  0 < numeral_val <= n:
                print("second check")
                break

    alpha_val = str(location[0])
    numeral_val = int (location[1])

    modify_grid(location[0], (int(location[1])) - 1 , canonical_grid_state, alternate_turns())

    win_check()

# TODO Powerups Spawner
