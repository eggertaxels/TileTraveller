# Constants
N = '(N)orth'
S = '(S)outh'
E = '(E)ast'
W = '(W)est'

col, row = 1, 1
move_is_right = ('')
direction = ''
victory = False
again = 0

def move(col, row, direction):
    ''' Take in current position and return a new position'''

    if direction.lower() == 'n':
        row += 1
    elif direction.lower() == 's':
        row -= 1
    elif direction.lower() == 'e':
        col += 1
    elif direction.lower() == 'w':
        col -= 1
    return col, row

def play(victory, direction, move_is_right, col, row, again):
    ''' Main game '''
    while not victory:
        if direction in move_is_right or again == 1:
            if ((col == 1) and (row == 1)) or ((col == 2) and (row == 1)):  # (1,1) / (2,1)
                print(f"You can travel: {N}.")
                move_is_right = ('n')
                again = 0
            elif (col == 1) and (row == 2):
                print(f"You can travel: {N} or {E} or {S}.")
                move_is_right = ('n', 'e', 's')
                again = 0
            elif (col == 1) and (row == 3):
                print(f"You can travel: {E} or {S}.")
                move_is_right = ('e', 's')
                again = 0
            elif (col == 2) and (row == 2):
                print(f"You can travel: {S} or {W}.")
                move_is_right = ('s', 'w')
                again = 0
            elif (col == 3) and (row == 3):
                print(f"You can travel: {S} or {W}.")
                move_is_right = ('s', 'w')
                again = 0
            elif (col == 2) and (row == 3):
                print(f"You can travel: {E} or {W}.")
                move_is_right = ('e', 'w')
                again = 0
            elif (col == 3) and (row == 2):
                print(f"You can travel: {N} or {S}.")
                move_is_right = ('n', 's')
                again = 0
            elif col == 3 and row == 1:
                print('Victory!')
                break

        direction = str(input("Direction: "))
        direction = direction.lower()
        if direction in move_is_right:
            col, row = move(col, row, direction)
        else:
            print('Not a valid direction!')
            again = 1


play(victory, direction, move_is_right, col, row, again)
