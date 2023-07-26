import copy
import os

def getCol(board, colnum):
    col = []
    for row in board:
        col.append(row[colnum])
    return col


def getBlock(board, rownum, colnum):
    block = []
    if 0 <= rownum <= 2:
        if 0 <= colnum <= 2:
            # return 1
            for i in range(0, 3):
                for x in range(0, 3):
                    block.append(board[i][x])
        if 3 <= colnum <= 5:
            # return 2
            for i in range(0, 3):
                for x in range(3, 6):
                    block.append(board[i][x])
        if 6 <= colnum <= 8:
            # return 3
            for i in range(0, 3):
                for x in range(6, 9):
                    block.append(board[i][x])
    if 3 <= rownum <= 5:
        if 0 <= colnum <= 2:
            # return 4
            for i in range(3, 6):
                for x in range(0, 3):
                    block.append(board[i][x])
        if 3 <= colnum <= 5:
            # return 5
            for i in range(3, 6):
                for x in range(3, 6):
                    block.append(board[i][x])
        if 6 <= colnum <= 8:
            # return 6
            for i in range(3, 6):
                for x in range(6, 9):
                    block.append(board[i][x])
    if 6 <= rownum <= 8:
        if 0 <= colnum <= 2:
            # return 7
            for i in range(6, 9):
                for x in range(0, 3):
                    block.append(board[i][x])
        if 3 <= colnum <= 5:
            # return 8
            for i in range(6, 9):
                for x in range(3, 6):
                    block.append(board[i][x])
        if 6 <= colnum <= 8:
            # return 9
            for i in range(6, 9):
                for x in range(6, 9):
                    block.append(board[i][x])
    return block


def findFit(solution, row, col):
    theRow = solution[row]
    theCol = getCol(solution, col)
    theBlock = getBlock(solution, row, col)
    current = solution[row][col]
    for i in range(current + 1, 10):
        if i not in theRow and i not in theCol and i not in theBlock:
            return i
    return 0

def validate(board, row, col):
    theRow = board[row]
    theCol = getCol(board, col)
    theBlock = getBlock(board, row, col)
    current = board[row][col]
    if theRow.count(current) == 1 and theCol.count(current) == 1 and theBlock.count(current) == 1:
        return True
    return False


def printBoard(board, input=False):
    rowtext = ''
    print('||=====================================||')
    for rowNum in range(0, 9):
        rowtext = '|| '
        if input and rowNum == input[0]:
            for colNum in range(0, 9):
                if colNum == input[1]:
                    rowtext += '?' + ' | '
                elif board[rowNum][colNum] != 0:
                    rowtext += str(board[rowNum][colNum]) + ' | '
                else:
                    rowtext += '- | '
                if colNum == 2 or colNum == 5:
                    rowtext = rowtext[0:-1] + '| '
        else:
            for colNum in range(0, 9):
                if board[rowNum][colNum] != 0:
                    rowtext += str(board[rowNum][colNum]) + ' | '
                else:
                    rowtext += '- | '
                if colNum == 2 or colNum == 5:
                        rowtext = rowtext[0:-1] + '| '
        rowtext = rowtext[0:-1] + '|'
        print(rowtext)
        if rowNum == 2 or rowNum == 5:
            print('||=====================================||')
    print('||=====================================||')

original_board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

#fill board
fillRow = 0
fillCol = 0
filled = False

while not filled:
    os.system('cls' if os.name == 'nt' else 'clear')
    printBoard(original_board, [fillRow, fillCol])
    userInput = int(input('Enter number for the marked spot (-1 to fix): ') or '0')
    if 0 <= userInput < 10:
        original_board[fillRow][fillCol] = userInput
        if fillCol == 8:
            if fillRow == 8:
                filled = True
            else:
                fillRow += 1
                fillCol = 0
        else: 
            fillCol += 1

    elif userInput == -1:
        if fillCol == 0 and fillRow != 0:
            fillRow -= 1
            fillCol = 8
        elif not (fillCol == 0 and fillRow == 0):
            fillCol -= 1
    else:
        print('invalid input!')

os.system('cls' if os.name == 'nt' else 'clear')
print('The Board:')
printBoard(original_board)

solved = False
noSolution = False

for i in range(0, 9):
    for j in range(0, 9):
        if original_board[i][j] != 0:
            if not validate(original_board, i, j):
                solved = True
                noSolution = True

print('\nSOLVING...')

solution = copy.deepcopy(original_board)
currentRow = 0
currentCol = 0
actions = []
lastAction = []
goBack = False

while not solved:
    if solution[currentRow][currentCol] == 0 or goBack:
        solution[currentRow][currentCol] = findFit(solution, currentRow, currentCol)
        if solution[currentRow][currentCol] != 0:
            goBack = False
            #print('CHANGES!')
            #for i in solution:
            #    print(i)
            actions.append([currentRow, currentCol])
            if currentCol == 8:
                if currentRow == 8:
                    solved = True
                else:
                    currentCol = 0
                    currentRow += 1
            else:
                currentCol += 1
        else:
            # go back
            # print('GOBACK!')
            goBack = True
            if len(actions) > 0:
                lastAction = actions.pop()
                #print(lastAction)
                currentRow = lastAction[0]
                currentCol = lastAction[1]
            else:
                if currentCol == 0 and currentRow == 0:
                    solved = True
                    noSolution = True
                else:
                    goBack = False
                    currentCol = 0
                    currentRow = 0

    else:
        if currentCol == 8:
            if currentRow == 8:
                solved = True
            else:
                currentCol = 0
                currentRow += 1
        else:
            currentCol += 1

if noSolution:
    print('\nNO SOLUION!\n')
else:
    print('\nSOLVED!\nSolution:')
    printBoard(solution)