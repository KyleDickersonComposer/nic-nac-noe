import lib 


debug = False

n = lib.get_n_val()

grid = lib.get_grid(n)

#debug logic
if debug == False:
    # ANSI code to clear the screen.
    print('\033[H\033[J')
    lib.scroll_screen()

while True:
    hud_text = "{}'s turn. Xs placed: {}. Os placed: {}. \n".format(lib.current_player_turn(), lib.get_xs_placed(), lib.get_os_placed())
    prompt_result = lib.get_input(hud_text)
    if lib.valid_input(prompt_result) == True:
        grid = lib.modify_grid(prompt_result, lib.current_player_turn(), grid)
        break
    elif lib.valid_input(prompt_result) == False:
        continue

#game logic
#dont know about this one:
#lib.win_check(main.grid, main.turn_switch)

