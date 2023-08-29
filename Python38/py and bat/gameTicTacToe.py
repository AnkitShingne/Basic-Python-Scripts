theBoard = {'top-L':' ','top-M':' ','top-R':' ',
            'mid-L':' ','mid-M':' ','mid-R':' ',
            'low-L':' ','low-M':' ','low-R':' '}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)

def get_input(key,p):
    if p == 1:
        theBoard[key] = '0'
    else:
        theBoard[key] = 'X'

def bewa(p):
    if theBoard['top-L']==theBoard['top-M']==theBoard['top-R'] and
    theBoard['top-L']!= ' ' and theBoard['top-M'] != ' ' and theBoard['top-R'] != ' ':
        print('You are winner.',p)
        return 1
    elif theBoard['mid-L']==theBoard['mid-M']==theBoard['mid-R'] and
    theBoard['mid-L']!= ' ' and theBoard['mid-M'] != ' ' and theBoard['mid-R'] != ' ':
        print('You are winner.',p)
        return 1
    elif theBoard['low-L']==theBoard['low-M']==theBoard['low-R'] and
    theBoard['low-L']!= ' ' and theBoard['low-M'] != ' ' and theBoard['low-R'] != ' ':
        print('You are winner.',p)
        return 1
    elif theBoard['top-L']==theBoard['mid-L']==theBoard['low-L'] and
    theBoard['top-L']!= ' ' and theBoard['mid-L'] != ' ' and theBoard['low-L'] != ' ':
        print('You are winner.',p)
        return 1
    elif theBoard['top-M']==theBoard['mid-M']==theBoard['low-M'] and
    theBoard['top-M']!= ' ' and theBoard['mid-M'] != ' ' and theBoard['low-M'] != ' ':
        print('You are winner.',p)
        return 1
    elif theBoard['top-R']==theBoard['mid-R']==theBoard['low-R'] and
    theBoard['top-R']!= ' ' and theBoard['mid-R'] != ' ' and theBoard['low-R'] != ' ':
        print('You are winner.',p)
        return 1
    elif theBoard['top-L']==theBoard['mid-M']==theBoard['low-R'] and
    theBoard['top-L']!= ' ' and theBoard['mid-M'] != ' ' and theBoard['low-R'] != ' ':
        print('You are winner.',p)
        return 1
    elif theBoard['top-R']==theBoard['mid-M']==theBoard['low-L'] and
    theBoard['top-R']!= ' ' and theBoard['mid-M'] != ' ' and theBoard['low-L '] != ' ':
        print('You are winner.',p)
        return 1
    else:
        return 0

def bewakuf():
    print('Please play player 1')
    print('Choose')

    Fus = {'1':'top-L','2':'top-M','3':'top-R',
           '4':'mid-L','5':'mid-M','6':'mid-R',
           '7':'low-L','8':'low-M','9':'low-R'}
    q = input()
    get_input(Fus.getitem(q),1)
    printBoard()
    bewa('player1')
    print('Please play player 2')
    print('Choose')
    q = input()
    get_input(Fus.getitem(q),2)
    printBoard()
    bewa('player2')
for i in range(1,10):
    if bewa('s')== 0:
        bewakuf()
    else:
        break
print('It is a draw.')








