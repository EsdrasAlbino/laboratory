def make_board(sample):
    return [['' if item == '_' else item for item in row.split('|')] for row in sample]


def game_over(board):
    def transpose_3x3_matrix(matrix):
        return [[matrix[j][i] for j in range(3)] for i in range(3)]

    for board_ in [board, transpose_3x3_matrix(board)]:
        for col_idx in range(3):
            if all(board_[col_idx][i] != '' and board_[col_idx][i] == board_[col_idx][0] for i in range(1, 3)):
                return True, board_[col_idx][0]

    if board[0][0] != '' and board[0][0] == board[1][1] == board[2][2]:
        return True, board[0][0]
    elif board[0][2] != '' and board[0][2] == board[1][1] == board[2][0]:
        return True, board[0][2]

    return False,


def evaluate_board(state):
    return 1 if state[0] and state[1] == 'x' else -1 if state[0] and state[1] == 'o' else 0


def get_possible_moves(board, player='x'):
    moves_board_list = []
    for col in range(3):
        for row in range(3):
            if board[col][row] == '':
                move_board = [row[:] for row in board]
                move_board[col][row] = player
                moves_board_list.append(move_board)
    return moves_board_list


def get_freedom_degrees(board):
    return sum(1 for col in board for item in col if item == '')


def alpha_beta_minimax(board, freedom_degrees, maximizing=True, alpha=float('-inf'), beta=float('inf')):
    game_state = game_over(board)
    # print('------')
    # print(f"\n".join([" ".join(row) for row in board]))
    if game_state[0] or freedom_degrees == 0:
        return evaluate_board(game_state)

    best_eval = float('-inf') if maximizing else float('inf')
    player = 'x' if maximizing else 'o'

    game_state = game_over(board)
    if game_state[0] or freedom_degrees == 0:
        return evaluate_board(game_state)

    if maximizing:
        best_eval = float('-inf')
        player = 'x'
        for move_board in get_possible_moves(board, player):
            eval = alpha_beta_minimax(
                move_board, freedom_degrees - 1, False, alpha, beta)
            best_eval = max(best_eval, eval)
            alpha = max(alpha, best_eval)
            if beta <= alpha:
                break
    else:
        best_eval = float('inf')
        player = 'o'
        for move_board in get_possible_moves(board, player):
            eval = alpha_beta_minimax(
                move_board, freedom_degrees - 1, True, alpha, beta)
            best_eval = min(best_eval, eval)
            beta = min(beta, best_eval)
            if beta <= alpha:
                break

    return best_eval


def x_curr_player(board):
    x_count = sum(row.count('x') for row in board)
    o_count = sum(row.count('o') for row in board)
    return x_count <= o_count


sample_board = make_board([input() for _ in range(3)])

result = alpha_beta_minimax(sample_board, get_freedom_degrees(
    sample_board), x_curr_player(sample_board))
if result == 0:
    print("As previsões indicam que o resultado é empate. Aperte o botão correspondente")
else:
    winner = 'x' if result == 1 else 'o'
    print(
        f"As previsões indicam que o resultado é vitória do {winner}. Aperte o botão correspondente")
