from random import randint
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
def print_board(board):
    for row in board:
        print " ".join(row)
#create 2 variables to store ship's location
def random_row(board):
    return randint(0,len(board)-1)
def random_col(board):
    return randint(0,len(board[0])-1)

ship_row = random_row(board)
ship_col = random_col(board)

print ship_row
print ship_col
