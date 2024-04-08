def check_winner(board, player):
    # Verifica se o jogador 'player' ganhou nas linhas, colunas ou diagonais
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False


def predict_result(board, player):
    # Verifica se o jogador atual venceu
    if check_winner(board, player):
        return f"vitória do {player}"

    # Verifica se é empate
    if all(cell != '_' for row in board for cell in row):
        return "empate"

    # Caso contrário, simula todas as jogadas possíveis do próximo jogador
    next_player = 'x' if player == 'o' else 'o'
    results = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                new_board = [row[:] for row in board]
                new_board[i][j] = player
                result = predict_result(new_board, next_player)
                results.append(result)

    # Retorna o melhor resultado para o jogador atual
    if player == 'x':
        return max(results, key=lambda r: 'x' in r)
    else:
        return min(results, key=lambda r: 'o' in r)


board = [list(input().split("|")) for _ in range(3)]
player = 'x' if sum(row.count('x') for row in board) <= sum(
    row.count('o') for row in board) else 'o'

# Chamada da função de previsão e impressão do resultado
result = predict_result(board, player)
print(
    f"As previsões indicam que o resultado é {result}. Aperte o botão correspondente")
