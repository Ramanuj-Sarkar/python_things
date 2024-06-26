'''
Originally created by Aprataksh

Changes
global variables gone
print has less changing state
set_mines grows O(mines) and is more consistent
set_values grows O(mines)
1,1 never has a mine
boards of 10 or larger are okay (boards larger than 1000 really won't be)
repeated stuff is taken away

Future changes
different row and column?
variable length
better functions
better variable names

Needs special coaxing on Mac
You have to change some variable or it won't clear the screen between turns
You can just use Spyder in Anaconda, it works there for some reason
'''

# Importing packages
import random
import os


# Printing the Minesweeper Layout
def print_mines_layout(mine_val, n):
    print("\n\t\t\tMINESWEEPER\n")
    
    pad = len(str(n)) - 1

    # row with Numbers
    bookend = [" " * (6 - len(str(i))) + str(i + 1) for i in range(n)]
    print(" " * (3 + pad) + ''.join(bookend))

    # Top of Minesweeper Box
    print(" " * (6 + pad) + "______" * n)

    for r in range(n):
        # Beginning part without number
        st = ' ' * (5 + pad)
        strr = str(r + 1)

        # Beginning part with number
        number_st = " " * (3 + pad - len(strr)) + strr + " " * 2

        # Middle part with mine / no mine indicator
        middles = ''.join(["|  " + str(mine_val[r][col]) + "  " for col in range(n)])

        print(st + "|     " * n + "|")

        print(number_st + middles + "|")

        print(st + "|_____" * n + '|')

    print(" " * (3 + pad) + ''.join(bookend) + '\n')


# Function for setting up mines
def set_mines(numbers, minelist, n):
    for pos in minelist:
        # Generating row and column from the position
        r = pos // n
        col = pos % n

        # set the mine to -1
        numbers[r][col] = -1


# Function for setting up the other grid values
def set_values(numbers, minelist, n):
    # Loop for counting each cell value
    for pos in minelist:
        # generate row and column from position
        r = pos // n
        col = pos % n
        
        if r > 0:
            # add to top
            numbers[r-1][col] = numbers[r-1][col] + 1
            if col > 0:
                # add to top left
                numbers[r-1][col-1] = numbers[r-1][col-1] + 1
            if col < n-1:
                # add to top right
                numbers[r-1][col+1] = numbers[r-1][col+1] + 1
        
        if r < n - 1:
            # add to bottom
            numbers[r+1][col] = numbers[r+1][col] + 1
            if col > 0:
                # add to bottom left
                numbers[r+1][col-1] = numbers[r+1][col-1] + 1
            if col < n-1:
                # add to bottom right
                numbers[r+1][col+1] = numbers[r+1][col+1] + 1
        
        if col > 0:
            # add to left
            numbers[r][col-1] = numbers[r][col-1] + 1
        if col < n-1:
            # add to right
            numbers[r][col+1] = numbers[r][col+1] + 1
    
    # set the mine to -1
    set_mines(numbers, minelist, n)
        
        


# Recursive function to display all zero-valued neighbours
def neighbours(mine_values, numbers, vis, n, r, col):

    # If the cell already not visited
    if [r, col] not in vis:

        # Mark the cell visited
        vis.append([r, col])

        # If the cell is not zero-valued
        if numbers[r][col] != 0:
            mine_values[r][col] = numbers[r][col]
        else: # If the cell is zero-valued

            # Display it to the user
            mine_values[r][col] = numbers[r][col]

            # Recursive calls for the neighbouring cells
            if r > 0:
                neighbours(mine_values, numbers, vis, n, r - 1, col)
                if col > 0:
                    neighbours(mine_values, numbers, vis, n, r - 1, col - 1)
                if col < n - 1:
                    neighbours(mine_values, numbers, vis, n, r - 1, col + 1)
                
            if r < n - 1:
                neighbours(mine_values, numbers, vis, n, r + 1, col)
                if col > 0:
                    neighbours(mine_values, numbers, vis, n, r + 1, col - 1)
                if col < n - 1:
                    neighbours(mine_values, numbers, vis, n, r + 1, col + 1)
                
            if col > 0:
                neighbours(mine_values, numbers, vis, n, r, col - 1)
            if col < n - 1:
                neighbours(mine_values, numbers, vis, n, r, col + 1)


