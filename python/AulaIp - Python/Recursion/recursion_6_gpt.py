def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))


def eliminate_lines(matrix):
    n = len(matrix)
    m = len(matrix[0])
    eliminated = 0
    new_matrix = [['O' for _ in range(m)] for _ in range(n)]
    for i in range(n-1, -1, -1):
        if 'X' not in matrix[i]:
            eliminated += 1
        else:
            new_matrix[i] = matrix[i]
    return new_matrix, eliminated


def drop_blocks(matrix):
    n = len(matrix)
    m = len(matrix[0])
    new_matrix = [['O' for _ in range(m)] for _ in range(n)]
    for j in range(m):
        col = [matrix[i][j] for i in range(n)]
        new_col = [c for c in col if c != 'O']
        new_col = ['O'] * (n - len(new_col)) + new_col
        for i in range(n):
            new_matrix[i][j] = new_col[i]
    return new_matrix


def calculate_score(N, lines_eliminated):
    return (N ** 2) * max(N, lines_eliminated)


def add_block(matrix, row, col, block):
    n = len(matrix)
    m = len(matrix[0])
    if 0 <= row < n and 0 <= col < m and matrix[row][col] == 'O':
        matrix[row][col] = block


def main():
    N = int(input())
    matrix = [list(input()) for _ in range(N)]

    while True:
        line = input()
        if line == "sair":
            break
        row, col, block = line.split(',')
        row = int(row)
        col = int(col)
        add_block(matrix, row, col, block)

    while True:
        new_matrix, lines_eliminated = eliminate_lines(matrix)
        if lines_eliminated == 0:
            break
        matrix = drop_blocks(new_matrix)

    total_score = 0
    for _ in range(N):
        total_score += calculate_score(N, lines_eliminated)

    print("Resultado:")
    print_matrix(matrix)
    print(f"Pontuação: {total_score}")


if __name__ == "__main__":
    main()
