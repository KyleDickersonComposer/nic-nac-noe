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
        self.pieces = set([" . ", " X ", " O ", YELLOW + " / " + END, BLUE + " \\ " + END, PINK + " | " + END, CYAN + " - " + END])
        self.grid = [[" . " for _ in range(self.n)] for _ in range(self.n)]
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        self.sub_set_of_replacedable_pieces = set([" . ", YELLOW + " / " + END, BLUE + " \\ " + END, PINK + " | " + END, CYAN + " - " + END])
        self.set_of_x_y = set([" X ", " O "])
        self.set_of_powerups = set([YELLOW + " / " + END, BLUE + " \\ " + END, PINK + " | " + END, CYAN + " - " + END])
        self.powerup = ""
 

    def current_player_turn(self):

        if self.turn_switch:
            return " O "
        else:
            return " X " 

    def alternate_player_turn(self, _game_state):
        self.turn_switch = not self.turn_switch
        _game_state.pieces_placed_on_this_player_turn = 0 


def nested_list_not_cointains_all_elements_of_set(_nested_list, _set):
    for i in _set:
        if not any(i in row for row in _nested_list):
            return True
    else:
        return False

def display_in_gameloop(_game_state):
#display first screen
    display_grid(_game_state.grid, _game_state.n, _game_state.alphabet)
    display_status_text(_game_state.status_message)

def clean_input(_input_str, _alphabet):
    #Inputs are valid.
    #Convert string coords to int.
    alpha_index = _alphabet.index(_input_str[0])
    numeral_index = int (_input_str[1])
    #fix offset
    numeral_index -= 1

    return (alpha_index, numeral_index)

def get_random_powerup_coords(_n):

    alpha_val = random.randint(0, _n-1)
    numeral_val =  random.randint(0, _n-1)

    return (alpha_val, numeral_val)

def get_random_powerup(_set_of_powerups):
    powerup = random.choice(list(_set_of_powerups))

    return powerup

def validate_powerup_placement(_coords, _grid, _sub_set_of_overridable_pieces, _n):
    location = _grid[_coords[0]][_coords[1]]
    reduce = set([])

    #reduce the list
    for i in range(_n):
        for j in range(_n):
            reduce.add(_grid[i][j])

    #check if piece is in sublist and return true
    if location in _sub_set_of_overridable_pieces:
        return True

    else:
        return False

def modify_grid(_coords, _piece, _grid, _game_state):
    if _piece == " X ":
        _game_state.xs_placed += 1

    elif _piece == " O ":
        _game_state.os_placed += 1

    _grid[_coords[0]][_coords[1]] = _piece

    return _grid

def draw_check(_game_state):
    rset = {i for sub_l in _game_state.grid for i in sub_l}
    print("rset val", rset)
    print(_game_state.grid)
    print("result", rset in _game_state.set_of_x_y)
    print(_game_state.set_of_x_y)
    
    if rset == _game_state.set_of_x_y:
        draw(_game_state)
    else:
        return False


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

def draw(_game_state):
    clear_screen()
    display_grid(_game_state.grid, _game_state.n, _game_state.alphabet)
    display_status_text("Draw Game")
    exit()

def win(_grid, _n, _alphabet, _current_player_turn):
    clear_screen()
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

def powerup_activation_logic(_coords, _this_powerup, _list_of_powerups, _n):

    # Powerup type: /
    print("powerup type val:", _this_powerup)
    print("boom!")
    #wrong
    if _this_powerup == _list_of_powerups[0]:
        print("alpha:{} num:{} powerup:{}".format(_coords[0], _coords[1], _this_powerup))

        max_effect = _n-1

        effect_size = max_effect - _coords[0]

        for _ in range(effect_size):
            print("test")
            pass

        #foreach step away from [0],[n], max_effect -1
        #only numeral val matters because of how effect is applied to best case only.
        #

    # Powerup type: \
    elif _this_powerup == _list_of_powerups[1]:
        print("alpha:{} num:{} powerup:{}".format(_coords[0], _coords[1], _this_powerup))

    # Powerup type: |
    elif _this_powerup == _list_of_powerups[2]:
        print("alpha:{} num:{} powerup:{}".format(_coords[0], _coords[1], _this_powerup))
    
    # Powerup type: -
    # returned yellow /
    elif _this_powerup == _list_of_powerups[3]:
        print("alpha:{} num:{} powerup:{}".format(_coords[0], _coords[1], _this_powerup))

def piece_is_powerup(_coords, _grid, _set_of_powerups):
        if _grid[_coords[0]][_coords[1]] in _set_of_powerups:

            return True

        else:
            return False


def get_input(_prompt):
    print(_prompt)
    location = input("Enter coordiates: ")
    location = location.split()
    return location

def overlap_check(_coords, _game_state: GameState, _grid):

    location = _grid[_coords[0]][_coords[1]]

    if location in _game_state.set_of_x_y:
        _game_state.status_message = "Place your piece on a dot or powerup."
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
