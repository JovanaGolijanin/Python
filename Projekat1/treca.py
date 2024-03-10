import sys
import string

matrix = []
firstPlayer = 0
turn = 'X'
numRows = 0
numColumns = 0

# Implement functions to obtain initial game parameters
def init():
  global matrix
  global numRows
  global numColumns

  print("Enter number of rows:")
  numRows = int(sys.stdin.readline())

  print("Enter number of columns:")
  numColumns = int(sys.stdin.readline())

  matrix = [ [ " " for i in range(numColumns) ] for j in range(numRows) ]

# Implement functions to display any state of the game
def print_board(matrix):
  top(numColumns)

  for x in range(0,numRows):
    print(str(numRows-x)+"||",end='')
    for num in range(0,numColumns):
      print(matrix[x][num]+'|',end='')
    print("|"+str(numRows-x))
    
  bottom(numColumns)    

def top(numColumns):
  print('  ',end='')
  for num in range(0,numColumns):
    print(' '+string.ascii_uppercase[num],end='')
  print('')
  print('  ',end='')
  for num in range(0,numColumns):
    print(' =',end='')
  print('')

def bottom(numColumns):
  print('  ',end='')
  for num in range(0,numColumns):
    print(' =',end='')
  print('')
  print('  ',end='')
  for num in range(0,numColumns):
    print(' '+string.ascii_uppercase[num],end='')
  print('')

# Implement functions to check if a move is valid
# row 1..N | column A..Z
def moveValid(row,column): 
  col = ord(column)-65
  r = numRows-row

  if(r<0 or col<0):
    return False
  
  if(turn=='X'):

    if((r+1)>=numRows or col>=numColumns):
      return False

    if(matrix[r][col]==' ' and matrix[r+1][col]==' '):
      return True
    else:
      return False
  else:
    if(r>=numRows or (col+1)>=numColumns):
      return False

    if(matrix[r][col]==' ' and matrix[r][col+1]==' '):
      return True
    else:
      return False

# Implement functions to change the current state of the game based on a given player's move and transition to a new state
def playMove(row,column):
    global matrix
    global turn

    if(moveValid(row,column)):
        kol = ord(column)-65
        vrs = numRows-row
        if(naPotezu=='X'):
            matrix[vrs][kol]='X'
            matrix[vrs+1][kol]='X'
            naPotezu='O'
        else:
            matrix[vrs][kol]='O'
            matrix[vrs][kol+1]='O'
            naPotezu='X'
        getGameStatus()
        print_board(matrix)
    else:
        print("Uneli ste nevalidni potez!")


###########
#nadole je sam odradio , treba da ubacim još što nije preveo

#Napisati funkcije za proveru kraja igre
def krajIgre():
    if(naPotezu=='X'):
        for i in range(0,brojVrsta-1):
            for j in range(0,brojKolona):
                if(matrica[i][j]==' ' and matrica[i+1][j]==' '):
                    return False
    else:
        for i in range(0,brojVrsta):
            for j in range(0,brojKolona-1):
                if(matrica[i][j]==' ' and matrica[i][j+1]==' '):
                    return False
    return True #Kraj je igre zato sto nema slobodnih polja za igraca koj je na potezu


#Omogućiti izbor ko će igrati prvi (čovek ili računar)
def koIgraPrvi():
    global igraPrvi

    print("Ko igra prvi? (0-covek, 1-racunar):")
    igraPrvi = int(sys.stdin.readline())
    if(igraPrvi==0):
        print("Covek je prvi na potezu!")
    else:
        print("Racunar je prvi na potezu!")

