def evaluate(board):
    # Verifica todas as possíveis linhas, colunas e diagonais
    for i in range(3):
        # Checa linhas e colunas
        if board[i][0] == board[i][1] == board[i][2] != '_':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '_':
            return board[0][i]
        # Checa diagonais
        if board[0][0] == board[1][1] == board[2][2] != '_':
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != '_':
            return board[0][2]
    # Se não houver vencedor, retorna empate
    return '_'


def is_full(board):
    # Verifica se o tabuleiro está cheio
    for row in board:
        for cell in row:
            if cell == '_':
                return False
    return True


def minimax(board, depth, is_maximizing):
    result = evaluate(board)

    if result != '_':
        return result

    if is_full(board):
        return 'empate'

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'x'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = '_'
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'o'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = '_'
                    best_score = min(best_score, score)
        return best_score


def predict_winner(board):
    result = minimax(board, 0, True)
    if result == 'x':
        print("As previsões indicam que o resultado é vitória do x. Aperte o botão correspondente")
    elif result == 'o':
        print("As previsões indicam que o resultado é vitória do o. Aperte o botão correspondente")
    else:
        print(
            "As previsões indicam que o resultado é empate. Aperte o botão correspondente")


board = []
for _ in range(3):
    row = input().split("|")
    board.append(row)

# Chama a função para prever o vencedor
predict_winner(board)
