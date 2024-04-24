import math
import random

#Debug Mode
debug = False

def debug_mode_toggle(_debug):
    _debug = not _debug

#Enable debug mode here
debug_mode_toggle(debug)

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

def current_player_turn(_switch):
    if _switch:
        return "{}".format(pieces[2])
    else:
        return "{}".format(pieces[1])

def modify_grid(alpha_index, numeral_index, piece, _grid, _xs_placed, _os_placed):
    if piece == pieces[1]:
        _xs_placed += 1
    elif piece == pieces[2]:
        _os_placed += 1

    if (piece == pieces[1] or piece == pieces[2])\
        and (piece != pieces[3] and piece != pieces[4] and piece != pieces[5] and piece != pieces[6])\
        and (_grid[alpha_index][numeral_index-1] == pieces[3] or _grid[alpha_index][numeral_index-1] == pieces[4] or _grid[alpha_index][numeral_index-1] == pieces[5] or _grid[alpha_index][numeral_index-1] == pieces[6]):
        powerup_logic(alpha_index, numeral_index-1, _grid[alpha_index][numeral_index-1], piece, grid)

    _grid[alpha_index][numeral_index-1] = piece

    return _grid


pieces = [" . ", " X ", " O ", YELLOW + " / " + END, BLUE + " \\ " + END, PINK + " | " + END, CYAN + " - " + END]

pieces_placed_on_this_player_turn = 0

while True:
    print('\033[H\033[J')

    # Num of rows/cols.
    try:
        n = int(input("Enter the number of rows and columns desired. Must be a value between 3-52\n"))
    except:
        continue
    if 3 <= n <= 53:
        print()
        break
    
#pieces_per_turn = math.floor(math.log(n**2,3))
pieces_per_turn = 1

# Nested loop comprehension to create the 2D matrix for the grid.
grid = [[pieces[0] for _ in range(n)] for _ in range(n)]

# Display the grid.
def display_grid(grid_state):
    print("Pieces to place per player turn", pieces_per_turn)
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

# Spacing for x axis names.
# Values for x axis names.
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Print x axis names per grid unit.
def scroll_screen():
    for _ in range(500):
        print()

turn_switch = False

def alternate_turns(_switch):
    _switch = not _switch

    global pieces_placed_on_this_player_turn
    pieces_placed_on_this_player_turn = 0 


    if turn_switch:
        return pieces[2]
    else:
        return pieces[1]  

def draw():
    print("Draw Game")
    exit()

def ugly_powerup_placement_checks():
    global grid

    try_count = 0

    while True:
        
        powerup_numeral_pos = random.randint(0, n-1)
        powerup_alpha_pos =  random.randint(0, n-1)

        random_powerup = pieces[random.randint(3, 6)]

        if grid[powerup_alpha_pos][powerup_numeral_pos] != pieces[1] and grid[powerup_alpha_pos-1][powerup_numeral_pos] != pieces[2] and grid[powerup_alpha_pos][powerup_numeral_pos] == pieces[0] or grid[powerup_alpha_pos][powerup_numeral_pos] == pieces[3] or grid[powerup_alpha_pos][powerup_numeral_pos] == pieces[4] or grid[powerup_alpha_pos][powerup_numeral_pos] == pieces[5] or grid[powerup_alpha_pos][powerup_numeral_pos] == pieces[6]:
            grid = modify_grid(powerup_alpha_pos, powerup_numeral_pos+1, random_powerup, grid, xs_placed, os_placed)
            
            break
        elif try_count >= 10000:
            draw()
        elif grid[powerup_alpha_pos-1][powerup_numeral_pos-1] != pieces[0]:
            try_count += 1
        else:
            continue
            

status_message = ""

def win():
    lock_game_state()

def horizontal_check():
    for i in range(n):
        count = 0 
        
        for j in range(n):
            if grid[i][j] == current_player_turn(turn_switch):
                count = count + 1

        if count == n:
            win()
            return True

        elif count != n and i != n:
            continue

        else: 
            return False

def vertical_check():
    for i in range(n):
        count = 0 
        
        for j in range(n):
            if grid[j][i] == current_player_turn(turn_switch):
                count = count + 1

        if count == n:
            win()
            return True

        elif count != n and i != n:
            continue

        else: 
            return False


