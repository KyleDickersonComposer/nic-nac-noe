import lib
import main

while True:
    # Num of rows/cols.
    #get n
    try:
        n = int(input("Enter the number of rows and columns desired. Must be a value between 3-52\n"))
    except:
        continue
    if 3 <= n <= 53:
        print()
        break

    #debug logic
    if main.debug == False:
        # ANSI code to clear the screen.
        print('\033[H\033[J')
        lib.scroll_screen()


    #display first screen
    lib.display_grid(main.grid, main.n, main.alphabet)

    lib.display_status_text(main.status_message)

    status_message = ""

    while True:
        #check piece location input
        valid_alpha_chars = main.alphabet[:n]
        hud_text = "{}'s turn. Xs placed: {}. Os placed: {}. \n".format(lib.current_player_turn(main.turn_switch, main.pieces), main.xs_placed, main.os_placed)
        location = input(hud_text)
        location = location.split()
        l_len = len(location)
        if l_len < 2:
            status_message = "Not enough arguments. For example: A 1"
            lib.display_grid(main.grid, main.n, main.alphabet)
            lib.display_status_text(status_message)
            continue
        elif l_len > 2:
            status_message = "Too many arguments. For example: A 1"
            lib.display_grid(main.grid, main.n, main.alphabet)
            lib.display_status_text(status_message)
            continue

        alpha_val = location[0]
        numeral_val = location[1]

        if not alpha_val in valid_alpha_chars:
            status_message = "Not a valid alpha input. For example: A 1"
            lib.display_grid(main.grid, main.n, main.alphabet)
            lib.display_status_text(status_message)
            continue

        try:
            numeral_val = int (numeral_val)
        except:
            status_message = "the second value should be a number. For example: A 1"
            lib.display_grid(main.grid, main.n, main.alphabet)
            lib.display_status_text(status_message)
            continue
        
        if  numeral_val < 1 or numeral_val > n:
            status_message = "Number should be between 1 and {}. val: {}.".format(n, numeral_val)
            lib.display_grid(main.grid, main.n, main.alphabet)
            lib.display_status_text(status_message)
            continue

        #check for X's and O's overlapping each other
        if main.grid[main.alphabet.index(alpha_val)][numeral_val-1] == main.pieces[1] or main.grid[main.alphabet.index(alpha_val)][numeral_val-1] == main.pieces[2]:
            lib.display_grid(main.grid, main.n, main.alphabet)
            lib.display_status_text(status_message)
            continue
        else:   
            grid = lib.modify_grid(main.alphabet.index(alpha_val), numeral_val, lib.current_player_turn(main.turn_switch, main.pieces), main.grid, main.xs_placed, main.os_placed, main.pieces, main.n, main.alphabet)
            status_message = ""
            break

    #game logic
    lib.win_check(main.grid,main.turn_switch, main.n, main.pieces, main.alphabet)
    print(main.pieces_placed_on_this_player_turn, "placed", main.pieces_per_turn, "placements per turn")
    if main.pieces_placed_on_this_player_turn >= main.pieces_per_turn:
        lib.alternate_turns(main.turn_switch, main.pieces)
        grid = lib.ugly_powerup_placement_checks(main.grid, main.n, main.pieces,main.xs_placed, main.os_placed, main.alphabet)

