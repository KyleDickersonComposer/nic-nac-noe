import lib 

debug_mode = False

lib.clear_screen()

while True:
    try:
        n = int(input("Enter desired board size: "))
    except:
        continue

    if 3 <= n <= 53:
        break

game_state = lib.GameState(n)

while True:
    while True:
        #If debug mode is true print debug statements will be hidden.
        if debug_mode == False:
            # ANSI code to clear the screen.
            lib.clear_screen()

        if game_state.status_message != "":
            lib.display_status_text(game_state.status_message)

        hud_text = "{}'s turn. Xs placed: {}. Os placed: {}. \n".format(game_state.current_player_turn(), game_state.xs_placed, game_state.os_placed)

        lib.display_grid(game_state.grid, game_state.n, game_state.alphabet)

        prompt_result = lib.get_input(hud_text)
        is_valid = lib.valid_input(prompt_result, game_state.alphabet, game_state.n, game_state)
        if is_valid:
            player_input = lib.clean_input(prompt_result, game_state.alphabet)
        else:
            continue

        check = lib.overlap_check(player_input, game_state, game_state.pieces, game_state.grid, game_state.current_player_turn())
        print(check)
        
        if check == True:
            if lib.piece_is_powerup(player_input, game_state.alphabet, game_state.grid) == True:
                lib.powerup_activation_logic(player_input, game_state.grid[player_input[0]][player_input[1]], game_state.pieces, game_state.n)  

            grid = lib.modify_grid(player_input, game_state.current_player_turn(), game_state.grid, game_state.pieces, game_state)
            game_state.pieces_placed_on_this_player_turn += 1

            lib.display_grid(game_state.grid, game_state.n, game_state.alphabet)

        elif check == False:
            continue

        lib.win_check(game_state.grid, game_state.n, game_state.current_player_turn(), game_state.alphabet)

        #Game logic for after placement of a piece.
        #If you have placed all the pieces for your turn, then handle next turn.
        if game_state.pieces_placed_on_this_player_turn == game_state.pieces_to_place_for_each_player_turn:
            game_state.alternate_player_turn(game_state)

            while True:
                #May have to add check for if pieces x, so that powerups are placed once per 2 player turns. Then, spawn powerup if too many powerups.
                try_coords = lib.get_powerup_coords(game_state.n)
                is_valid = lib.validate_powerup_placement(try_coords, game_state.pieces, game_state.grid, game_state.sublist, game_state.n) 
                if is_valid == True:
                    grid = lib.modify_grid(try_coords, lib.get_random_powerup(game_state.pieces), game_state.grid, game_state.pieces, game_state)
                    break
                else:
                    continue
