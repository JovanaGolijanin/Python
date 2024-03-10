# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import copy
import random



def MakeTable():
    table = []
    for i in range(0,4):
        row = []
        for j in range(0, 5):
            row.append(random.randint(0, 3))
        table.append(row)
    return table

def PrintTable(table):
    for i in range(0,4):
        for j in range(0, 5):
            print(table[i][j], end='  ')
        print("")

def MakeDominoPeces():
    peces = []
    for i in range(0,4):
        for j in range(0, 4):
            peces.append((i, j))
    return peces

def PlayPeace(table: list, i, j, direction):
    newTable = copy.deepcopy(table)
    newTable[i][j] = -1
    if direction == "U":
        newTable[i - 1][j] = -1
    elif direction == "D":
        newTable[i + 1][j] = -1
    elif direction == "L":
        newTable[i][j - 1] = -1
    elif direction == "R":
        newTable[i][j + 1] = -1
    return newTable

def CheckAdjesantAreas(table, i, j, peace, placemants):
    moves = []
    if i > 0 and table[i - 1][j] == peace[1]:
        moves.append((i, j, "U"))
    if i < 3 and table[i + 1][j] == peace[1]:
        moves.append((i, j, "D"))
    if j > 0 and table[i][j - 1] == peace[1]:
        moves.append((i, j, "L"))
    if j < 4 and table[i][j + 1] == peace[1]:
        moves.append((i, j, "R"))
    return moves

def GetAllPosiblePlacesForPeace(table, peace):
    placemants = []
    for i in range(0, 4):
        for j in range(0, 5):
            if table[i][j] == peace[0]:
               placemants += CheckAdjesantAreas(table, i, j, peace, placemants)
    return placemants

# def GenAllPosibleMoves(table, myPeaces):
#     allMoves = []
#     for peace in myPeaces:
#         allMoves.append((peace, GetAllPosiblePlacesForPeace(table, peace)))
#     return  allMoves

def CheckSolved(table):
    for i in range(0, 4):
        for j in range(0, 5):
            if table[i][j] != -1:
                return 0
    return 1

def FindMoves(table, myPeaces):
    if len(myPeaces) == 0:
        if CheckSolved(table) == 1:
            return ()
        else:
            return None

    peace = myPeaces[0]
    peaceMoves = GetAllPosiblePlacesForPeace(table, peace)
    if len(peaceMoves) == 0:
        newPeaces = copy.deepcopy(myPeaces)
        newPeaces.remove(peace)
        moves = FindMoves(copy.deepcopy(table), newPeaces)
        if moves is not None:
            return moves
        else:
            return None

    for move in peaceMoves:
        # print(peace, move)
        # PrintTable(table)
        newPeaces = copy.deepcopy(myPeaces)
        newPeaces.remove(peace)
        moves = FindMoves(PlayPeace(table, move[0], move[1], move[2]), newPeaces)
        if moves is not None:
            return (peace, move) + moves
    return None


if __name__ == '__main__':
    tabla = MakeTable()
    # tabla = [[2, 3, 2, 2, 2], [3, 0, 3, 0, 0], [3, 0, 3, 1, 1], [0, 1, 1, 1, 2]]
    peces = MakeDominoPeces()
    PrintTable(tabla)
    print(peces)
    res = FindMoves(tabla, peces)
    # while res is None:
    #     table = MakeTable()
    #     peces = MakeDominoPeces()
    #     res = FindMoves(table, peces)

    print(res)

