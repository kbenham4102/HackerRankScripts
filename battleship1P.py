import random
import itertools


def movedesc(board, ind, i, j):
    if board[i][j] == 'h' and board[i+1][j] == 'h':
        if board[i-1][j] == '-':
            move = '%d %d' % (i-1,j)
        elif i+2 <= ind and board[i+2][j] == '-':
            move = '%d %d' % (i+2,j)
        elif i+3 <= ind and board[i+3][j] == '-':
            move = '%d %d' % (i+3,j)
        elif i+4 <= ind and board[i+4][j] == '-':
            move = '%d %d' % (i+4,j)
    elif board[i][j] == 'h' and board[i-1][j] == 'h':
        if board[i+1][j] == '-':
            move = '%d %d' % (i+1,j)
        elif i-2 >= 0 and board[i-2][j] == '-':
            move = '%d %d' % (i-2,j)
    elif board[i][j] == 'h' and board[i][j+1] == 'h':
        if board[i][j-1] == '-':
            move = '%d %d' % (i,j-1)
        elif j+2 <= ind and board[i][j+2] == '-':
            move = '%d %d' % (i,j+2)
        elif j+3 <= ind and board[i][j+3] == '-':
            move = '%d %d' % (i,j+3)
        elif j+4 <= ind and board[i][j+4] == '-':
            move = '%d %d' % (i,j+4)
    elif board[i][j] == 'h' and board[i][j-1] == 'h':
        if board[i][j+1] == '-':
            move = '%d %d' % (i,j+1)
        elif j-2 >= 0 and board[i][j-2] == '-':
            move = '%d %d' % (i,j-2)
    else:
        for ch in [(i+1,j), (i,j+1), (i-1,j), (i,j-1)]:
            n,m = ch
            if board[n][m] == '-':
                move = '%d %d' % ch
                break
    return move

def movedesctop(board, ind, i, j):
    if board[i][j] == 'h' and board[i+1][j] == 'h':
        if i+2 <= ind and board[i+2][j] == '-':
            move = '%d %d' % (i+2,j)
        elif i+3 <= ind and board[i+3][j] == '-':
            move = '%d %d' % (i+3,j)
        elif i+4 <= ind and board[i+4][j] == '-':
            move = '%d %d' % (i+4,j)
    elif board[i][j] == 'h' and board[i][j+1] == 'h':
        if board[i][j-1] == '-':
            move = '%d %d' % (i,j-1)
        elif j+2 <= ind and board[i][j+2] == '-':
            move = '%d %d' % (i,j+2)
        elif j+3 <= ind and board[i][j+3] == '-':
            move = '%d %d' % (i,j+3)
        elif j+4 <= ind and board[i][j+4] == '-':
            move = '%d %d' % (i,j+4)
    elif board[i][j] == 'h' and board[i][j-1] == 'h':
        if board[i][j+1] != 'm':
            move = '%d %d' % (i,j+1)
        elif j-2 >= 0:
            move = '%d %d' % (i,j-2)
    else:
        for ch in [(i+1,j), (i,j+1), (i,j-1)]:
            n,m = ch
            if board[n][m] != 'm' and board[n][m] != 'd':
                move = '%d %d' % ch
                break
    return move

def movedescbot(board, ind, i, j):
    if board[i][j] == 'h' and board[i-1][j] == 'h':
        move = '%d %d' % (i-2,j)
    elif board[i][j] == 'h' and board[i][j+1] == 'h':
        if board[i][j-1] == '-':
            move = '%d %d' % (i,j-1)
        elif j+2 <= ind and board[i][j+2] == '-':
            move = '%d %d' % (i,j+2)
        elif j+3 <= ind and board[i][j+3] == '-':
            move = '%d %d' % (i,j+3)
        elif j+4 <= ind and board[i][j+4] == '-':
            move = '%d %d' % (i,j+4)
    elif board[i][j] == 'h' and board[i][j-1] == 'h':
        if board[i][j+1] != 'm':
            move = '%d %d' % (i,j+1)
        elif j-2 >= 0:
            move = '%d %d' % (i,j-2)
    else:
        for ch in [(i,j+1), (i-1,j), (i,j-1)]:
            n,m = ch
            if board[n][m] != 'm' and board[n][m] != 'd':
                move = '%d %d' % ch
                break
    return move

