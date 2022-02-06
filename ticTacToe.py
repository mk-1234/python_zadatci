theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print('     ' + '|' + '     ' + '|')
    print('  ' + board['top-L'] + '  |  ' + board['top-M'] + '  |  ' + board['top-R'])
    print('     ' + '|' + '     ' + '|')
    print('-----+-----+-----')
    print('     ' + '|' + '     ' + '|')
    print('  ' + board['mid-L'] + '  |  ' + board['mid-M'] + '  |  ' + board['mid-R'])
    print('     ' + '|' + '     ' + '|')
    print('-----+-----+-----')
    print('     ' + '|' + '     ' + '|')
    print('  ' + board['low-L'] + '  |  ' + board['low-M'] + '  |  ' + board['low-R'])
    print('     ' + '|' + '     ' + '|')

def checkForVictory(board):
    if board['top-L'] == board['top-M'] == board['top-R'] and board['top-L'] != ' ':
        return board['top-L']
    if board['mid-L'] == board['mid-M'] == board['mid-R'] and board['mid-L'] != ' ':
        return board['mid-L']
    if board['low-L'] == board['low-M'] == board['low-R'] and board['low-L'] != ' ':
        return board['low-L']
    if board['top-L'] == board['mid-L'] == board['low-L'] and board['top-L'] != ' ':
        return board['top-L']
    if board['top-M'] == board['mid-M'] == board['low-M'] and board['top-M'] != ' ':
        return board['top-M']
    if board['top-R'] == board['mid-R'] == board['low-R'] and board['top-R'] != ' ':
        return board['top-R']
    if board['top-L'] == board['mid-M'] == board['low-R'] and board['top-L'] != ' ':
        return board['top-L']
    if board['top-R'] == board['mid-M'] == board['low-L'] and board['top-R'] != ' ':
        return board['top-R']

turn = 'X'
printBoard(theBoard)
for i in range(9):
    print('Turn for ' + turn + '. Move on which space? (top-L / top-M / top-R / mid-L / mid-M / mid-R / low-L / low-M / low-R)')
    falseEntry = 1
    while falseEntry:
        move = input()
        if move == 'exit':
            break
        if move not in theBoard.keys():
            print('That place does not exist. Try again!')
        elif theBoard[move] != ' ':
            print('There is already something in that place. Try again!')
        else:
            falseEntry = 0
    if move == 'exit':
        print('Player has left the game.')
        break
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    printBoard(theBoard)
    result = checkForVictory(theBoard)
    if result:
        print('Victory! Player ' + result + ' wins!')
        break
