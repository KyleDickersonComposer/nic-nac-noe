import lib 
import math

debug = False


#remove comment to enable.
#debug = lib.debug_mode_toggle(debug)

# TODO Grid Display
# ANSI escape codes for text colors

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PINK = "\x1b[38;5;205m"
CYAN = "\x1b[36m"
END = "\033[0m"  # Reset color to default

n = 0 

xs_placed = 0

os_placed = 0 

pieces = [" . ", " X ", " O ", YELLOW + " / " + END, BLUE + " \\ " + END, PINK + " | " + END, CYAN + " - " + END]

pieces_placed_on_this_player_turn = 0
    
#pieces_per_turn = math.floor(math.log(n**2,3))
#disable this to re-enable mutliplacement ability.
pieces_per_turn = 1

# Nested loop comprehension to create the 2D matrix for the grid.
grid = [[pieces[0] for _ in range(n)] for _ in range(n)]

# Values for x axis names.
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Print x axis names per grid unit.

turn_switch = False
status_message = ""

#debug logic
if debug == False:
    # ANSI code to clear the screen.
    print('\033[H\033[J')
    lib.scroll_screen()
# Num of rows/cols.


#get n

while True:
    hud_text = "{}'s turn. Xs placed: {}. Os placed: {}. \n".format(lib.current_player_turn(turn_switch), xs_placed, os_placed)
    prompt_result = lib.get_input(hud_text)
    if lib.valid_input(prompt_result) == True:
        grid = lib.modify_grid(prompt_result, lib.current_player_turn(turn_switch), grid)
        break
    elif lib.valid_input(prompt_result) == False:
        continue

#game logic
#dont know about this one:
#lib.win_check(main.grid, main.turn_switch)

