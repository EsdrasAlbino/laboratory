def alpha_beta_search(board, free_spaces, maximizing=True, alpha=float('-inf'), beta=float('inf')):
    game_condition = check_game_over(board)

    if game_condition[0] or free_spaces == 0:
        return evaluate_position(game_condition)

    best_value = float('-inf') if maximizing else float('inf')
    player = 'x' if maximizing else 'o'

    if maximizing:
        best_value = float('-inf')
        player = 'x'
        for move_board in get_available_moves(board, player):
            value = alpha_beta_search(
                move_board, free_spaces - 1, False, alpha, beta)
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break
    else:
        best_value = float('inf')
        player = 'o'
        for move_board in get_available_moves(board, player):
            value = alpha_beta_search(
                move_board, free_spaces - 1, True, alpha, beta)
            best_value = min(best_value, value)
            beta = min(beta, best_value)
            if beta <= alpha:
                break

    return best_value


def check_game_over(board):
    def transpose_matrix(matrix):
        return [[matrix[j][i] for j in range(3)] for i in range(3)]

    for board_ in [board, transpose_matrix(board)]:
        for col_idx in range(3):
            if all(board_[col_idx][i] != '_' and board_[col_idx][i] == board_[col_idx][0] for i in range(1, 3)):
                return True, board_[col_idx][0]

    if board[0][0] != '_' and board[0][0] == board[1][1] == board[2][2]:
        return True, board[0][0]
    elif board[0][2] != '_' and board[0][2] == board[1][1] == board[2][0]:
        return True, board[0][2]

    return False, None


def evaluate_position(condition):
    return 1 if condition[0] and condition[1] == 'x' else -1 if condition[0] and condition[1] == 'o' else 0


def get_available_moves(board, player='x'):
    moves = []
    for col in range(3):
        for row in range(3):
            if board[col][row] == '_':
                new_board = [row[:] for row in board]
                new_board[col][row] = player
                moves.append(new_board)
    return moves


def main():
    input_board = [input().split("|") for _ in range(3)]
    x_count = sum(row.count('x') for row in input_board)
    o_count = sum(row.count('o') for row in input_board)
    is_max = x_count <= o_count
    depth = sum(1 for col in input_board for item in col if item == '_')
    result = alpha_beta_search(
        input_board, depth, is_max)

    if result == 0:
        print("Empate previsto. Pressione o botão correspondente.")
    else:
        if result == 1:
            print(
                f"Vitória prevista para x. Pressione o botão correspondente.")
        else:
            print(
                f"Vitória prevista para o. Pressione o botão correspondente.")


main()
