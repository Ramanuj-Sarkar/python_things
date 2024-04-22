# Originally created by Aprataksh
# Changes: global variables gone
# Future changes: variable length, better functions, better variable names


# Importing packages
import random
import os


# Printing the Minesweeper Layout
def print_mines_layout(mine_values, n):
    print()
    print("\t\t\tMINESWEEPER\n")

    st = "   "
    for i in range(n):
        st = st + "     " + str(i + 1)
    print(st)

    for r in range(n):
        st = "     "
        if r == 0:
            for col in range(n):
                st = st + "______"
            print(st)

        st = "     "
        for col in range(n):
            st = st + "|     "
        print(st + "|")

        st = "  " + str(r + 1) + "  "
        for col in range(n):
            st = st + "|  " + str(mine_values[r][col]) + "  "
        print(st + "|")

        st = "     "
        for col in range(n):
            st = st + "|_____"
        print(st + '|')

    print()


# Function for setting up Mines
def set_mines(numbers, mines_no, n):
    # Track of number of mines already set up
    count = 0
    while count < mines_no:

        # Random number from all possible grid positions
        val = random.randint(0, n * n - 1)

        # Generating row and column from the number
        r = val // n
        col = val % n

        # Place the mine, if it doesn't already have one
        if numbers[r][col] != -1:
            count = count + 1
            numbers[r][col] = -1


# Function for setting up the other grid values
def set_values(numbers, n):
    # Loop for counting each cell value
    for r in range(n):
        for col in range(n):

            # Skip, if it contains a mine
            if numbers[r][col] == -1:
                continue

            # Check up
            if r > 0 and numbers[r - 1][col] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check down
            if r < n - 1 and numbers[r + 1][col] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check left
            if col > 0 and numbers[r][col - 1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check right
            if col < n - 1 and numbers[r][col + 1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check top-left
            if r > 0 and col > 0 and numbers[r - 1][col - 1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check top-right
            if r > 0 and col < n - 1 and numbers[r - 1][col + 1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check below-left
            if r < n - 1 and col > 0 and numbers[r + 1][col - 1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check below-right
            if r < n - 1 and col < n - 1 and numbers[r + 1][col + 1] == -1:
                numbers[r][col] = numbers[r][col] + 1


# Recursive function to display all zero-valued neighbours
def neighbours(mine_values, numbers, vis, n, r, col):

    # If the cell already not visited
    if [r, col] not in vis:

        # Mark the cell visited
        vis.append([r, col])

        # If the cell is zero-valued
        if numbers[r][col] == 0:

            # Display it to the user
            mine_values[r][col] = numbers[r][col]

            # Recursive calls for the neighbouring cells
            if r > 0:
                neighbours(mine_values, numbers, vis, n, r - 1, col)
            if r < n - 1:
                neighbours(mine_values, numbers, vis, n, r + 1, col)
            if col > 0:
                neighbours(mine_values, numbers, vis, n, r, col - 1)
            if col < n - 1:
                neighbours(mine_values, numbers, vis, n, r, col + 1)
            if r > 0 and col > 0:
                neighbours(mine_values, numbers, vis, n, r - 1, col - 1)
            if r > 0 and col < n - 1:
                neighbours(mine_values, numbers, vis, n, r - 1, col + 1)
            if r < n - 1 and col > 0:
                neighbours(mine_values, numbers, vis, n, r + 1, col - 1)
            if r < n - 1 and col < n - 1:
                neighbours(mine_values, numbers, vis, n, r + 1, col + 1)

        # If the cell is not zero-valued
        if numbers[r][col] != 0:
            mine_values[r][col] = numbers[r][col]


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
    if count == n * n - mines_no:
        return True
    else:
        return False


# Display all the mine locations
def show_mines(mine_values, numbers, n):
    for r in range(n):
        for col in range(n):
            if numbers[r][col] == -1:
                mine_values[r][col] = 'M'


if __name__ == "__main__":

    # Size of grid
    actual_n = 8
    # xlimit = 8
    # ylimit = 8

    # Number of mines
    actual_mines_no = 2

    # The actual values of the grid
    actual_numbers = [[0 for y in range(actual_n)] for x in range(actual_n)]
    # The apparent values of the grid
    actual_mine_values = [[' ' for y in range(actual_n)] for x in range(actual_n)]
    # The positions that have been flagged
    flags = []

    # Set the mines
    set_mines(actual_numbers, actual_mines_no, actual_n)

    # Set the values
    set_values(actual_numbers, actual_n)

    # Display the instructions
    instructions()

    # Variable for maintaining Game Loop
    game_running = True

    # The GAME LOOP
    while game_running:
        print_mines_layout(actual_mine_values, actual_n)

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
            if inp[2] != 'F' and inp[2] != 'f':
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
            if val[0] > actual_n or val[0] < 1 or val[1] > actual_n or val[1] < 1:
                clear()
                print("Wrong input!")
                instructions()
                continue

            # Get row and column numbers
            actual_r = val[0] - 1
            actual_col = val[1] - 1

            # If cell already been flagged
            if [actual_r, actual_col] in flags:
                clear()
                print("Flag already set")
                continue

            # If cell already been displayed
            if actual_mine_values[actual_r][actual_col] != ' ':
                clear()
                print("Value already known")
                continue

            # Check the number for flags
            if len(flags) < actual_mines_no:
                clear()
                print("Flag set")

                # Adding flag to the list
                flags.append([actual_r, actual_col])

                # Set the flag for display
                actual_mine_values[actual_r][actual_col] = 'F'
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
        if val[0] > actual_n or val[0] < 1 or val[1] > actual_n or val[1] < 1:
            clear()
            print("Wrong Input!")
            instructions()
            continue

        # Get row and column number
        actual_r = val[0] - 1
        actual_col = val[1] - 1

        # Unflag the cell if already flagged
        if [actual_r, actual_col] in flags:
            flags.remove([actual_r, actual_col])

        # If landing on a mine --- GAME OVER
        if actual_numbers[actual_r][actual_col] == -1:
            actual_mine_values[actual_r][actual_col] = 'M'
            show_mines(actual_mine_values, actual_numbers, actual_n)
            print_mines_layout(actual_mine_values, actual_n)
            print("Landed on a mine. GAME OVER!!!!!")
            game_running = False
            continue

        # If landing on a cell with 0 mines in neighboring cells
        elif actual_numbers[actual_r][actual_col] == 0:
            vis = []
            actual_mine_values[actual_r][actual_col] = '0'
            neighbours(actual_mine_values, actual_numbers, vis, actual_n, actual_r, actual_col)

        # If selecting a cell with at least 1 mine in neighboring cells
        else:
            actual_mine_values[actual_r][actual_col] = str(actual_numbers[actual_r][actual_col])

        # Check for game completion
        if (check_over(actual_mine_values, actual_mines_no, actual_n)):
            show_mines(actual_mine_values, actual_numbers, actual_n)
            print_mines_layout(actual_mine_values, actual_n)
            print("Congratulations!!! YOU WIN")
            game_running = False
            continue
        clear()
