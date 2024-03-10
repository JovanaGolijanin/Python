import string
import sys

matrica = []
igraPrvi = 0
naPotezu = 'X'
brojVrsta = 0
brojKolona = 0

#Implementirati funkcije koje obezbeđuju unos početnih parametara igre
def init():
    global matrica
    global brojVrsta
    global brojKolona

    print("Unesite broj vrsta:")
    brojVrsta = int(sys.stdin.readline())

    print("Unesite broj kolona:")
    brojKolona = int(sys.stdin.readline())

    matrica = [ [ " " for i in range(brojKolona) ] for j in range(brojVrsta) ]

#Implementirati funkcije koje obezbeđuju prikaz proizvoljnog stanja problema (igre)
def stampaj(matrica):
    top(brojKolona)

    for x in range(0,brojVrsta):
        print(str(brojVrsta-x)+"||",end='')
        for num in range(0,brojKolona):
            print(matrica[x][num]+'|',end='')
        print("|"+str(brojVrsta-x))
        
    bottom(brojKolona)    

def top(brojKolona):
    print('  ',end='')
    for num in range(0,brojKolona):
        print(' '+string.ascii_uppercase[num],end='')
    print('')
    print('  ',end='')
    for num in range(0,brojKolona):
        print(' =',end='')
    print('')

def bottom(brojKolona):
    print('  ',end='')
    for num in range(0,brojKolona):
        print(' =',end='')
    print('')
    print('  ',end='')
    for num in range(0,brojKolona):
        print(' '+string.ascii_uppercase[num],end='')
    print('')


#Realizovati funkcije koje proveravaju da li je potez valjan
# vrsta 1..N | kolona A..Z
def potezValjan(vrsta,kolona): 
    kol = ord(kolona)-65
    vrs = brojVrsta-vrsta

    if(vrs<0 or kol<0):
        return False
    
    if(naPotezu=='X'):

        if((vrs+1)>=brojVrsta or kol>=brojKolona):
            return False

        if(matrica[vrs][kol]==' ' and matrica[vrs+1][kol]==' '):
            return True
        else:
            return False
    else:
        if(vrs>=brojVrsta or (kol+1)>=brojKolona):
            return False

        if(matrica[vrs][kol]==' ' and matrica[vrs][kol+1]==' '):
            return True
        else:
            return False

#Realizovati funkcije koje na osnovu zadatog poteza igrača menjaju trenutno stanjeproblema (igre) i prelaze u novo
def odigrajPotez(vrsta,kolona):
    global matrica
    global naPotezu

    if(potezValjan(vrsta,kolona)):
        kol = ord(kolona)-65
        vrs = brojVrsta-vrsta
        if(naPotezu=='X'):
            matrica[vrs][kol]='X'
            matrica[vrs+1][kol]='X'
            naPotezu='O'
        else:
            matrica[vrs][kol]='O'
            matrica[vrs][kol+1]='O'
            naPotezu='X'
        krajIgre()
        stampaj(matrica)
    else:
        print("Uneli ste nevalidni potez!")

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

from typing import List, Tuple

# The minimax function takes in the current game state, the current depth of the search tree,
# and the alpha and beta values for alpha-beta pruning. It returns the minimax value
# and the best move for the current player.
def minimax(state: List[List[str]], depth: int, alpha: int, beta: int) -> Tuple[int, Tuple[int, int]]:
    # If the game is over or we have reached the maximum search depth, return the heuristic value of the state
    if game_over(state) or depth == 0:
        return heuristic_value(state), None
    
    # Initialize best_move to None and best_value to a large negative number for the maximizing player
    # or a large positive number for the minimizing player
    best_move = None
    if naPotezu == "X":
        best_value = float("-inf")
        for move in get_valid_moves(state):
            # Make the move and recursively call minimax for the resulting state
            next_state = make_move(state, move)
            value, _ = minimax(next_state, depth - 1, alpha, beta)
            # Update the best value and best move if necessary
            if value > best_value:
                best_value = value
                best_move = move
            # Update alpha for alpha-beta pruning
            alpha = max(alpha, best_value)
            # If beta is less than or equal to alpha, prune the rest of the search tree
            if beta <= alpha:
                break
    else:
        best_value = float("inf")
        for move in get_valid_moves(state):
            # Make the move and recursively call minimax for the resulting state
            next_state = make_move(state, move)
            value, _ = minimax(next_state, depth - 1, alpha, beta)
            # Update the best value and best move if necessary
            if value < best_value:
                best_value = value
                best_move = move
            # Update beta for alpha-beta pruning
            beta = min(beta, best_value)
            # If beta is less than or equal to alpha, prune the rest of the search tree
            if beta <= alpha:
                break
    # Return the best value and the corresponding best move
    return best_value, best_move

# The game_over function returns True if the game is over, and False otherwise.
def game_over(state: List[List[str]]) -> bool:
    # Check if the board is full or if there are no more valid moves
    return all(cell != " " for row in state for cell in row) or not get_valid_moves(state)

