
def debug_mode_toggle(_debug):
    _debug = not _debug

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

    display_grid(_grid)
    return _grid

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
            _grid = modify_grid(powerup_alpha_pos, powerup_numeral_pos+1, random_powerup, grid, xs_placed, os_placed)
            
            break
        elif try_count >= 10000:
            draw()
        elif _grid[powerup_alpha_pos-1][powerup_numeral_pos-1] != pieces[0]:
            try_count += 1
        else:
            continue
    return _grid

def win():
    lock_game_state()

def horizontal_check(_grid):
    for i in range(n):
        count = 0 
        
        for j in range(n):
            if _grid[i][j] == current_player_turn(turn_switch):
                count = count + 1

        if count == n:
            win()
            return True

        elif count != n and i != n:
            continue

        else: 
            return False

def vertical_check(_grid):
    for i in range(n):
        count = 0 
        
        for j in range(n):
            if _grid[j][i] == current_player_turn(turn_switch):
                count = count + 1

        if count == n:
            win()
            return True

        elif count != n and i != n:
            continue

        else: 
            return False


def diagonal_down_check(current_pieces, _grid):
    dia_down_count = 0 

    for i in range(0, n-1):
        if _grid[i][i] == current_pieces:
            dia_down_count += 1

    if dia_down_count == n - 1 and _grid[n-1][n-1] == current_pieces:
        win()

def diagonal_up_check(current_pieces, _grid):
    dia_up_count = 0

    j = n-1

    for i in range(0 , n-1):
        if _grid[i][j] == current_pieces:
            dia_up_count += 1
            j -= 1

    if dia_up_count == n - 1 and _grid[n-1][0] == current_pieces:
        win()

def win_check():
    horizontal_check(grid)

    vertical_check(grid)

    diagonal_down_check(current_player_turn(turn_switch), grid)

    diagonal_up_check(current_player_turn(turn_switch), grid)

def game_logic_turn(_pieces_placed_this_player_turn):
    _pieces_placed_this_player_turn += 1


def display_status_text(message):
    status_color_wrap = "{}{}{}".format(YELLOW, message, END)
    print(status_color_wrap)

def scroll_screen():
    for _ in range(500):
        print()

def lock_game_state():

    #scroll_screen()
    display_grid(grid)
    display_status_text("{}'s WIN!".format(current_player_turn(turn_switch)))

    exit(0)

def powerup_logic(alpha_val, numeral_val, powerup_type, activating_piece, _grid):
    # Powerup type: /
    print("powerup type val:", powerup_type)
    if powerup_type == pieces[3]:
        print("alpha:{} num:{} powerup:{}".format(alpha_val,numeral_val,powerup_type))

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


