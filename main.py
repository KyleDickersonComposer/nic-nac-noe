import math

# TODO Grid Display
# ANSI escape codes for text colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PINK = "\x1b[38;5;205m"
CYAN = "\x1b[36m"
END = "\033[0m"  # Reset color to default

xs_placed = 0
os_placed = 0 


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

def current_player_turn():
    global turn_switch
    if turn_switch:
        return "X"
    else:
        return "O"



# TODO Modify grid State
def modify_grid(alpha_index, numeral_index, grid, piece):
    # Add overlap checks
    grid[alphabet.index(alpha_index)][numeral_index - 1] = piece

    global xs_placed
    global os_placed
    if piece == pieces[1]:
        xs_placed = xs_placed + 1
    else:
        os_placed = os_placed + 1



status_message = ""


while True:
    display_grid(canonical_grid_state)
    
    while True:
        # ANSI code to clear the screen.
        #print('\033[H\033[J')

        scroll_screen()
        display_grid(canonical_grid_state)
        status_color_wrap = "{}{}{}".format(YELLOW, status_message, END)
        print(status_color_wrap)
        status_message = ""

        #TODO Implement bounds checking.
        valid_alpha_chars = alphabet[:n]
        hud_text = "{}'s turn. Xs placed: {}. Os placed: {}. \n".format(current_player_turn(), xs_placed, os_placed)
        location = input(hud_text)

        location = location.split()

        l_len = len(location)

        if l_len < 2:
            status_message = "Not enough arguments. For example: A 1"
            continue
        elif l_len > 2:
            status_message = "Too many arguments. For example: A 1"
            continue

        alpha_val = location[0]
        numeral_val = location[1]

        if not alpha_val in valid_alpha_chars:
            status_message = "Not a valid alpha input. For example: A 1"
            continue

        try:
            numeral_val = int (numeral_val)
        except:
            status_message = "the second value should be a number. For example: A 1"
            continue
        
        if  numeral_val < 1 or numeral_val > n:
            status_message = "Number should be between 1 and {}. val: {}.".format(n, numeral_val)
            continue

        if canonical_grid_state[alphabet.index(alpha_val)][numeral_val-1] == pieces[1] or canonical_grid_state[alphabet.index(alpha_val)][numeral_val-1] == pieces[2]:
            continue
        else:   
            modify_grid(alpha_val, numeral_val,  canonical_grid_state, alternate_turns())

        win_check(canonical_grid_state)
