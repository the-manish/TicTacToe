import numpy
board=numpy.array([['_','_','_'],['_','_','_'],['_','_','_']])
p1s='X'
p2s='O'

def place(symbol):
    print(numpy.matrix(board))
    while(1):
     row=int(input('Enter row -1 or 2 or 3:'))
     col=int(input('Enter column -1 or 2 or 3:'))
     if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='_':
        break
     else:
         print('Invalid input. Please enter again')
    board[row-1][col-1]=symbol

def play():
    for turn in range(9):
        if turn%2==0:
            print('X turn')
            place(p1s)
            if won(p1s):
                break
            else:
                print('O turn')
                place(p2s)
                if won(p2s):
                    break