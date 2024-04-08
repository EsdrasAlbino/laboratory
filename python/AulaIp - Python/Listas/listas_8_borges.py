clothes_combination_matrix = list()
for i in range(4):
    clothes_combination_matrix.append(input().split(' - '))
print("Triagem das peças realizada com sucesso, pronta para iniciar mesclagem!")

exited = 0

saved_index = ['','','','']
while exited == 0:
    moves = input().split(' ')
    print("Iniciando mesclagem...")
    clothes_combination = list()
    for i in range(4):
        moves[i] = list(moves[i])
        direction = moves[i].pop()
        move_module = int(''.join(moves[i]))
        if direction == '<':
            move_module *= -1
        if saved_index[i] == '':
            saved_index[i] = len(clothes_combination_matrix[i])
            if saved_index[i] % 2 == 0:
                saved_index[i] = saved_index[i] / 2
            else:
                saved_index[i] = saved_index[i] // 2
        saved_index[i] += move_module
        saved_index[i] = int(saved_index[i] % len(clothes_combination_matrix[i]))
            
        clothes_combination.append(clothes_combination_matrix[i][saved_index[i]])
    print(f'O look gerado foi:\ncabelo {clothes_combination[0]}, {clothes_combination[1]} com {clothes_combination[2]} e {clothes_combination[3]} nos pés.')

    barbies_decision = input()

    if barbies_decision == 'Amei!!':
        if clothes_combination[1] == 'camisa da seleção':
            print("Essa Barbie vai torcer pela seleção feminina na copa do mundo 2023!")
        else:
            print("Essa Barbie vai arrasar com o look perfeito!")
        exited = 1
    elif barbies_decision == 'Melhor escolher eu mesma':
        print("Acho que estou precisando de ajustes, Ken :(")
        exited=1