def movedescLS(board, ind, i, j):
    if board[i][j] == 'h' and board[i+1][j] == 'h':
        if board[i-1][j] == '-':
            move = '%d %d' % (i-1,j)
        elif i+2 <= ind and board[i+2][j] == '-':
            move = '%d %d' % (i+2,j)
        elif i+3 <= ind and board[i+3][j] == '-':
            move = '%d %d' % (i+3,j)
        elif i+4 <= ind and board[i+4][j] == '-':
            move = '%d %d' % (i+4,j)
    elif board[i][j] == 'h' and board[i-1][j] == 'h':
        if board[i+1][j] != 'm':
            move = '%d %d' % (i+1,j)
        elif i-2 >= 0 and (board[i-2][j] != 'm' or board[i-2][j] != 'd'):
            move = '%d %d' % (i-2,j)
    elif board[i][j] == 'h' and board[i][j+1] == 'h':
        if j+2 <= ind and board[i][j+2] == '-':
            move = '%d %d' % (i,j+2)
        elif j+3 <= ind and board[i][j+3] == '-':
            move = '%d %d' % (i,j+3)
        elif j+4 <= ind and board[i][j+4] == '-':
            move = '%d %d' % (i,j+4)
    else:
        for ch in [(i+1,j), (i,j+1), (i-1,j)]:
            n,m = ch
            if board[n][m] != 'm' and board[n][m] != 'd':
                move = '%d %d' % ch
                break
    return move

def movedescRS(board, ind, i, j):
    if board[i][j] == 'h' and board[i+1][j] == 'h':
        if board[i-1][j] == '-':
            move = '%d %d' % (i-1,j)
        elif i+2 <= ind and board[i+2][j] == '-':
            move = '%d %d' % (i+2,j)
        elif i+3 <= ind and board[i+3][j] == '-':
            move = '%d %d' % (i+3,j)
        elif i+4 <= ind and board[i+4][j] == '-':
            move = '%d %d' % (i+4,j)
    elif board[i][j] == 'h' and board[i-1][j] == 'h':
        if board[i+1][j] != 'm':
            move = '%d %d' % (i+1,j)
        elif i-2 >= 0:
            move = '%d %d' % (i-2,j)
    elif board[i][j] == 'h' and board[i][j-1] == 'h':
        move = '%d %d' % (i,j-2)
    else:
        for ch in [(i+1,j), (i-1,j), (i,j-1)]:
            n,m = ch
            if board[n][m] != 'm' and board[n][m] != 'd':
                move = '%d %d' % ch
                break
    return move

def movedescBRC(board, ind, i, j):
    if board[i][j] == 'h' and board[i-1][j] == 'h':
        move = '%d %d' % (i-2,j)
    elif board[i][j] == 'h' and board[i][j-1] == 'h':
        move = '%d %d' % (i,j-2)
    else:
        for ch in [(i-1,j), (i,j-1)]:
            n,m = ch
            if board[n][m] != 'm' and board[n][m] != 'd':
                move = '%d %d' % ch
                break
    return move

def movedescTRC(board, ind, i, j):
    if board[i][j] == 'h' and board[i+1][j] == 'h':
        if i+2 <= ind and board[i+2][j] == '-':
            move = '%d %d' % (i+2,j)
        elif i+3 <= ind and board[i+3][j] == '-':
            move = '%d %d' % (i+3,j)
        elif i+4 <= ind and board[i+4][j] == '-':
            move = '%d %d' % (i+4,j)
    elif board[i][j] == 'h' and board[i][j-1] == 'h':
        move = '%d %d' % (i,j-2)
    else:
        for ch in [(i+1,j), (i,j-1)]:
            n,m = ch
            if board[n][m] != 'm' and board[n][m] != 'd':
                move = '%d %d' % ch
                break
    return move