# The get_valid_moves function returns a list of valid moves for the current player.
def get_valid_moves(state: List[List[str]]) -> List[Tuple[int, int]]:
    # If it is X's turn, check for empty pairs of adjacent cells in the same column
    if naPotezu == "X":
        return [(i, j) for i in range(brojVrsta - 1) for j in range(brojKolona) if state[i][j] == " " and state[i + 1][j] == " "]
    # If it is O's turn, check for empty pairs of adjacent cells in the same row
    else:
        return [(i, j) for i in range(brojVrsta) for j in range(brojKolona - 1) if state[i][j] == " " and state[i][j + 1] == " "]

# The make_move function takes in a game state and a move, and returns the new game state after the move has been made.
def make_move(state: List[List[str]], move: Tuple[int, int]) -> List[List[str]]:
    # Convert the move to zero-based indices
    i, j = brojVrsta - move[0] - 1, ord(move[1]) - ord("A")
    # If it is X's turn, fill in the two cells in the same column
    if naPotezu == "X":
        state[i][j] = "X"
        state[i + 1][j] = "X"
    # If it is O's turn, fill in the two cells in the same row
    else:
        state[i][j] = "O"
        state[i][j + 1] = "O"
    # Return the updated game state
    return state

# The heuristic_value function returns a heuristic value for the given game state.
def heuristic_value(state: List[List[str]]) -> int:
    # Count the number of X's and O's on the board
    x_count = 0
    o_count = 0
    for row in state:
        for cell in row:
            if cell == "X":
                x_count += 1
            elif cell == "O":
                o_count += 1
    # If X has more pieces, return a positive value
    if x_count > o_count:
        return x_count - o_count
    # If O has more pieces, return a negative value
    elif o_count > x_count:
        return x_count - o_count
    # If both players have the same number of pieces, return 0
    else:
        return 0

# The current_player function returns the player ("X" or "O") whose turn it is.
def current_player(state: List[List[str]]) -> str:
    # Count the number of X's and O's on the board
    x_count = sum(cell == "X" for row in state for cell in row)
    o_count = sum(cell == "O" for row in state for cell in row)
    # If the number of X's and O's is the same, it is X's turn
    if x_count == o_count:
        return "X"
    # If the number of X's is one more than the number of O's, it is O's turn
    elif x_count == o_count + 1:
        return "O"
    # If the number of X's and O's is not consistent, the game is over
    else:
        raise ValueError("Invalid game state")


def startStara():
    global kraj
    global matrica

    koIgraPrvi()
    init()
    stampaj(matrica)

    while True:
        if(krajIgre()):
            pobedio=""
            if(naPotezu=='X'):
                pobedio='O'
            else:
                pobedio='X'
            print("Kraj Igre, pobedio je igrac "+pobedio+"!!!")
            break


        print("\nIgrac "+naPotezu+" na potezu")
        print("Unesite vrstu (broj 1..N)(-1 prekid igre, -2 stampanje svih mogucih stanja):")
        vrsta = int(sys.stdin.readline())
        if vrsta == -1:
            break
        else:
            if vrsta == -2:
                svaMogucaStanja()
                print("Unesite vrstu (broj 1..N)(-1 prekid igre, -2 stampanje svih mogucih stanja):")
                vrsta = int(sys.stdin.readline())
                print("Unesite kolonu (slovo A..Z):")
                kolona = sys.stdin.readline()
                odigrajPotez(vrsta,kolona[0])
            else:
                print("Unesite kolonu (slovo A..Z):")
                kolona = sys.stdin.readline()
                odigrajPotez(vrsta,kolona[0])

# The start function initializes the game and runs the game loop.
def start():
    # Initialize the game
    koIgraPrvi()
    init()
    stampaj(matrica)

    # Set the search depth
    depth = 3

    # Run the game loop
    while True:
        if krajIgre():
            pobedio=""
            if naPotezu == "X":
                pobedio = "O"
            else:
                pobedio = "X"
            print("Kraj Igre, pobedio je igrac " + pobedio + "!!!")
            break

        # If it is the computer's turn, use the minimax algorithm to determine the best move
        if naPotezu == "O":
            value, move = minimax(matrica, depth, float("-inf"), float("inf"))
            print("Igrac " + naPotezu + " je odabrao potez:", move)
            odigrajPotez(move[0], move[1])
        else:
            print("\nIgrac " + naPotezu + " na potezu")
            print("Unesite vrstu (broj 1..N)(-1 prekid igre, -2 stampanje svih mogucih stanja):")
            vrsta = int(sys.stdin.readline())
            if vrsta == -1:
                break
            else:
                if vrsta == -2:
                    svaMogucaStanja()
                    print("Unesite vrstu (broj 1..N)(-1 prekid igre, -2 stampanje svih mogucih stanja):")
                    vrsta = int(sys.stdin.readline())
                    print("Unesite kolonu (slovo A..Z):")
                    kolona = sys.stdin.readline()
                    odigrajPotez(vrsta, kolona[0])
                else:
                    print("Unesite kolonu (slovo A..Z):")
                    kolona = sys.stdin.readline()
                    odigrajPotez(vrsta, kolona[0])

start()


