# In this project I'll build one-player version of the classic board game Battleship!
# there will be a single ship hidden in a random location on a 5x5 grid.
# The player will have 10 guesses to try to sink the ship.

# Step1 Create a variable board and set it equal to an empty list.
board= []

#Create a 5 x 5 grid initialized to all '*'s and store it in board.
for i in range(5):
    board.append(["*"]* 5)
#define a function to print the board and getting rid of those
#quote marks and commas using ".join"
def print_board(board_in):
    for row in board:
        print " ".join(row)
