# This is based on the language on this page:
# https://esolangs.org/wiki/2Deadfish
def run_2deadfish(code_string: str, file_name=False, starting_input=0):
    # This is the code itself.
    code = []

    # This debug string prints the equivalent code in Deadfish
    debug_string = ''

    # You can use text files
    # Newline characters don't affect anything
    # Therefore, the code is different when using or not using a text file
    if file_name:
        with open(code_string, 'r') as file:
            code = file.readlines()
    else:
        code = code_string.split('\n')

    # This makes sure you can still go down
    # when one line is shorter than all the rest
    max_line = max([len(line) for line in code])

    pointer = (0, 0)

    # This is incremented / decremented / squared.
    counter = starting_input

    # The direction is equal to direction * 90 degrees counterclockwise from right.
    direction = 0
    while -1 < pointer[0] < len(code) and -1 < pointer[1] < max_line:
        row = pointer[0]
        column = pointer[1]

        if counter == 256 or counter == -1:
            counter = 0

        if column < len(code[row]) and code[row][column] in 'diso':
            instruction = code[row][column]
            debug_string += instruction

            if instruction == 'o':
                print(counter)
            elif instruction == 'i':  # clockwise / right
                counter += 1
                direction += 1
            elif instruction == 's':  # backwards
                counter **= 2
                direction += 2
            elif instruction == 'd':  # counterclockwise / left
                counter -= 1
                direction -= 1

        # 4 * 90 = 360 degrees = 0 degrees
        direction %= 4

        if direction == 0:  # east
            pointer = (row, column + 1)
        elif direction == 1:  # south
            pointer = (row + 1, column)
        elif direction == 2:  # west
            pointer = (row, column - 1)
        elif direction == 3:  # north
            pointer = (row - 1, column)

    return counter


def print_730263108188381677183711651244095019(seconds=True, hours_days=True, aeons=True):
    """
    original = 730263108188381677183711651244095019
    # original = approx2 ** 2 + 184492320800793883
    approx2 = 854554333081508444
    # approx2 = approx4 ** 2 + 1781984203
    approx4 = 924421079
    # approx4 = approx8 ** 2 + 17863
    approx8 = 30404
    # approx8 = approx16 ** 2 + 128
    approx16 = 174
    # approx16 = 13 ** 2 + 5
    approx32 = 13

    seconds: returns
    """

    # reaches 174, squares it, and continues adding
    lines = ('  i i   \n'
             'ii i i  \n'
             ' s   isi\n'
             'iiiidd i').split('\n')

    # continues adding, with the goal of reaching 30406
    lines[0] += '  ' * 16
    lines[1] += 'i ' * 16
    lines[2] += ' i' * 16
    lines[3] += 'ii' * 16

    # reaches 30404, squares it, and continues adding
    # the value at the end is 924403224
    lines[0] += '  ii  '
    lines[1] += 'isddi '
    lines[2] += 'd di i'
    lines[3] += '   iii'

    # continues adding, with the goal of 924421072
    lines[0] += '  ' * 2231
    lines[1] += 'i ' * 2231
    lines[2] += ' i' * 2231
    lines[3] += 'ii' * 2231

    # reaches 924421079, squares it, and continues adding
    # the value at the end is 854554331299524240
    lines[0] += ' s'
    lines[1] += 'id'
    lines[2] += ' i'
    lines[3] += 'ii'

    if seconds:
        print(run_2deadfish('\n'.join(lines)))
        return 0
    elif not hours_days and not aeons:
        print("Why did you do this?")
        return 0

    # continues adding, with the goal of reaching 854554333081508440
    # running this would take hours, if not days
    lines[0] += '  ' * 222748025
    lines[1] += 'i ' * 222748025
    lines[2] += ' i' * 222748025
    lines[3] += 'ii' * 222748025

    # reaches 854554333081508444, squares it, and continues adding
    # the value at the end of this part is 730263108188381676999219330443301146
    # the file is at least 1.78 GB in size at this point
    lines[0] += 'iii i  '
    lines[1] += 'd isdi '
    lines[2] += 'i d i i'
    lines[3] += 'ii  iii'

    if hours_days:
        print(run_2deadfish('\n'.join(lines)))
        return 0
    else:
        print("This might result in a memory error.\n"
              "Even if it doesn't, it will take aeons.")

    # if I run it with this number, it results in a memory error
    biggest_addition = 23061540100099234

    # continues adding and finally reaches 730263108188381677183711651244095019
    # this would take tens, if not millions, of years
    lines[0] += '  ' * biggest_addition + ' '
    lines[1] += 'i ' * biggest_addition + 'i'
    lines[2] += ' i' * biggest_addition + 'o'
    lines[3] += 'ii' * biggest_addition + ' '

    print(run_2deadfish('\n'.join(lines)))
    return 0


if __name__ == '__main__':
    # change the boolean values accordingly
    print_730263108188381677183711651244095019(seconds=True, hours_days=False, aeons=False)
