import random
import math

#remove comment to enable.
#debug = debug_mode_toggle(debug)

# TODO Grid Display
# ANSI escape codes for text colors

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PINK = "\x1b[38;5;205m"
CYAN = "\x1b[36m"
END = "\033[0m"  # Reset color to default

n = 0 

xs_placed = 0

os_placed = 0 

pieces = [" . ", " X ", " O ", YELLOW + " / " + END, BLUE + " \\ " + END, PINK + " | " + END, CYAN + " - " + END]

pieces_placed_on_this_player_turn = 0
    
pieces_per_turn = math.floor(math.log(n**2,3))

# Nested loop comprehension to create the 2D matrix for the grid.
def get_grid(_n):
    return [[pieces[0] for _ in range(_n)] for _ in range(_n)]

# Values for x axis names.
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Print x axis names per grid unit.

turn_switch = False
status_message = ""

def get_xs_placed():
    global xs_placed
    return xs_placed

def get_os_placed():
    global os_placed
    return os_placed

def x_placed():
    global xs_placed
    xs_placed += 1

def o_placed():
    global os_placed
    os_placed += 1

def debug_mode_toggle(_debug):
    _debug = not _debug

def current_player_turn():
    global turn_switch

    if turn_switch:
        return "{}".format(pieces[2])
    else:
        return "{}".format(pieces[1])

def modify_grid(_coords, _piece, _grid):
    if _piece == pieces[1]:
        x_placed()

    elif _piece == pieces[2]:
        o_placed()

    if (_piece == pieces[1] or _piece == pieces[2])\
        and (_piece != pieces[3] and _piece != pieces[4] and _piece != pieces[5] and _piece != pieces[6])\
        and (_grid[_coords[0]][_coords[1]] == pieces[3] or _grid[_coords[0]][_coords[1]] == pieces[4] or _grid[_coords[0]][_coords[1]] == pieces[5] or _grid[_coords[0]][_coords[1]] == pieces[6]):
        powerup_logic(_coords, _grid[_coords[0]][_coords[1]])

    _grid[_coords[0]][_coords[1]] = _piece

    display_grid(_grid)
    return _grid

def display_grid(grid_state):
    print()
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


def alternate_turns(_switch):
    _switch = not _switch

    global pieces_placed_on_this_player_turn
    pieces_placed_on_this_player_turn = 0 


    if _switch:
        return pieces[2]
    else:
        return pieces[1]  


def draw():
    print("Draw Game")
    exit()

def ugly_powerup_placement_checks(_grid):
    try_count = 0

    while True:
        powerup_numeral_pos = random.randint(0, n-1)
        powerup_alpha_pos =  random.randint(0, n-1)

        random_powerup = pieces[random.randint(3, 6)]

        if _grid[powerup_alpha_pos][powerup_numeral_pos] != pieces[1] and _grid[powerup_alpha_pos-1][powerup_numeral_pos] != pieces[2] and _grid[powerup_alpha_pos][powerup_numeral_pos] == pieces[0] or _grid[powerup_alpha_pos][powerup_numeral_pos] == pieces[3] or _grid[powerup_alpha_pos][powerup_numeral_pos] == pieces[4] or _grid[powerup_alpha_pos][powerup_numeral_pos] == pieces[5] or _grid[powerup_alpha_pos][powerup_numeral_pos] == pieces[6]:
            #random +1 might be a bug or something.
            _grid = modify_grid((powerup_alpha_pos, powerup_numeral_pos+1), random_powerup, _grid)
            
            break
        elif try_count >= 10000:
            draw()
        elif _grid[powerup_alpha_pos-1][powerup_numeral_pos-1] != pieces[0]:
            try_count += 1
        else:
            continue
    return _grid

def win(_grid):
    lock_game_state(_grid)

def horizontal_check(_grid):
    for i in range(n):
        count = 0 
        
        for j in range(n):
            if _grid[i][j] == current_player_turn():
                count = count + 1

        if count == n:
            win(_grid)
            return True

        elif count != n and i != n:
            continue

        else: 
            return False

