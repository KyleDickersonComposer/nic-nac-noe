import random
import main

def debug_mode_toggle(_debug):
    _debug = not _debug

def current_player_turn(_switch, _pieces):
    if _switch:
        return "{}".format(_pieces[2])
    else:
        return "{}".format(_pieces[1])

def modify_grid(alpha_index, numeral_index, piece, _grid, _xs_placed, _os_placed, _pieces, _n, _alphabet):
    if piece == _pieces[1]:
        _xs_placed += 1
    elif piece == _pieces[2]:
        _os_placed += 1

    if (piece == _pieces[1] or piece == _pieces[2])\
        and (piece != _pieces[3] and piece != _pieces[4] and piece != _pieces[5] and piece != _pieces[6])\
        and (_grid[alpha_index][numeral_index-1] == _pieces[3] or _grid[alpha_index][numeral_index-1] == _pieces[4] or _grid[alpha_index][numeral_index-1] == _pieces[5] or _grid[alpha_index][numeral_index-1] == _pieces[6]):
        powerup_logic(alpha_index, numeral_index-1, _grid[alpha_index][numeral_index-1], piece, _grid, _n, _alphabet )

    _grid[alpha_index][numeral_index-1] = piece

    display_grid(_grid, _n, _alphabet)
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


def alternate_turns(_switch, _pieces):
    _switch = not _switch

    global pieces_placed_on_this_player_turn
    pieces_placed_on_this_player_turn = 0 


    if _switch:
        return _pieces[2]
    else:
        return _pieces[1]  


def draw():
    print("Draw Game")
    exit()

def ugly_powerup_placement_checks(_grid, _n, _pieces, _xs_placed, _os_placed, _alphabet):
    try_count = 0

    while True:
        
        powerup_numeral_pos = random.randint(0, _n-1)
        powerup_alpha_pos =  random.randint(0, _n-1)

        random_powerup = _pieces[random.randint(3, 6)]

        if _grid[powerup_alpha_pos][powerup_numeral_pos] != _pieces[1] and _grid[powerup_alpha_pos-1][powerup_numeral_pos] != _pieces[2] and _grid[powerup_alpha_pos][powerup_numeral_pos] == _pieces[0] or _grid[powerup_alpha_pos][powerup_numeral_pos] == _pieces[3] or _grid[powerup_alpha_pos][powerup_numeral_pos] == _pieces[4] or _grid[powerup_alpha_pos][powerup_numeral_pos] == _pieces[5] or _grid[powerup_alpha_pos][powerup_numeral_pos] == _pieces[6]:
            _grid = modify_grid(powerup_alpha_pos, powerup_numeral_pos+1, random_powerup, _grid, _xs_placed, _os_placed, _pieces, _n, _alphabet)
            
            break
        elif try_count >= 10000:
            draw()
        elif _grid[powerup_alpha_pos-1][powerup_numeral_pos-1] != _pieces[0]:
            try_count += 1
        else:
            continue
    return _grid

def win(_grid, _n, _pieces, _alphabet, _turn_switch):
    lock_game_state(_grid, _n, _pieces, _alphabet, _turn_switch)

def horizontal_check(_grid, _n, _pieces, _turn_switch, _alphabet):
    for i in range(_n):
        count = 0 
        
        for j in range(_n):
            if _grid[i][j] == current_player_turn(_turn_switch, _pieces):
                count = count + 1

        if count == _n:
            win(_grid, _n, _pieces, _alphabet, _turn_switch)
            return True

        elif count != _n and i != _n:
            continue

        else: 
            return False

def vertical_check(_grid, _n, _pieces, _turn_switch, _alphabet):
    for i in range(_n):
        count = 0 
        
        for j in range(_n):
            if _grid[j][i] == current_player_turn(_turn_switch, _pieces):
                count = count + 1

        if count == _n:
            win(_grid, _n, _pieces, _turn_switch, _alphabet)
            return True

        elif count != _n and i != _n:
            continue

        else: 
            return False


def diagonal_down_check(_grid, _n, _pieces, _alphabet, _turn_switch):
    dia_down_count = 0 

    for i in range(0, _n-1):
        if _grid[i][i] == _pieces:
            dia_down_count += 1

    if dia_down_count == _n - 1 and _grid[_n-1][_n-1] == _pieces:
        win(_grid, _n, _pieces, _alphabet, _turn_switch)

def diagonal_up_check(_grid, _n, _pieces, _alphabet, _turn_switch):
    dia_up_count = 0

    j = _n-1

    for i in range(0 , _n-1):
        if _grid[i][j] == _pieces:
            dia_up_count += 1
            j -= 1

    if dia_up_count == _n - 1 and _grid[_n-1][0] == _pieces:
        win(_grid, _n, _pieces, _alphabet, _turn_switch)

def win_check(_grid, _turn_switch, _n, _pieces, _alphabet):
    horizontal_check(_grid, _n, _pieces, _turn_switch, _alphabet)

    vertical_check(_grid, _n, _turn_switch, _pieces, _alphabet)

    diagonal_down_check(current_player_turn(_turn_switch, _pieces), _grid, _n, _alphabet, _turn_switch)

    diagonal_up_check(current_player_turn(_turn_switch, _pieces), _grid, _n, _alphabet, _turn_switch)

def game_logic_turn(_pieces_placed_this_player_turn):
    _pieces_placed_this_player_turn += 1


def display_status_text(message):
    status_color_wrap = "{}{}{}".format(main.YELLOW, message, main.END)
    print(status_color_wrap)

def scroll_screen():
    for _ in range(500):
        print()

def lock_game_state(_grid, _n, _pieces, _alphabet, _turn_switch):

    #scroll_screen()
    display_grid(_grid, _n, _alphabet)
    display_status_text("{}'s WIN!".format(current_player_turn(_turn_switch, _pieces)))

    exit(0)

def powerup_logic(alpha_val, numeral_val, powerup_type, activating_piece, _grid, _n, _pieces):
    # Powerup type: /
    print("powerup type val:", powerup_type)
    if powerup_type == _pieces[3]:
        print("alpha:{} num:{} powerup:{}".format(alpha_val,numeral_val,powerup_type))

        max_effect = _n-1

        effect_size = max_effect - alpha_val

        for i in range(effect_size):
            pass

        #foreach step away from [0],[n], max_effect -1
        #only numeral val matters because of how effect is applied to best case only.
        #

    # Powerup type: \
    elif powerup_type == _pieces[4]:
        print("alpha:{} num:{} powerup:{}".format(alpha_val,numeral_val,powerup_type))

    # Powerup type: |
    elif powerup_type == _pieces[5]:
        print("alpha:{} num:{} powerup:{}".format(alpha_val,numeral_val,powerup_type))
    
    # Powerup type: -
    elif powerup_type == _pieces[6]:
        print("alpha:{} num:{} powerup:{}".format(alpha_val,numeral_val,powerup_type))


