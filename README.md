# Tic-Tac-Toe-Python
The termcolor module is used to colorize the output, so make sure to install it by running <i>pip install termcolor</i> in your terminal before running the game.
```
pip install termcolor
```
After we install termcolor module. Now we must import colored from termcolor module at the beginning of our Python code.
```
from termcolor import colored
```
Then we start coding the Tic Tac Toe grid.
```
# Define the Tic Tac Toe grid
grid = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
```
Following on create funtion to print Tic Tac Toe grid.
```
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
```
Now, we need to create a function to check if a player has won.
```
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
```
Then we also need to create a function to allow player to play for a turn.
```
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
```
Finally, we need to call out for the game to start.
```
print(colored("Let's play Tic Tac Toe!", 'blue'))
print_grid()
play_turn("X")
```
