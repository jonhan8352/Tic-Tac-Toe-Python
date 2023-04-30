from termcolor import colored

# Define the Tic Tac Toe grid
grid = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Function to print the Tic Tac Toe grid
def print_grid():
    for i in range(3):
        row = ""
        for j in range(3):
            if j == 0:
                row += " " + grid[i][j] + " |"
            elif j == 2:
                row += " " + grid[i][j] + " "
            else:
                row += " " + grid[i][j] + " |"
        print(row)
        if i != 2:
            print("-----------")

# Function to check if a player has won
def check_win(player):
    # Check rows
    for i in range(3):
        if grid[i][0] == player and grid[i][1] == player and grid[i][2] == player:
            return True
    # Check columns
    for j in range(3):
        if grid[0][j] == player and grid[1][j] == player and grid[2][j] == player:
            return True
    # Check diagonals
    if grid[0][0] == player and grid[1][1] == player and grid[2][2] == player:
        return True
    if grid[0][2] == player and grid[1][1] == player and grid[2][0] == player:
        return True
    return False

# Function to play a turn
def play_turn(player):
    # Get player input
    print(colored("Player " + player + "'s turn", 'green'))
    row = int(input("Enter row (1-3): ")) - 1
    col = int(input("Enter column (1-3): ")) - 1
    # Check if the space is available
    if grid[row][col] != " ":
        print(colored("That space is already taken, try again", 'red'))
        play_turn(player)
    else:
        grid[row][col] = player
        print_grid()
        # Check for win
        if check_win(player):
            print(colored("Player " + player + " wins!", 'green'))
            return
        # Check for tie
        if " " not in grid[0] and " " not in grid[1] and " " not in grid[2]:
            print(colored("It's a tie!", 'yellow'))
            return
        # Switch players
        if player == "X":
            play_turn("O")
        else:
            play_turn("X")

# Start the game
print(colored("Let's play Tic Tac Toe!", 'blue'))
print_grid()
play_turn("X")
