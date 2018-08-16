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
print_board(board)
#create 2 variables to store ship's location
def random_row(board):
    return randint(0,len(board)-1)
def random_col(board):
    return randint(0,len(board[0])-1)

ship_row = random_row(board)
ship_col = random_col(board)

print ship_row
print ship_col
#create for loop to allow the player to make up to 5 guesses
for turn in range(2):
    print "Turn{}".format(turn +1)
#the code to allow the player to guess where it is:
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))
# add conditions to check if guess_row/col equals to ship_row/col
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sank the battleship!"
        board[guess_row][guess_col]= "$"
        print_board(board)
        break
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print "that's not in the ocean"
        elif board[guess_row][guess_col] == "X":
            print "you already guessed that one."
        else:
            print "you missed the battleship"
            board[guess_row][guess_col] = "X"
        if turn == 2:
            print "Game OVER"
            board[ship_row][ship_col]= "$"
        print_board(board)
        
        