# Function for clearing the terminal
def clear():
    os.system("clear")


# Function to display the instructions
def instructions():
    print("Instructions:")
    print("1. Enter row and column number to select a cell, Example \"2 3\"")
    print("2. In order to flag a mine, enter F after row and column numbers, Example \"2 3 F\"")


# Function to check for completion of the game
def check_over(mine_values, mines_no, n):
    # Count of all numbered values
    count = 0

    # Loop for checking each cell in the grid
    for r in range(n):
        for col in range(n):

            # If cell not empty or flagged
            if mine_values[r][col] != ' ' and mine_values[r][col] != 'F':
                count = count + 1

    # Count comparison
    return count == n * n - mines_no


# Display all the mine locations
def show_mines(mine_values, numbers, n):
    for r in range(n):
        for col in range(n):
            if numbers[r][col] == -1:
                mine_values[r][col] = 'M'


def main():
    # Size of grid
    n = 9
    # xlimit = 8
    # ylimit = 8

    # Number of mines
    mines_no = 4

    # The actual values of the grid
    numbers = [[0 for y in range(n)] for x in range(n)]
    # The apparent values of the grid
    apparent = [[' ' for y in range(n)] for x in range(n)]
    # The positions that have been flagged
    flags = []
    
    # creates list of positions for mines
    # they can't be in the top left corner
    mines_list = random.sample(range(1, n * n - 1), mines_no)

    # Set the values
    set_values(numbers, mines_list, n)

    # Display the instructions
    instructions()

    # Variable for maintaining Game Loop
    game_running = True

    # The GAME LOOP
    while game_running:
        print_mines_layout(apparent, n)

        # Input from the user
        inp = input("Enter row number followed by space and column number = ").split()

        # Standard input
        if len(inp) == 2:

            # Try block to handle errant input
            try:
                val = list(map(int, inp))
            except ValueError:
                clear()
                print("Wrong input!")
                instructions()
                continue

        # Flag input
        elif len(inp) == 3:
            if inp[2].upper() != 'F':
                clear()
                print("Wrong Input!")
                instructions()
                continue

            # Try block to handle errant input
            try:
                val = list(map(int, inp[:2]))
            except ValueError:
                clear()
                print("Wrong input!")
                instructions()
                continue

            # Sanity checks
            if val[0] > n or val[0] < 1 or val[1] > n or val[1] < 1:
                clear()
                print("Wrong input!")
                instructions()
                continue

            # Get row and column numbers
            r = val[0] - 1
            col = val[1] - 1

            # If cell already been flagged
            if [r, col] in flags:
                clear()
                print("Flag already set")
                continue

            # If cell already been displayed
            if apparent[r][col] != ' ':
                clear()
                print("Value already known")
                continue

            # Check the number for flags
            if len(flags) < mines_no:
                clear()
                print("Flag set")

                # Adding flag to the list
                flags.append([r, col])

                # Set the flag for display
                apparent[r][col] = 'F'
                continue
            else:
                clear()
                print("Flags finished")
                continue

        else:
            clear()
            print("Wrong input!")
            instructions()
            continue

        # Sanity checks
        if val[0] > n or val[0] < 1 or val[1] > n or val[1] < 1:
            clear()
            print("Wrong Input!")
            instructions()
            continue

        # Get row and column number
        r = val[0] - 1
        col = val[1] - 1

        # Unflag the cell if already flagged
        if [r, col] in flags:
            flags.remove([r, col])

        # If landing on a mine --- GAME OVER
        if numbers[r][col] == -1:
            show_mines(apparent, numbers, n)
            print_mines_layout(apparent, n)
            print("Landed on a mine. GAME OVER!!!!!")
            game_running = False
            continue

        # If landing on a cell with 0 mines in neighboring cells
        elif numbers[r][col] == 0:
            vis = []
            neighbours(apparent, numbers, vis, n, r, col)

        # If selecting a cell with at least 1 mine in neighboring cells
        else:
            apparent[r][col] = str(numbers[r][col])

        # Check for game completion
        if (check_over(apparent, mines_no, n)):
            clear()
            show_mines(apparent, numbers, n)
            print_mines_layout(apparent, n)
            print("Congratulations!!! YOU WIN")
            game_running = False
            continue
        clear()

if __name__ == "__main__":
    main()

# fin