#Realizovati funkcije koje na osnovu zadatog igrača na potezu i zadatog stanje igre formiraju sva moguća stanja igre (sve moguće table)
def svaMogucaStanja():
    if(naPotezu=='X'):
        for i in range(0,brojVrsta-1):
            for j in range(0,brojKolona):
                if(matrica[i][j]==' ' and matrica[i+1][j]==' '):
                    matrica[i][j] = 'X'
                    matrica[i+1][j] = 'X'
                    stampaj(matrica)
                    matrica[i][j] = ' '
                    matrica[i+1][j] = ' '

    else:
        for i in range(0,brojVrsta):
            for j in range(0,brojKolona-1):
                if(matrica[i][j]==' ' and matrica[i][j+1]==' '):
                    matrica[i][j] = 'O'
                    matrica[i][j+1] = 'O'
                    stampaj(matrica)
                    matrica[i][j] = ' '
                    matrica[i][j+1] = ' '

# Realize functions that, based on the current state of the game, generate and return all possible moves for the player who has the next turn
def generateMoves():
  global turn

  moves = []
  if turn == 'X':
    for i in range(numRows):
      for j in range(numColumns):
        if matrix[i][j] == ' ':
          if (i+1) < numRows and matrix[i+1][j] == ' ':
            moves.append((i,j))
  else:
    for i in range(numRows):
      for j in range(numColumns):
        if matrix[i][j] == ' ':
          if (j+1) < numColumns and matrix[i][j+1] == ' ':
            moves.append((i,j))
  return moves

# Implement a function that, based on the current state of the game, returns a value that indicates the current status of the game (win, draw, undecided)
def getGameStatus():
  x_count = 0
  o_count = 0
  for i in range(numRows):
    for j in range(numColumns):
      if matrix[i][j] == 'X':
        x_count += 1
      elif matrix[i][j] == 'O':
        o_count += 1

  if x_count + o_count == numRows * numColumns:
    return 'draw'
  elif x_count == 0:
    return 'O'
  elif o_count == 0:
    return 'X'
  else:
    return 'undecided'

# Implement the minimax function with alpha-beta pruning
def minimax(depth, alpha, beta, maximizingPlayer):
  gameStatus = getGameStatus()
  if gameStatus != 'undecided':
    if gameStatus == 'X':
      return 1
    elif gameStatus == 'O':
      return -1
    elif gameStatus == 'draw':
      return 0

  if maximizingPlayer:
    maxEval = -sys.maxsize
    for move in generateMoves():
      matrix[move[0]][move[1]] = 'X'
      eval = minimax(depth+1, alpha, beta, False)
      matrix[move[0]][move[1]] = ' '
      maxEval = max(maxEval, eval)
      alpha = max(alpha, eval)
      if beta <= alpha:
        break
    return maxEval
  else:
    minEval = sys.maxsize
    for move in generateMoves():
      matrix[move[0]][move[1]] = 'O'
      eval = minimax(depth+1, alpha, beta, True)
      matrix[move[0]][move[1]] = ' '
      minEval = min(minEval, eval)
      beta = min(beta, eval)
      if beta <= alpha:
        break
    return minEval

# Implement the main function to play the game
def main():
  global firstPlayer
  global turn

  init()
  print_board(matrix)

  while True:
    gameStatus = getGameStatus()
    if gameStatus != 'undecided':
      print("Game over! " + gameStatus + " wins.")
      break

    if firstPlayer:
      print("Enter move (row column): ")
      move = input().split()
      row = int(move[0])
      column = move[1]
      if moveValid(row, column):
        playMove(row, column)
        firstPlayer = False
        turn = 'O'
      else:
        print("Invalid move.")
    else:
      bestMove = None
      maxEval = -sys.maxsize
      for move in generateMoves():
        matrix[move[0]][move[1]] = 'O'
        eval = minimax(0, -sys.maxsize, sys.maxsize, True)
        matrix[move[0]][move[1]] = ' '
        if eval > maxEval:
          maxEval = eval
          bestMove = move
      playMove(numRows-bestMove[0], chr(bestMove[1]+65))
      firstPlayer = True
      turn = 'X'

    print_board(matrix)

main()