def vertical_check(_grid):
    for i in range(n):
        count = 0 
        
        for j in range(n):
            if _grid[j][i] == current_player_turn():
                count = count + 1

        if count == n:
            win(_grid)
            return True

        elif count != n and i != n:
            continue

        else: 
            return False


def diagonal_down_check(_grid):
    dia_down_count = 0 

    for i in range(0, n-1):
        if _grid[i][i] == pieces:
            dia_down_count += 1

    if dia_down_count == n - 1 and _grid[n-1][n-1] == pieces:
        win(_grid)

def diagonal_up_check(_grid):
    dia_up_count = 0

    j = n-1

    for i in range(0 , n-1):
        if _grid[i][j] == pieces:
            dia_up_count += 1
            j -= 1

    if dia_up_count == n - 1 and _grid[n-1][0] == pieces:
        win(_grid)

def win_check(_grid):
    horizontal_check(_grid)

    vertical_check(_grid)

    diagonal_down_check(_grid)

    diagonal_up_check(_grid)


def display_status_text(message):
    status_color_wrap = "{}{}{}".format(YELLOW, message, END)
    print(status_color_wrap)

def scroll_screen():
    for _ in range(500):
        print()

def lock_game_state(_grid):
    scroll_screen()
    display_grid(_grid)
    display_status_text("{}'s WIN!".format(current_player_turn()))
    exit(0)

def powerup_logic(_coords, _powerup_type):
    # Powerup type: /
    print("powerup type val:", _powerup_type)
    if _powerup_type == pieces[3]:
        print("alpha:{} num:{} powerup:{}".format(_coords, _powerup_type))

        max_effect = n-1

        effect_size = max_effect - _coords[0]

        for _ in range(effect_size):
            pass

        #foreach step away from [0],[n], max_effect -1
        #only numeral val matters because of how effect is applied to best case only.
        #

    # Powerup type: \
    elif _powerup_type == pieces[4]:
        print("alpha:{} num:{} powerup:{}".format(_coords, _powerup_type))

    # Powerup type: |
    elif _powerup_type == pieces[5]:
        print("alpha:{} num:{} powerup:{}".format(_coords, _powerup_type))
    
    # Powerup type: -
    elif _powerup_type == pieces[6]:
        print("alpha:{} num:{} powerup:{}".format(_coords, _powerup_type))

def get_n_val():

    try:
        n = int(input("Enter the number of rows and columns desired. Must be a value between 3-52\n"))
    except:
        return False

    if 3 <= n <= 53:
        return True


def display_in_gameloop(_grid):
#display first screen
    display_grid(_grid)
    display_status_text(status_message)

def get_input(_prompt):
    location = input(_prompt)
    location = location.split()
    return location

def valid_input(_input):

    #validation logic is displaying the grid == bad.

    #check piece location input

    valid_alpha_chars = alphabet[:n]

    l_len = len(_input)
    if l_len < 2:
        status_message = "Not enough arguments. For example: A 1"
        return False, status_message
 
    elif l_len > 2:
        status_message = "Too many arguments. For example: A 1"
        return False, status_message
 

    alpha_val = _input[0]
    numeral_val = _input[1]

    if not alpha_val in valid_alpha_chars:
        status_message = "Not a valid alpha input. For example: A 1"
        return False, status_message

    try:
        numeral_val = int (numeral_val)
    except:
        status_message = "the second value should be a number. For example: A 1"
        return False, status_message

    if  numeral_val < 1 or numeral_val > n:
        status_message = "Number should be between 1 and {}. val: {}.".format(n, numeral_val)
        return False, status_message
    else:
        return True

def check_for_overlap(_coords, _grid):
    #check for X's and O's overlapping each other
    if _grid[_coords[0]][_coords[1]] == pieces[1] or _grid[_coords[0]][_coords[1]] == pieces[2]:
        status_message = "Can't place an X or O ontop of on another."
        return False, status_message
    
def handle_change_turn(_grid):

    print(pieces_placed_on_this_player_turn, "placed", pieces_per_turn, "placements per turn")
    if pieces_placed_on_this_player_turn >= pieces_per_turn:
        alternate_turns(turn_switch)
        return ugly_powerup_placement_checks(_grid)

