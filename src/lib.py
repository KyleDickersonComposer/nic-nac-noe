import random
import main

def debug_mode_toggle(_debug):
    _debug = not _debug

def current_player_turn(_switch):
    if _switch:
        return "{}".format(main.pieces[2])
    else:
        return "{}".format(main.pieces[1])

def modify_grid(alpha_index, numeral_index, _piece, _grid):
    if _piece == main.pieces[1]:
        main.xs_placed += 1
    elif _piece == main.pieces[2]:
        main.os_placed += 1

    if (_piece == main.pieces[1] or _piece == main.pieces[2])\
        and (_piece != main.pieces[3] and _piece != main.pieces[4] and _piece != main.pieces[5] and _piece != main.pieces[6])\
        and (main.grid[alpha_index][numeral_index-1] == main.pieces[3] or main.grid[alpha_index][numeral_index-1] == main.pieces[4] or main.grid[alpha_index][numeral_index-1] == main.pieces[5] or main.grid[alpha_index][numeral_index-1] == main.pieces[6]):
        powerup_logic(alpha_index, numeral_index-1, main.grid[alpha_index][numeral_index-1])

    main.grid[alpha_index][numeral_index-1] = _piece

    display_grid(_grid)
    return _grid

def display_grid(grid_state):
    print()
    for i in range(main.n):
        # Print number prefix per row.
        print("{}".format(main.alphabet[i]), end = "  ")
        for j in range(0, main.n):
            print(grid_state[i][j], end = "  ")

        print("\n")
    print("   ", end = "")
    for i in range(main.n):
        print("{:2d}".format(i + 1), end = "   ")
    print("\n")


def alternate_turns(_switch):
    _switch = not _switch

    global pieces_placed_on_this_player_turn
    pieces_placed_on_this_player_turn = 0 


    if _switch:
        return main.pieces[2]
    else:
        return main.pieces[1]  


def draw():
    print("Draw Game")
    exit()

def ugly_powerup_placement_checks(_grid):
    try_count = 0

    while True:
        
        powerup_numeral_pos = random.randint(0, main.n-1)
        powerup_alpha_pos =  random.randint(0, main.n-1)

        random_powerup = main.pieces[random.randint(3, 6)]

        if _grid[powerup_alpha_pos][powerup_numeral_pos] != main.pieces[1] and _grid[powerup_alpha_pos-1][powerup_numeral_pos] != main.pieces[2] and _grid[powerup_alpha_pos][powerup_numeral_pos] == main.pieces[0] or _grid[powerup_alpha_pos][powerup_numeral_pos] == main.pieces[3] or _grid[powerup_alpha_pos][powerup_numeral_pos] == main.pieces[4] or _grid[powerup_alpha_pos][powerup_numeral_pos] == main.pieces[5] or _grid[powerup_alpha_pos][powerup_numeral_pos] == main.pieces[6]:
            _grid = modify_grid(powerup_alpha_pos, powerup_numeral_pos+1, random_powerup, _grid)
            
            break
        elif try_count >= 10000:
            draw()
        elif _grid[powerup_alpha_pos-1][powerup_numeral_pos-1] != main.pieces[0]:
            try_count += 1
        else:
            continue
    return _grid

def win(_grid, _turn_switch):
    lock_game_state(_grid, _turn_switch)

def horizontal_check(_grid, _turn_switch):
    for i in range(main.n):
        count = 0 
        
        for j in range(main.n):
            if _grid[i][j] == current_player_turn(_turn_switch):
                count = count + 1

        if count == main.n:
            win(_grid, _turn_switch)
            return True

        elif count != main.n and i != main.n:
            continue

        else: 
            return False

def vertical_check(_grid, _turn_switch):
    for i in range(main.n):
        count = 0 
        
        for j in range(main.n):
            if _grid[j][i] == current_player_turn(_turn_switch):
                count = count + 1

        if count == main.n:
            win(_grid, _turn_switch)
            return True

        elif count != main.n and i != main.n:
            continue

        else: 
            return False


def diagonal_down_check(_grid, _turn_switch):
    dia_down_count = 0 

    for i in range(0, main.n-1):
        if _grid[i][i] == main.pieces:
            dia_down_count += 1

    if dia_down_count == main.n - 1 and _grid[main.n-1][main.n-1] == main.pieces:
        win(_grid, _turn_switch)

def diagonal_up_check(_grid, _turn_switch):
    dia_up_count = 0

    j = main.n-1

    for i in range(0 , main.n-1):
        if _grid[i][j] == main.pieces:
            dia_up_count += 1
            j -= 1

    if dia_up_count == main.n - 1 and _grid[main.n-1][0] == main.pieces:
        win(_grid, _turn_switch)

def win_check(_grid, _turn_switch):
    horizontal_check(_grid, _turn_switch)

    vertical_check(_grid, _turn_switch)

    diagonal_down_check(_grid, _turn_switch)

    diagonal_up_check(_grid, _turn_switch)


def display_status_text(message):
    status_color_wrap = "{}{}{}".format(main.YELLOW, message, main.END)
    print(status_color_wrap)

def scroll_screen():
    for _ in range(500):
        print()

def lock_game_state(_grid, _turn_switch):

    #scroll_screen()
    display_grid(_grid)
    display_status_text("{}'s WIN!".format(current_player_turn(_turn_switch)))

    exit(0)

def powerup_logic(alpha_val, numeral_val, powerup_type):
    # Powerup type: /
    print("powerup type val:", powerup_type)
    if powerup_type == main.pieces[3]:
        print("alpha:{} num:{} powerup:{}".format(alpha_val,numeral_val,powerup_type))

        max_effect = main.n-1

        effect_size = max_effect - alpha_val

        for _ in range(effect_size):
            pass

        #foreach step away from [0],[n], max_effect -1
        #only numeral val matters because of how effect is applied to best case only.
        #

    # Powerup type: \
    elif powerup_type == main.pieces[4]:
        print("alpha:{} num:{} powerup:{}".format(alpha_val,numeral_val,powerup_type))

    # Powerup type: |
    elif powerup_type == main.pieces[5]:
        print("alpha:{} num:{} powerup:{}".format(alpha_val,numeral_val,powerup_type))
    
    # Powerup type: -
    elif powerup_type == main.pieces[6]:
        print("alpha:{} num:{} powerup:{}".format(alpha_val,numeral_val,powerup_type))


