import random
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

n = 0 

xs_placed = 0

os_placed = 0 

pieces_placed_on_this_player_turn = 0

pieces_to_place_for_each_player_turn = 0 

turn_switch = False

status_message = ""

def get_pieces():
    return [" . ", " X ", " O ", YELLOW + " / " + END, BLUE + " \\ " + END, PINK + " | " + END, CYAN + " - " + END]

def get_pieces_per_player_turn(_n):
    return math.floor(math.log(_n**2,3))

def get_alphabet():
    # Values for x axis names.
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# Nested loop comprehension to create the 2D matrix for the grid.
def get_grid(_n):
    pieces = get_pieces()

    return [[pieces[0] for _ in range(_n)] for _ in range(_n)]

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

def current_player_turn():
    pieces = get_pieces()

    global turn_switch

    if turn_switch:
        return "{}".format(pieces[2])
    else:
        return "{}".format(pieces[1])

def modify_grid(_coords, _piece, _grid):
    pieces = get_pieces()
    alphabet = get_alphabet()


    #Inputs are valid.
    #Convert string coords to int.
    alpha_index = alphabet.index(_coords[0])
    numeral_index = int (_coords[1])
    numeral_index -= 1

    if _piece == pieces[1]:
        x_placed()

    elif _piece == pieces[2]:
        o_placed()

    if (_piece == pieces[1] or _piece == pieces[2])\
        and (_piece != pieces[3] and _piece != pieces[4] and _piece != pieces[5] and _piece != pieces[6])\
        and (_grid[alpha_index][numeral_index] == pieces[3] or _grid[alpha_index][numeral_index] == pieces[4] or _grid[alpha_index][numeral_index] == pieces[5] or _grid[alpha_index][numeral_index] == pieces[6]):
        powerup_logic(_coords, _grid[alpha_index][numeral_index])

    _grid[alpha_index][numeral_index] = _piece

    return _grid

def display_grid(grid_state):
    n = get_n_val()
    alphabet = get_alphabet()

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

def clear_screen():
    print('\033[H\033[J')
    scroll_screen()

def alternate_player_turn():
    global turn_switch

    turn_switch = not turn_switch

    set_pieces_placed_on_this_player_turn(0)

    if turn_switch:
        current_player_turn()
    else:
        current_player_turn()


def draw():
    print("Draw Game")
    exit()

def ugly_powerup_placement_checks(_grid):
    pieces = get_pieces()
    n = get_n_val()

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
    n = get_n_val()
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
    n = get_n_val()
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
    n = get_n_val()
    current_pieces = current_player_turn()
    dia_down_count = 0 


    for i in range(0, n-1):
        if _grid[i][i] == current_pieces:
            dia_down_count += 1

    if dia_down_count == n - 1 and _grid[n-1][n-1] == current_pieces:
        win(_grid)

def diagonal_up_check(_grid):
    n = get_n_val()
    current_pieces = current_player_turn()
    dia_up_count = 0

    j = n-1

    for i in range(0 , n-1):
        if _grid[i][j] == current_pieces:
            dia_up_count += 1
            j -= 1

    if dia_up_count == n - 1 and _grid[n-1][0] == current_pieces:
        win(_grid)

def win_check(_grid):
    print("checking win")
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
    pieces = get_pieces()
    n = get_n_val()
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

def init_n_val():

    try:
        n = int(input("Enter desired board size: "))
    except:
        return False

    if 3 <= n <= 53:
        return n

def get_n_val():
    global n
    return n

def set_n_val(_n):
    global n 
    n = _n

def set_status_message(_message):
    global status_message
    status_message = _message

def get_status_message():
    global status_message
    return status_message

def display_in_gameloop(_grid):
#display first screen
    display_grid(_grid)
    display_status_text(status_message)

def get_input(_prompt):
    print(_prompt)
    location = input("Enter coordiates: ")
    location = location.split()
    return location

def valid_input(_input):

    #validation logic is displaying the grid == bad.

    #check piece location input

    alphabet = get_alphabet()

    n = get_n_val()


    l_len = len(_input)
    if l_len < 2:

        set_status_message("Not enough arguments. For example: A 1")
        return False
 
    elif l_len > 2:
        set_status_message("Too many arguments. For example: A 1")
        return False
 

    valid_alpha_chars = alphabet[:n]
    alpha_val = _input[0]
    numeral_val = _input[1]

    if not alpha_val in valid_alpha_chars:
        set_status_message("Not a valid alpha input. For example: A 1")
        return False

    try:
        numeral_val = int (numeral_val)
    except:
        set_status_message("The second value should be a number. For example: A 1")
        return False

    if  numeral_val < 1 or numeral_val > n:
        set_status_message("Number should be between 1 and {}. val: {}.".format(n, numeral_val))
        return False

    else:
        set_status_message("")
        return True

def check_for_overlap(_coords, _grid):
    pieces = get_pieces()
    #check for X's and O's overlapping each other
    if _grid[_coords[0]][_coords[1]] == pieces[1] or _grid[_coords[0]][_coords[1]] == pieces[2]:
        status_message = "Can't place an X or O ontop of on another."
        return False, status_message
    
def get_pieces_placed_on_this_player_turn():
    global pieces_placed_on_this_player_turn
    return pieces_placed_on_this_player_turn

def set_pieces_placed_on_this_player_turn(_val):
    global pieces_placed_on_this_player_turn
    pieces_placed_on_this_player_turn = _val

def iterate_pieces_placed_on_this_player_turn():
    global pieces_placed_on_this_player_turn
    pieces_placed_on_this_player_turn += 1


def handle_change_turn(_grid):
    global pieces_to_place_for_each_player_turn

    pieces_placed_on_this_player_turn = get_pieces_placed_on_this_player_turn()
    pieces_per_turn = pieces_to_place_for_each_player_turn

    print(pieces_placed_on_this_player_turn, "placed", pieces_per_turn, "placements per turn")
    if pieces_placed_on_this_player_turn >= pieces_per_turn:
        alternate_player_turn()
        return ugly_powerup_placement_checks(_grid)

