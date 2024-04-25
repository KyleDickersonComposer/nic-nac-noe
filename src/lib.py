import random
import math

# ANSI escape codes for text colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PINK = "\x1b[38;5;205m"
CYAN = "\x1b[36m"
END = "\033[0m"  # Reset color to default

#TODO: create the gamestate class.
class GameState:
    def __init__(self, _n):
        self.n = _n
        self.xs_placed = 0
        self.os_placed = 0
        self.pieces_to_place_for_each_player_turn = math.floor(math.log(self.n**2,3))
        self.pieces_placed_on_this_player_turn = 0
        self.turn_switch = False
        self.status_message = ""
        self.pieces = [" . ", " X ", " O ", YELLOW + " / " + END, BLUE + " \\ " + END, PINK + " | " + END, CYAN + " - " + END]
        self.grid = [[self.pieces[0] for _ in range(self.n)] for _ in range(self.n)]
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        self.sublist = [" . ", YELLOW + " / " + END, BLUE + " \\ " + END, PINK + " | " + END, CYAN + " - " + END]
        self.list_of_x_and_y = [" X ", " O "]
 

    def current_player_turn(self):

        if self.turn_switch:
            return "{}".format(self.pieces[2])
        else:
            return "{}".format(self.pieces[1])

    def alternate_player_turn(self, _game_state):
        self.turn_switch = not self.turn_switch
        _game_state.pieces_placed_on_this_player_turn = 0 

def display_in_gameloop(_grid, _status_message, _n, _alphabet):
#display first screen
    display_grid(_grid, _n, _alphabet)
    display_status_text(_status_message)

def clean_input(_input_str, _alphabet):
    #Inputs are valid.
    #Convert string coords to int.
    alpha_index = _alphabet.index(_input_str[0])
    numeral_index = int (_input_str[1])
    numeral_index -= 1

    return (alpha_index, numeral_index)

def get_powerup_coords(_n):

    alpha_val = random.randint(0, _n-1)
    numeral_val =  random.randint(0, _n-1)

    return (alpha_val, numeral_val)

def get_random_powerup(_pieces):
    return _pieces[random.randint(3,6)]

def help(_sublist, _grid, _n):
    reduce = []

    for i in range(_n):
        for j in range(_n):
            reduce.append(_grid[i][j])

    for i in range(len(_sublist)):
        if _sublist[i] in reduce:
            return False
    else:
        return True

    

def validate_powerup_placement(_coords, _pieces, _grid, _sublist, _n):
    location = _grid[_coords[0]][_coords[1]]

    if (location != _pieces[1] and location != _pieces[2]) and location == _pieces[0] or location == _pieces[3] or location == _pieces[4] or location == _pieces[5] or location == _pieces[6]:
        return True

    if help(_sublist, _grid, _n):
        draw()
    else:
        return False

def modify_grid(_coords, _piece, _grid, _pieces, _game_state):
    if _piece == _pieces[1]:
        _game_state.xs_placed += 1

    elif _piece == _pieces[2]:
        _game_state.os_placed += 1

    _grid[_coords[0]][_coords[1]] = _piece

    return _grid

def display_grid(grid_state, _n, _alphabet):
    print()
    for i in range(_n):
        # Print number prefix per row.
        print("{}".format(_alphabet[i]), end = "  ")
        for j in range(0, _n):
            print(grid_state[i][j], end = "  ")

        print("\n")
    print("   ", end = "")
    for i in range(_n):
        print("{:2d}".format(i + 1), end = "   ")
    print("\n")

def clear_screen():
    print('\033[H\033[J')
    scroll_screen()

def draw():
    print("Draw Game")
    exit()

def win(_grid, _n, _alphabet, _current_player_turn):
    scroll_screen()
    display_grid(_grid, _n, _alphabet)
    display_status_text("{}'s WIN!".format(_current_player_turn))
    exit(0)

def horizontal_check(_grid, _n, _current_player_turn, _alphabet):
    for i in range(_n):
        count = 0 
        
        for j in range(_n):
            if _grid[i][j] == _current_player_turn:
                count = count + 1

        if count == _n:
            win(_grid, _n, _alphabet, _current_player_turn)
            return True

        elif count != _n and i != _n:
            continue

        else: 
            return False

def vertical_check(_grid, _n, _current_player_turn, _alphabet):
    for i in range(_n):
        count = 0 
        
        for j in range(_n):
            if _grid[j][i] == _current_player_turn:
                count = count + 1

        if count == _n:
            win(_grid, _n, _alphabet, _current_player_turn)
            return True

        elif count != _n and i != _n:
            continue

        else: 
            return False


