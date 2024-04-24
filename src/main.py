import lib 

debug_mode = True

# ANSI code to clear the screen.
lib.clear_screen()

while True:

    n = lib.init_n_val()
    if n == False:
        continue
    else:
        lib.set_n_val(n)
        break

grid = lib.get_grid(lib.get_n_val())


while True:
    while True:

        #If debug mode is true print debug statements will be hidden.
        if debug_mode == False:
            # ANSI code to clear the screen.
            lib.clear_screen()
        else: 
            print(grid)
            print("n =",n)


        if lib.get_status_message() != "":
            lib.display_status_text(lib.get_status_message())

        hud_text = "{}'s turn. Xs placed: {}. Os placed: {}. \n".format(lib.current_player_turn(), lib.get_xs_placed(), lib.get_os_placed())

        lib.display_grid(grid)
        prompt_result = lib.get_input(hud_text)
        validation_result = lib.valid_input(prompt_result)

        if validation_result == True:
            grid = lib.modify_grid(prompt_result, lib.current_player_turn(), grid)
            lib.iterate_pieces_placed_on_this_player_turn()
            lib.display_grid(grid)
        elif validation_result == False:
            continue

        lib.win_check(grid)

        if lib.get_pieces_placed_on_this_player_turn() >= lib.get_pieces_per_player_turn(lib.get_n_val()):
            print("alternate turns")
            lib.alternate_player_turn()