def diagonal_down_check(current_pieces):
    dia_down_count = 0 

    for i in range(0, n-1):
        if grid[i][i] == current_pieces:
            dia_down_count += 1

    if dia_down_count == n - 1 and grid[n-1][n-1] == current_pieces:
        win()

def diagonal_up_check(current_pieces):
    dia_up_count = 0

    j = n-1

    for i in range(0 , n-1):
        if grid[i][j] == current_pieces:
            dia_up_count += 1
            j -= 1

    if dia_up_count == n - 1 and grid[n-1][0] == current_pieces:
        win()

def win_check():
    horizontal_check()

    vertical_check()

    diagonal_down_check(current_player_turn(turn_switch))

    diagonal_up_check(current_player_turn(turn_switch))

def game_logic_turn(_pieces_placed_this_player_turn):
    _pieces_placed_this_player_turn += 1


def display_status_text(message):
    status_color_wrap = "{}{}{}".format(YELLOW, message, END)
    print(status_color_wrap)

def lock_game_state():

    scroll_screen()
    display_grid(grid)
    display_status_text("{}'s WIN!".format(current_player_turn(turn_switch)))

    exit(0)

def powerup_logic(alpha_val, numeral_val, powerup_type, activating_piece, _grid):
    # Powerup type: /
    print("powerup type val:", powerup_type)
    if powerup_type == pieces[3]:
        print("alpha:{} num:{} powerup:{}".format(alpha_val,numeral_val,powerup_type))

        global max_effect
        global grid

        max_effect = n-1

        effect_size = max_effect - alpha_val

        for i in range(effect_size):
            pass


        #foreach step away from [0],[n], max_effect -1
        #only numeral val matters because of how effect is applied to best case only.
        #

    # Powerup type: \
    elif powerup_type == pieces[4]:
        print("alpha:{} num:{} powerup:{}".format(alpha_val,numeral_val,powerup_type))

    # Powerup type: |
    elif powerup_type == pieces[5]:
        print("alpha:{} num:{} powerup:{}".format(alpha_val,numeral_val,powerup_type))
    
    # Powerup type: -
    elif powerup_type == pieces[6]:
        print("alpha:{} num:{} powerup:{}".format(alpha_val,numeral_val,powerup_type))

while True:
    if debug == False:

        # ANSI code to clear the screen.
        print('\033[H\033[J')
        scroll_screen()

    display_grid(grid)

    if game_logic_turn(pieces_placed_on_this_player_turn) == True:
        alternate_turns(turn_switch)


    display_status_text(status_message)

    status_message = ""

    while True:
        #Check for Draw


        #TODO Implement bounds checking.
        valid_alpha_chars = alphabet[:n]
        hud_text = "{}'s turn. Xs placed: {}. Os placed: {}. \n".format(current_player_turn(turn_switch), xs_placed, os_placed)
        location = input(hud_text)

        location = location.split()

        l_len = len(location)

        if l_len < 2:
            status_message = "Not enough arguments. For example: A 1"
            display_grid(grid)
            display_status_text(status_message)
            continue
        elif l_len > 2:
            status_message = "Too many arguments. For example: A 1"
            display_grid(grid)
            display_status_text(status_message)
            continue

        alpha_val = location[0]
        numeral_val = location[1]

        if not alpha_val in valid_alpha_chars:
            status_message = "Not a valid alpha input. For example: A 1"
            display_grid(grid)
            display_status_text(status_message)
            continue

        try:
            numeral_val = int (numeral_val)
        except:
            status_message = "the second value should be a number. For example: A 1"
            display_grid(grid)
            display_status_text(status_message)
            continue
        
        if  numeral_val < 1 or numeral_val > n:
            status_message = "Number should be between 1 and {}. val: {}.".format(n, numeral_val)
            display_grid(grid)
            display_status_text(status_message)
            continue

        if grid[alphabet.index(alpha_val)][numeral_val-1] == pieces[1] or grid[alphabet.index(alpha_val)][numeral_val-1] == pieces[2]:
            display_grid(grid)
            display_status_text(status_message)
            continue
        else:   
            grid = modify_grid(alphabet.index(alpha_val), numeral_val, current_player_turn(turn_switch), grid, xs_placed, os_placed)
            status_message = ""
            break

    win_check()


    if pieces_placed_on_this_player_turn >= pieces_per_turn:
        alternate_turns(turn_switch)
        ugly_powerup_placement_checks()