def diagonal_down_check(_grid, _n, _current_pieces, _alphabet):
    dia_down_count = 0 


    for i in range(0, _n-1):
        if _grid[i][i] == _current_pieces:
            dia_down_count += 1

    if dia_down_count == _n - 1 and _grid[_n-1][_n-1] == _current_pieces:
        win(_grid, _n, _alphabet, _current_pieces)

def diagonal_up_check(_grid, _n, _current_pieces, _alphabet):
    dia_up_count = 0

    j = _n-1

    for i in range(0 , _n-1):
        if _grid[i][j] == _current_pieces:
            dia_up_count += 1
            j -= 1

    if dia_up_count == _n - 1 and _grid[_n-1][0] == _current_pieces:
        win(_grid, _n, _alphabet, _current_pieces)

def win_check(_grid, _n, _current_pieces, _alphabet):
    horizontal_check(_grid, _n, _current_pieces, _alphabet)

    vertical_check(_grid, _n, _current_pieces, _alphabet)

    diagonal_down_check(_grid, _n, _current_pieces, _alphabet)

    diagonal_up_check(_grid, _n, _current_pieces, _alphabet)


def display_status_text(message):
    status_color_wrap = "{}{}{}".format(YELLOW, message, END)
    print(status_color_wrap)

def scroll_screen():
    for _ in range(500):
        print()


def powerup_activation_logic(_coords, _powerup_type, _pieces, _n):
    # Powerup type: /
    print("powerup type val:", _powerup_type)
    if _powerup_type == _pieces[3]:
        print("alpha:{} num:{} powerup:{}".format(_coords, _powerup_type))

        max_effect = _n-1

        effect_size = max_effect - _coords[0]

        for _ in range(effect_size):
            pass

        #foreach step away from [0],[n], max_effect -1
        #only numeral val matters because of how effect is applied to best case only.
        #

    # Powerup type: \
    elif _powerup_type == _pieces[4]:
        print("alpha:{} num:{} powerup:{}".format(_coords, _powerup_type))

    # Powerup type: |
    elif _powerup_type == _pieces[5]:
        print("alpha:{} num:{} powerup:{}".format(_coords, _powerup_type))
    
    # Powerup type: -
    elif _powerup_type == _pieces[6]:
        print("alpha:{} num:{} powerup:{}".format(_coords, _powerup_type))

def piece_is_powerup(_coords, _pieces, _grid):
    if _grid[_coords[0]][_coords[1]] != _pieces[0] and _grid[_coords[0]][_coords[1]] != _pieces[1] and _grid[_coords[0]][_coords[1]] == _pieces[2]:
        return True
    else:
        return False

def get_input(_prompt):
    print(_prompt)
    location = input("Enter coordiates: ")
    location = location.split()
    return location

def overlap_check(_coords, _game_state, _pieces, _grid, _current_player_turn):
    print(_coords, "overlap coords")

    if _grid[_coords[0]][_coords[1]] == _pieces[1] or _grid[_coords[0]][_coords[1]] == _pieces[1]:
        _game_state.status_message = "Place your piece on a dot or powerup"
        return False
    else:
        return True


def valid_input(_coords, _alphabet, _n, _game_state):
    l_len = len(_coords)
    if l_len < 2:

        _game_state.status_message = "Not enough arguments. For example: A 1"
        return False
 
    elif l_len > 2:
        _game_state.status_message = "Too many arguments. For example: A 1"
        return False
 

    valid_alpha_chars = _alphabet[:_n]
    alpha_val = _coords[0]
    numeral_val = _coords[1]

    if not alpha_val in valid_alpha_chars:
        _game_state.status_message = "Not a valid alpha input. For example: A 1"
        return False

    try:
        numeral_val = int (numeral_val)
    except:
        _game_state.status_message = "The second value should be a number. For example: A 1"
        return False

    if  numeral_val < 1 or numeral_val > _n:
        _game_state.status_message = "Number should be between 1 and {}. val: {}.".format(_n, numeral_val)
        return False

    else:
        _game_state.status_message = ""
        return True

def check_for_overlap(_coords, _grid, _pieces):
    #check for X's and O's overlapping each other
    if _grid[_coords[0]][_coords[1]] == _pieces[1] or _grid[_coords[0]][_coords[1]] == _pieces[2]:
        status_message = "Can't place an X or O ontop of on another."
        return False, status_message
    
