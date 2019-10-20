import copy

def possibleMoves(board):
    moves = []
    index = 0
    for i in board:
        for j in range(len(i)):
            if i[j] == '-':
                moves.append([j,index])
        index = index +1
    return moves                

def checkScore(board):
    columns = [[],[],[]]
    diagonals = [[],[]]
    for i in board:
        columns[0].append(i[0])
        columns[1].append(i[1])
        columns[2].append(i[2]) 
    diagonals[0].append(board[0][0])
    diagonals[0].append(board[1][1])
    diagonals[0].append(board[2][2])
    diagonals[1].append(board[0][2])
    diagonals[1].append(board[1][1])
    diagonals[1].append(board[2][0])
    for i in board:
        if i[0] == 'X' and i[1] == 'X' and i[2] == 'X':
            return 1
        elif i[0] == 'O' and i[1] == 'O' and i[2] == 'O':
            return -1

    for i in columns:
        if i[0] == 'X' and i[1] == 'X' and i[2] == 'X':
            return 1
        elif i[0] == 'O' and i[1] == 'O' and i[2] == 'O':
            return -1

    for i in diagonals:
        if i[0] == 'X' and i[1] == 'X' and i[2] == 'X':
            return 1
        elif i[0] == 'O' and i[1] == 'O' and i[2] == 'O':
            return -1
    return 0

def miniMax(board,maximizer):
    scores = []
    if maximizer:
        moves = possibleMoves(board)
        if moves:
            for i in moves:
                temp = copy.deepcopy(board)
                temp[i[1]][i[0]] = 'X'
                score = checkScore(temp)
                if score == 0:
                    scores.append([miniMax(copy.deepcopy(temp),False)[0],i[1],i[0]])
                else:
                    scores.append([score,i[1],i[0]])
        else:
            scores.append([checkScore(board),board])

        scores = sorted(scores) 
        return scores.pop()
    else:
        moves = possibleMoves(board)
        if moves:
            for i in moves:
                temp = copy.deepcopy(board)
                temp[i[1]][i[0]] = 'O'
                score = checkScore(temp)
                if score == 0:
                    scores.append([miniMax(copy.deepcopy(temp),True)[0],i[1],i[0]])
                else:
                    scores.append([score,i[1],i[0]])
        else:
            scores.append([checkScore(board),board])
        scores = sorted(scores)
        return scores[0]

    
def playersTurn(board):
    for i in board:
        print(i)
    
    x,y = 1000,1000

    while(True):
        x,y = input("Enter your move (x, y)\n").split(',')
        x = int(x)
        y = int(y)
        if x > 2 or y > 2:
            print("Invalid input")
        elif board[y][x] != '-':
            print("spot is taken")
        else:
            break
    
    board[y][x] = 'O'
    return board

def compTurn(board):
    bestMove = miniMax(copy.deepcopy(board),True)
    board[bestMove[1]][bestMove[2]] = 'X'
    return board


def game(board):
    while(1):
        if possibleMoves(copy.deepcopy(board)):
            playersTurn(board)
            check = checkScore(copy.deepcopy(board))
            if check == -1:
                print("Final Board:")
                for i in board:
                    print(i)
                print("You Won!")
                break
        else:
            print("Final Board:")
            for i in board:
                print(i)
            print("Draw!")
            break

        if possibleMoves(copy.deepcopy(board)):
            compTurn(board)
            check = checkScore(copy.deepcopy(board))
            if check == 1:
                print("Final Board:")
                for i in board:
                    print(i)
                print("youre a loser")
                break
        else:
            print("Final Board:")
            for i in board:
                print(i)
            print("Draw!")
            break

board = [['X','-','-'],['-','-','-'],['-','-','-',]]
game(board)
#checkScore(board)