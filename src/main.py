import math
import random
import lib 
import gameloop

debug = False


#remove comment to enable.
#debug = debug_mode_toggle(debug)

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
pieces_per_turn = 1

# Nested loop comprehension to create the 2D matrix for the grid.
grid = [[pieces[0] for _ in range(n)] for _ in range(n)]

# Display the grid.

# Spacing for x axis names.
# Values for x axis names.
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Print x axis names per grid unit.

turn_switch = False
status_message = ""

