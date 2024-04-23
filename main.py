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

pieces_placed_on_this_player_turn = 0

while True:
    # Num of rows/cols.
    try:
        n = int(input("Enter the number of rows and columns desired. Must be a value between 3-52\n"))
    except:
        continue
    if 3 <= n <= 53:
        print()
        break
    
pieces_per_turn =  math.floor(math.log(n**2,5))

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

turn_switch = False

def alternate_turns():
    global turn_switch
    turn_switch = not turn_switch

    global pieces_placed_on_this_player_turn
    pieces_placed_on_this_player_turn = 0 


    if turn_switch:
        return pieces[2]
    else:
        return pieces[1]  

def current_player_turn():
    global turn_switch
    if turn_switch:
        return "{}".format(pieces[2])
    else:
        return "{}".format(pieces[1])
# TODO Modify grid State
def modify_grid(alpha_index, numeral_index, grid, piece):
    # Add overlap checks
    grid[alphabet.index(alpha_index)][numeral_index - 1] = piece

    global xs_placed
    global os_placed

    if piece == pieces[1]:
        xs_placed += 1
    else:
        os_placed += 1

status_message = ""

def win():
    lock_game_state()


def horizontal_check(grid):
    for i in range(n):
        count = 0 
        
        for j in range(n):
            if grid[i][j] == current_player_turn():
                count = count + 1

        if count == n:
            win()
            return True

        elif count != n and i != n:
            continue

        else: 
            return False

def vertical_check(grid):
    for i in range(n):
        count = 0 
        
        for j in range(n):
            if grid[j][i] == current_player_turn():
                count = count + 1

        if count == n:
            win()
            return True

        elif count != n and i != n:
            continue

        else: 
            return False

dia_down_count = 0 
dia_up_count = 0

def diagonal_down_check(grid, current_pieces):
    global dia_down_count
    dia_down_count = 0 

    for i in range(0, n-1):
        if grid[i][i] == current_pieces:
            dia_down_count += 1

    if dia_down_count == n - 1 and grid[n-1][n-1] == current_pieces:
        win()

def diagonal_up_check(grid, current_pieces):
    global dia_up_count
    dia_up_count = 0

    j = n-1

    for i in range(0 , n-1):
        print(j, "val: j")
        if grid[i][j] == current_pieces:
            dia_up_count += 1
            j -= 1

    print(grid[0][n-1])
    print(dia_up_count, "count up")

    if dia_up_count == n - 1 and grid[n-1][0] == current_pieces:
        win()

def win_check():
    horizontal_check(canonical_grid_state)

    vertical_check(canonical_grid_state)

    diagonal_down_check(canonical_grid_state, current_player_turn())

    diagonal_up_check(canonical_grid_state, current_player_turn())

def game_logic_turn():
    global pieces_placed_on_this_player_turn
    pieces_placed_on_this_player_turn += 1


def display_status_text(message):
    status_color_wrap = "{}{}{}".format(YELLOW, message, END)
    print(status_color_wrap)

def lock_game_state():

    #scroll_screen()
    display_grid(canonical_grid_state)
    display_status_text("{}'s WIN!".format(current_player_turn()))

    exit(0)

while True:
    # ANSI code to clear the screen.
    #print('\033[H\033[J')

    game_logic_turn()

    #scroll_screen()
    display_grid(canonical_grid_state)

    display_status_text(status_message)

    status_message = ""

    while True:
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
            modify_grid(alpha_val, numeral_val,  canonical_grid_state, current_player_turn())
            break

    win_check()

    if pieces_placed_on_this_player_turn >= pieces_per_turn:
        alternate_turns()
