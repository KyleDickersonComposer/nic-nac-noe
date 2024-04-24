while True:
    # Num of rows/cols.
    try:
        n = int(input("Enter the number of rows and columns desired. Must be a value between 3-52\n"))
    except:
        continue
    if 3 <= n <= 53:
        print()
        break

    if debug == False:
        # ANSI code to clear the screen.
        print('\033[H\033[J')
        lib.scroll_screen()

    lib.display_grid(grid)

    lib.display_status_text(status_message)

    status_message = ""

    while True:
        valid_alpha_chars = alphabet[:n]
        hud_text = "{}'s turn. Xs placed: {}. Os placed: {}. \n".format(lib.current_player_turn(turn_switch), xs_placed, os_placed)
        location = input(hud_text)

        location = location.split()

        l_len = len(location)

        if l_len < 2:
            status_message = "Not enough arguments. For example: A 1"
            lib.display_grid(grid)
            lib.display_status_text(status_message)
            continue
        elif l_len > 2:
            status_message = "Too many arguments. For example: A 1"
            lib.display_grid(grid)
            lib.display_status_text(status_message)
            continue

        alpha_val = location[0]
        numeral_val = location[1]

        if not alpha_val in valid_alpha_chars:
            status_message = "Not a valid alpha input. For example: A 1"
            lib.display_grid(grid)
            lib.display_status_text(status_message)
            continue

        try:
            numeral_val = int (numeral_val)
        except:
            status_message = "the second value should be a number. For example: A 1"
            lib.display_grid(grid)
            lib.display_status_text(status_message)
            continue
        
        if  numeral_val < 1 or numeral_val > n:
            status_message = "Number should be between 1 and {}. val: {}.".format(n, numeral_val)
            lib.display_grid(grid)
            lib.display_status_text(status_message)
            continue

        if grid[alphabet.index(alpha_val)][numeral_val-1] == pieces[1] or grid[alphabet.index(alpha_val)][numeral_val-1] == pieces[2]:
            lib.display_grid(grid)
            lib.display_status_text(status_message)
            continue
        else:   
            grid = lib.modify_grid(alphabet.index(alpha_val), numeral_val, lib.current_player_turn(turn_switch), grid, xs_placed, os_placed)
            status_message = ""
            break

    lib.win_check()

    print(pieces_placed_on_this_player_turn, "placed", pieces_per_turn, "placements per turn")
    if pieces_placed_on_this_player_turn >= pieces_per_turn:
        lib.alternate_turns(turn_switch)
        grid = ugly_powerup_placement_checks(grid)
