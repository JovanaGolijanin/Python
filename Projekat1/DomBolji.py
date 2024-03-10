from asyncio.windows_events import INFINITE
from json.encoder import INFINITY

BOARD_SIZE = 8

# Initialize the board
board = []
for i in range(BOARD_SIZE):
    row = []
    for j in range(BOARD_SIZE):
        row.append(0)
    board.append(row)

def draw_board():
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == 0:
                print(".", end="")
            elif board[i][j] == 1:
                print("X", end="")
            else:
                print("O", end="")
        print()

def get_possible_moves(board, player):
    moves = []
    if player == 1:
        # Player 1 can place a horizontal domino
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE-1):
                if board[i][j] == 0 and board[i][j+1] == 0:
                    moves.append((i, j, i, j+1))
    else:
        # Player 2 can place a vertical domino
        for i in range(BOARD_SIZE-1):
            for j in range(BOARD_SIZE):
                if board[i][j] == 0 and board[i+1][j] == 0:
                    moves.append((i, j, i+1, j))
    return moves

def make_move(board, move, player):
    x1, y1, x2, y2 = move[0], move[1], move[2], move[3]
    board[x1][y1] = player
    board[x2][y2] = player

def game_over(board):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == 0:
                return False
    return True

def evaluate(board):
    score = 0
    # Add some points for each vertical domino that player 1 has placed
    for i in range(BOARD_SIZE-1):
        for j in range(BOARD_SIZE):
            if board[i][j] == 1 and board[i+1][j] == 1:
                score += 1
    # Subtract some points for each horizontal domino that player 2 has placed
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE-1):
            if board[i][j] == 2 and board[i][j+1] == 2:
                score -= 1
    return score

def minimax(state, depth, alpha, beta, player):
    if player == "max":
        best = [-1, -1, -1, -1, -INFINITE]
    else:
        best = [-1, -1, -1, -1, +INFINITY]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, -1, -1, score]

    for move in get_possible_moves(state, player):
        x1, y1, x2, y2 = move[0], move[1], move[2], move[3]
        state[x1][y1] = player
        state[x2][y2] = player
        score = minimax(state, depth - 1, alpha, beta, -player)
        state[x1][y1] = 0
        state[x2][y2] = 0
        score[0], score[1], score[2], score[3] = x1, y1, x2, y2

        if player == "max":
            if score[4] > best[4]:
                best = score
            alpha = max(alpha, score[4])
        else:
            if score[4] < best[4]:
                best = score
            beta = min(beta, score[4])

        if beta <= alpha:
            break

    return best

def play_game():
    player = 1
    while not game_over(board):
        draw_board()
        print("Player", player)
        moves = get_possible_moves(board, player)
        if not moves:
            print("No moves available")
            break
        # Use minimax to choose a move
        move = minimax(board, 5, -INFINITE, +INFINITY, player)
        make_move(board, move, player)
        player = -player

play_game()
