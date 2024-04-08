

def predict_winner():
    


def main():
    input_board = []
    for _ in range(3):
        row = input().split("|")
        input_board.append(row)
    
    winner = predict_winner(input_board)
    if winner == "empate":
        print("As previsões indicam que o resultado é empate. Aperte o botão correspondente")
    else:
        print(f"As previsões indicam que o resultado é vitória do {winner}. Aperte o botão correspondente")