def movedescBLC(board, ind, i, j):
    if board[i][j] == 'h' and board[i-1][j] == 'h':
        move = '%d %d' % (i-2,j)
    elif board[i][j] == 'h' and board[i][j+1] == 'h':
        if j+2 <= ind and board[i][j+2] == '-':
            move = '%d %d' % (i,j+2)
        elif j+3 <= ind and board[i][j+3] == '-':
            move = '%d %d' % (i,j+3)
        elif j+4 <= ind and board[i][j+4] == '-':
            move = '%d %d' % (i,j+4)
    else:
        for ch in [(i,j+1), (i-1,j)]:
            n,m = ch
            if board[n][m] != 'm' and board[n][m] != 'd':
                move = '%d %d' % ch
                break
    return move

def movedescTLC(board, ind, i, j):
    if board[i][j] == 'h' and board[i+1][j] == 'h':
        if i+2 <= ind and board[i+2][j] == '-':
            move = '%d %d' % (i+2,j)
        elif i+3 <= ind and board[i+3][j] == '-':
            move = '%d %d' % (i+3,j)
        elif i+4 <= ind and board[i+4][j] == '-':
            move = '%d %d' % (i+4,j)
    elif board[i][j] == 'h' and board[i][j+1] == 'h':
        if j+2 <= ind and board[i][j+2] == '-':
            move = '%d %d' % (i,j+2)
        elif j+3 <= ind and board[i][j+3] == '-':
            move = '%d %d' % (i,j+3)
        elif j+4 <= ind and board[i][j+4] == '-':
            move = '%d %d' % (i,j+4)
    else:
        for ch in [(i+1,j), (i,j+1)]:
            n,m = ch
            if board[n][m] != 'm' and board[n][m] != 'd':
                move = '%d %d' % ch
                break
    return move

def poscase(board, N, i, j):
    ind = N-1
    if (i != 0 and j !=0) and (i != ind and j != ind):
        move = movedesc(board, ind, i, j)
    elif i == 0 and (j != 0 and j != ind):
        move = movedesctop(board, ind, i, j)
    elif i == ind and (j != 0 and j != ind):
        move = movedescbot(board, ind, i, j)
    elif j == 0 and (i != 0 and i != ind):
        move = movedescLS(board, ind, i, j)
    elif j == ind and (i != 0 and i != ind):
        move = movedescRS(board, ind, i, j)
    elif i == ind and j == ind:
        move = movedescBRC(board, ind, i, j)
    elif i == 0 and j == ind:
        move = movedescTRC(board, ind, i, j)
    elif i == ind and j == 0:
        move = movedescBLC(board, ind, i, j)
    elif (i == 0 and j == 0):
        move = movedescTLC(board, ind, i, j)
    else:
        print("ERROR: No move made based on decision process")
    return move

N = int(input())
board = []
for i in range(N):
    board.append(list(input()))

i = 0
j = 0
indicator = None
for i in range(N):
    for j in range(N):
        if board[i][j] == 'h':
            indicator = True
            #print((i,j))
            move = poscase(board, N, i, j)
            break
    if indicator == True:
        break
# For no unsunk ships present, randomly strike a subset of board spaces.
if indicator == None:
    evens = [e for e in range(0,N,2)]
    odds = [e for e in range(1,N,2)]
    Inds = list(itertools.multiply(evens, evens)) + list(itertools.multiply(odds,odds))
    i, j = random.choice(Inds)
    while board[i][j] == 'm' or board[i][j] == 'd':
        i, j = random.choice(Inds)
    move = '%d %d' % (i,j)
print(move)
