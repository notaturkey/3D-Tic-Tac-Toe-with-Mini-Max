import copy

def possibleMoves(board):
    moves = []
    y = 0
    z = 0
    for layer in board:
        y=0
        for i in layer:
            for x in range(len(i)):
                if i[x] == '-':
                    moves.append([x,y,z])
            y = y +1
        z=z+1
    return moves                

def checkWin(board):
    for layer in board:
        columns = [[],[],[]]
        diagonals = [[],[]]
        for i in layer:
            columns[0].append(i[0])
            columns[1].append(i[1])
            columns[2].append(i[2]) 
        diagonals[0].append(layer[0][0])
        diagonals[0].append(layer[1][1])
        diagonals[0].append(layer[2][2])
        diagonals[1].append(layer[0][2])
        diagonals[1].append(layer[1][1])
        diagonals[1].append(layer[2][0])
        for i in layer:
            if i[0] == 'X' and i[1] == 'X' and i[2] == 'X':
                return True
            elif i[0] == 'O' and i[1] == 'O' and i[2] == 'O':
                return True

        for i in columns:
            if i[0] == 'X' and i[1] == 'X' and i[2] == 'X':
                return True
            elif i[0] == 'O' and i[1] == 'O' and i[2] == 'O':
                return True

        for i in diagonals:
            if i[0] == 'X' and i[1] == 'X' and i[2] == 'X':
                return True
            elif i[0] == 'O' and i[1] == 'O' and i[2] == 'O':
                return True
    
    #check along z axis
    layer0 = board[0]
    layer1 = board[1]
    layer2 = board[2]

    for i in range(3):
        for j in range(3):
            if layer0[i][j] == 'X' and layer1[i][j] == 'X' and layer2[i][j] == 'X':
                return True
            elif layer0[i][j] == 'O' and layer1[i][j] == 'O' and layer2[i][j] == 'O':
                return True
            
    
    #check diagonals 
    diagonals = []
    #along x z axis 
    for i in range(3):
        diagonals.append([layer0[0][i], layer1[1][i], layer2[2][i]])
        diagonals.append([layer0[2][i], layer1[1][i], layer2[0][i]])
    
    #along y z axis 
    for i in range(3):
        diagonals.append([layer0[i][0], layer1[i][1], layer2[i][2]])
        diagonals.append([layer0[i][2], layer1[i][1], layer2[i][0]])

    #along xyz 
    diagonals.append([layer0[0][0], layer1[1][1], layer2[2][2]])
    diagonals.append([layer0[2][0], layer1[1][1], layer2[0][2]])
    diagonals.append([layer0[0][2], layer1[1][1], layer2[2][0]]) 
    diagonals.append([layer0[2][2], layer1[1][1], layer2[0][0]])
    for i in diagonals:
            if i[0] == 'X' and i[1] == 'X' and i[2] == 'X':
                return True
            elif i[0] == 'O' and i[1] == 'O' and i[2] == 'O':
                return True
    return False


