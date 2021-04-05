# One can play:
# rock-paper-scissors
# rock-paper-scissors-lizard-spock
# rock-paper-fire-water-scissors
# using this program.

from random import randint


def make_choice(choice):
    if choice == '1':
        moves = ['rock', 'paper', 'scissors']
        return (moves,
                (lambda x,y: x == moves[y-2]),
                (lambda x,y: x == moves[y-1]))
    elif choice == '2':
        moves = ['rock', 'paper', 'scissors', 'spock', 'lizard']
        return (moves,
                (lambda x,y: x == moves[y-4] or x == moves[y-2]),
                (lambda x,y: x == moves[y-3] or x == moves[y-1]))
    elif choice == '3':
        moves = ['rock', 'paper', 'fire', 'water', 'scissors']
        return (moves,
                (lambda x,y: x == moves[y-4] or x == moves[y-2]),
                (lambda x,y: x == moves[y-3] or x == moves[y-1]))
    else:
        return [], False, False


def play():
    move_list, human_win, computer_win = [], False, False # an empty list is also false
    while not move_list:
        move_list, human_win, computer_win = make_choice(input('1 to play rock-paper-scissors\n'
                                                               '2 to play rock-paper-scissors-lizard-spock\n'
                                                               '3 to play rock-paper-fire-water-scissors\n'
                                                               'Enter the number of your choice:'))
        if not move_list:
            print('That is not a valid choice. Please enter a NUMBER to play the game next to it.')
    len_move = len(move_list)
    print()


    move = ''   # an empty string is also False
    while not move:
        move = input('Valid moves: ' + str.join(', ', move_list) + '\nEnter a move:')
        if move not in move_list:
            print('That was not a valid move.')
            move = ''
    print()

    computer_move = randint(0,len_move-1)
    if human_win(move,computer_move):
        print('You won, as', move, 'beats', move_list[computer_move], end='.\n')
        return 'human'
    elif computer_win(move,computer_move):
        print('I won, as', move_list[computer_move], 'beats', move, end='!\n')
        return 'computer'
    print('There is no winner between your', move, 'and my', move_list[computer_move], end='!\n')
    return 'ties'


def keep_playing():
    cont = 'not Y or N'
    while cont not in ('Y', 'N'):
        cont = input('Enter Y to continue playing.\n'
                     'Enter N to stop playing.').upper()
        if cont not in ('Y', 'N'):
            print('You may only enter \'Y\' or \'N\', not', cont, end='.\n')
    return cont


if __name__ == '__main__':
    wins = {'human': 0, 'computer': 0, 'ties': 0}
    playing = 'Y'
    while playing == 'Y':
        wins[play()] += 1
        playing = keep_playing()
    print('The human won', wins['human'], 'times.\n'
          'The computer won', wins['computer'], 'times.\n'
          'There were', wins['ties'], 'ties.')
