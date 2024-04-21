# Determine which player has the "x" pieces.
# "x" pieces go first.
# Display game menu. 
# Game menu contents:
    # Num of rows/cols.
    # Powerups per turn.
    # Num of pieces placed per turn.
    # Default rulesets are displayed.
# Game procedure:
    # Players alternate turns after x's go first.
    # Players place their piece(s).
    # If player wins during turn break and show win screen.
# Display updated gameboard for every piece placed.
# Then, show game recap and "Play Again?" prompt.
# Powerup implementation.
    # Powerups have a grid position and an activation pattern
    # Individual types of powerups are subclasses of a baseclass Powerup that has members: grid position and activation pattern. Each powerup has its own pattern. The patterns are: "/", "\", "|", and "-"
    # Powerups determine their position pseudo-randomly. And, they check if there are spots available before they are placed. They check to see if they overlap other pieces or not before placed.
    # Powerups are triggered when a players places their piece ontop of it. Their pieces will not be destroyed, but the opposite type of pieces will be.
    # Optionally, the players can decide to enable a special rule that makes powerup activations destory both types of piecees and other powerups caught in the activation zone.
    # could add a red trail of the same powerup type along the path of the activation to visually show where the activation happened. This activation should be removed after next piece is placed. The smoke would also have to not hit a certain player as well. 
# Win condition implementation.
    # Win condition will be determined by each unit along (n,0) and (0,n) having the head of a linked list.
    # each node of the linked list will be called a "gridunit" which will have one function where it returns true if it is surround on both sides by another node, or is the last node n and has a node connected to it.
    # each node will have a function that checks if it is connected to the head of the list and if true game loop will break and show the type of it contains as winner.
    # This is a function called "circuitbreaker"
    # There will have to be 2n + 1 linked lists because there has to be two heads at (0,0) and (0,n)
    # Another complexity I just realized is that each node has to be be able to detect if its along either of the horizontal axes and also do the check for those too.
    # One particular node has to be responsible for 3 similultaneous circuit breaker connections at the same time. (The middle one, obviously)
    # Though this really shouldn't be a problem its just three checks per gridunit. And it only has to be computed by the gridunits that are on the horizontal axes.
