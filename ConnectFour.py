import random

def turn(column,board,player):
    if column < 0 or column > 6 or board[5][column] != None:
        return None
    for i in range(6):
        if board[i][column] == None:
            row = i
            board[i][column] = player
            break
    return row

def print_board(board):
    for i in range(len(board)-1,-1,-1):
        print('|',end=' ')
        for ii in board[i]:
            print(ii,'|',end=' ')
        print('')

def check_win(board,row,column):
    player = board[row][column]
    #verticle win
    if row >= 3:
        win = True
        for i in range(row-1,row-4,-1):
            if board[i][column] != player:
                win = False
        if win:
            print('verticle win')
            return True
    #right left win
    win = True
    start = column
    end = column
    for i in range(column-1,column-4,-1):
        if i >= 0:
            test1 = board[row][i]
            if board[row][i] != player:
                start = i + 1
                break
        else:
            start = 0
            break
    for i in range(column+1,column+4):
        if i <= 7:
            test2 = board[row][i]
            if board[row][i] != player:
                end = i-1
                break
        else:
            end = 7
            break
    if end-start >=3:
        print('left right win')
        return True
    #diagonal  win
    startRow = row
    startColumn = column
    endRow = row
    endColumn = column
    for i in range(-1,-4,-1):
        if (startRow + i) >= 0 and (startColumn + i) >= 0:
            if board[startRow+i][startColumn+i] != player:
                startRow = startRow+i+1
                startColumn = startColumn+i+1
                break
    return False

            
def main():
    board = [[None for _ in range(7)] for _ in range(6)]
    print_board(board)
    player = '\033[34mBlue\033[37m'
    win = False
    while win == False:
        running = True
        while running:
            column = int(input('Column 0-6:'))
            row = turn(column,board,player)
            if row != None:
                running = False
                if check_win(board,row,column):
                    win = True
            else:
                print('Invalid Move')
        player = (player=='\033[34mBlue\033[37m') * '\033[31mRed \033[37m' + (player=='\033[31mRed \033[37m') * '\033[34mBlue\033[37m'
        print_board(board)
main()