def checkScore(board):
    sum = 0
    for layer in board:
        columns = [[],[],[]]
        diagonals = [[],[]]
        for i in layer:
            columns[0].append(i[0])
            columns[1].append(i[1])
            columns[2].append(i[2]) 
        diagonals[0].append(layer[0][0])
        diagonals[0].append(layer[1][1])
        diagonals[0].append(layer[2][2])
        diagonals[1].append(layer[0][2])
        diagonals[1].append(layer[1][1])
        diagonals[1].append(layer[2][0])
        for i in layer:
            if i[0] == 'X' and i[1] == 'X' and i[2] == 'X':
                return 3
            elif i[0] == 'O' and i[1] == 'O' and i[2] == 'O':
                return -3 

        for i in columns:
            if i[0] == 'X' and i[1] == 'X' and i[2] == 'X':
                return 3
            elif i[0] == 'O' and i[1] == 'O' and i[2] == 'O':
                return -3

        for i in diagonals:
            if i[0] == 'X' and i[1] == 'X' and i[2] == 'X':
                return 3
            elif i[0] == 'O' and i[1] == 'O' and i[2] == 'O':
                return -3
    
    #check along z axis
    layer0 = board[0]
    layer1 = board[1]
    layer2 = board[2]

    for i in range(3):
        for j in range(3):
            if layer0[i][j] == 'X' and layer1[i][j] == 'X' and layer2[i][j] == 'X':
                return 3
            elif layer0[i][j] == 'O' and layer1[i][j] == 'O' and layer2[i][j] == 'O':
                return -3
            
    
    #check diagonals 
    diagonals = []
    #along x z axis 
    for i in range(2):
        diagonals.append([layer0[0][i], layer1[1][i], layer2[2][i]])
        diagonals.append([layer0[2][i], layer1[1][i], layer2[0][i]])
    
    #along y z axis 
    for i in range(2):
        diagonals.append([layer0[i][0], layer1[i][1], layer2[i][2]])
        diagonals.append([layer0[i][2], layer1[i][1], layer2[i][0]])

    #along xyz 
    diagonals.append([layer0[0][0], layer1[1][1], layer2[2][2]])
    diagonals.append([layer0[2][0], layer1[1][1], layer2[0][2]])
    diagonals.append([layer0[0][2], layer1[1][1], layer2[2][0]]) 
    diagonals.append([layer0[2][2], layer1[1][1], layer2[0][0]])
    for i in diagonals:
            if i[0] == 'X' and i[1] == 'X' and i[2] == 'X':
                return 3
            elif i[0] == 'O' and i[1] == 'O' and i[2] == 'O':
                return -3
    return 0


def miniMax(board,maximizer, depth):
    if depth == 3:
        return [checkScore(board),[]]

    if maximizer:
        best = -10000000
        moves = possibleMoves(board)
        if moves:
            bestMove = []
            for i in moves:
                temp = copy.deepcopy(board)
                temp[i[2]][i[1]][i[0]] = 'X'
                value = [-10000000, []]
                if checkWin(temp):
                    best = 7-depth
                    bestMove = i
                else:
                    value = miniMax(temp, False, depth+1)
                if value[0] > best:
                    best = value[0]
                    bestMove = i
            return [best, bestMove]
    else:
        best = 10000000
        moves = possibleMoves(board)
        if moves:
            bestMove = []
            for i in moves:
                temp = copy.deepcopy(board)
                temp[i[2]][i[1]][i[0]] = 'O'
                value = [10000000, []]
                if checkWin(temp) == True:
                    best = depth-7
                    bestMove = i
                else:
                    value = miniMax(temp, True, depth+1)
                if value[0] < best:
                    best = value[0]
                    bestMove = i
            return [best, bestMove]

def playersTurn(board):
    printBoard(board)
    x,y,z = 1000,1000,1000

    while(True):
        x,y,z = input("Enter your move i.e: x, y, z \n").split(',')
        x = int(x)
        y = int(y)
        z = int(z)
        if x > 2 or y > 2 or z>2:
            print("Invalid input")
        elif board[z][y][x] != '-':
            print("spot is taken")
        else:
            break
    board[z][y][x] = 'O'
    return board

def compTurn(board):
    bestMove = miniMax(copy.deepcopy(board), True,0)
    board[ bestMove[1][2]] [ bestMove[1][1] ][ bestMove[1][0] ] = 'X'
    return board


def game(board):
    while(1):
        
        if possibleMoves(copy.deepcopy(board)):
            playersTurn(board)
            check = checkWin(copy.deepcopy(board))
            if check:
                print("Final Board:")
                printBoard(board)
                print("You Won!")
                break
        else:
            print("Final Board:")
            printBoard(board)
            print("Draw!")
            break

        if possibleMoves(copy.deepcopy(board)):
            compTurn(board)
            check = checkWin(copy.deepcopy(board))
            if check:
                print("Final Board:")
                printBoard(board)
                print("youre a loser")
                break
        else:
            print("Final Board:")
            printBoard(board)
            print("Draw!")
            break
        


def printBoard(board):
    count = 0
    for i in board:
        print("Layer " +str(count)+" in board:")
        for j in i:
            print (j)
        count = count +1

board = [ [['-','-','-'],['-','-','-'],['-','-','-',]],[['-','-','-'],['-','X','-'],['-','-','-',]],[['-','-','-'],['-','-','-'],['-','-','-']]  ]
#print(checkWin(board))
game(board)
#checkScore(board)