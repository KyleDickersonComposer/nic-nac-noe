import lib

debug_mode = False

lib.clear_screen()

while True:
    try:
        n = int(input("Enter a whole number between 4 and 52 to determine grid size. "))

        if lib.validate_n(n, "The number must be between 4 and 52"):
            lib.clear_screen()
            break
    except ValueError:
        lib.clear_screen()
        continue

game_state = lib.GameState(n)

lib.display_in_gameloop(game_state)

while True:
    # If debug mode is true print debug statements will be hidden.
    if not debug_mode:
        # ANSI code to clear the screen.
        lib.clear_screen()

    lib.display_in_gameloop(game_state)

    last_grid_state = [row[:] for row in game_state.grid]

    hud_text = "{}'s turn. Xs placed: {}. Os placed: {}. \n".format(
        game_state.current_player_turn(), game_state.xs_placed, game_state.os_placed
    )

    prompt_result = lib.get_input_coords(hud_text)

    is_valid = lib.valid_input(
        prompt_result, game_state.alphabet, game_state.n, game_state
    )

    if is_valid:
        player_input = lib.clean_input(prompt_result, game_state.alphabet)

        check = lib.overlap_check(player_input, game_state, game_state.grid)
        if check:
            game_state.grid = lib.modify_grid(
                player_input,
                game_state.current_player_turn(),
                game_state.grid,
                game_state,
            )
            lib.win_check(game_state)
            game_state.pieces_placed_on_this_player_turn += 1

            if lib.piece_is_powerup(
                player_input, last_grid_state, game_state.set_of_powerups
            ):
                powerup_this_turn = lib.get_random_powerup(game_state.set_of_powerups)
                lib.powerup_activation_logic(
                    player_input,
                    last_grid_state[player_input[0]][player_input[1]],
                    game_state.n,
                    game_state,
                )

            if (
                game_state.pieces_placed_on_this_player_turn
                == game_state.pieces_to_place_for_each_player_turn
            ):
                while True:
                    # Place a piece
                    try_coords = lib.get_random_powerup_coords(game_state.n)

                    # broken Coords dont overwrite a X or Y
                    is_valid = lib.validate_powerup_placement(
                        try_coords,
                        game_state.grid,
                        game_state.sub_set_of_replacedable_pieces,
                        game_state.n,
                    )

                    if is_valid:
                        powerup_this_turn = lib.get_random_powerup(
                            game_state.set_of_powerups
                        )

                        if (
                            game_state.pieces_placed_on_this_player_turn
                            == game_state.pieces_to_place_for_each_player_turn
                        ):
                            game_state.grid = lib.modify_grid(
                                try_coords,
                                powerup_this_turn,
                                game_state.grid,
                                game_state,
                            )
                            last_grid_state = game_state.grid
                            game_state.alternate_player_turn(game_state)
                            break

    lib.draw_check(game_state)
    lib.display_in_gameloop(game_state)
