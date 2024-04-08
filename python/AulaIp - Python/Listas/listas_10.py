me = [[int(input())],[int(input())]]
cambista = [[int(input())], [int(input())]]
popcorn = {'position': (int(input()), int(input()))}
barbie = {'position': (int(input()), int(input()))}
oppenheimer = {'position': (int(input()), int(input()))}

matrix_size = 8
destroyed_popcorn = False
taked_popcorn = False
eating_popcorn = False
exited = False

while not exited:
    position_matrix = [['-' for _ in range(matrix_size)] for _ in range(matrix_size)]

    if cambista['position'][1] == me[0][1]:
        if cambista['position'][0] > me[0][0]:
            y, x = cambista['position']

            if 'cima' == 'cima' and y > 0:
                y -= 1

            cambista['position'] = y, x
        elif cambista['position'][0] < me[0][0]:

            y, x = cambista['position']

            if 'baixo' == 'baixo' and y < matrix_size - 1:
                y += 1
            cambista['position'] = y, x
    else:
        if cambista['position'][1] > me[0][1]:

            y, x = cambista['position']
            if 'esquerda' == 'esquerda' and x > 0:
                x -= 1

            cambista['position'] = y, x
        elif cambista['position'][1] < me[0][1]:

            y, x = cambista['position']

            if 'direita' == 'direita' and x < matrix_size - 1:
                x += 1

            cambista['position'] = y, x

    if cambista['position'] == popcorn['position'] and not destroyed_popcorn:
        destroyed_popcorn = True

    if me['position'] == cambista['position']:
        exited = True
        position_matrix[popcorn['position'][0]][popcorn['position'][1]] = 'P' if not taked_popcorn else '-'
        position_matrix[barbie['position'][0]][barbie['position'][1]] = 'B'
        position_matrix[oppenheimer['position'][0]][oppenheimer['position'][1]] = 'O'
        position_matrix[me['position'][0]][me['position'][1]] = 'V'
        position_matrix[cambista['position'][0]][cambista['position'][1]] = 'C'

        for row in position_matrix:
            print(' '.join(row))
        if not taked_popcorn and not destroyed_popcorn:
            print('Droga! Agora volto pra casa sem filme e sem dinheiro.')
        else:
            if me['position'] == barbie['position']:
                print('A Margot Robbie está incrível, mas que barulho é esse vindo da sala do lado?')
            elif me['position'] == oppenheimer['position']:
                print('Aí sim, que filmaço! Christopher Nolan nunca erra!')
            else:
                print('Ah não, vou passar fome! Não tem nem graça assistir filme sem uma pipoquinha.')
    else:
        move_direction = input()

        if not eating_popcorn:

            y, x = me['position']
            if move_direction == 'esquerda' and x > 0:
                x -= 1
            elif move_direction == 'cima' and y > 0:
                y -= 1
            elif move_direction == 'direita' and x < matrix_size - 1:
                x += 1
            elif move_direction == 'baixo' and y < matrix_size - 1:
                y += 1
             me['position'] = y, x

        position_matrix[popcorn['position'][0]][popcorn['position'][1]] = 'P' if not taked_popcorn else '-'
        position_matrix[barbie['position'][0]][barbie['position'][1]] = 'B'
        position_matrix[oppenheimer['position'][0]][oppenheimer['position'][1]] = 'O'
        position_matrix[me['position'][0]][me['position'][1]] = 'V'
        position_matrix[cambista['position'][0]][cambista['position'][1]] = 'C'

        for row in position_matrix:
            print(' '.join(row))

        if me['position'] == barbie['position'] or me['position'] == oppenheimer['position']:
            exited = True
            if not taked_popcorn:
                print('Ah não, vou passar fome! Não tem nem graça assistir filme sem uma pipoquinha.')
            else:
                print('A Margot Robbie está incrível, mas que barulho é esse vindo da sala do lado?')
        elif taked_popcorn:
            print('Já peguei a pipoca')
            eating_popcorn = False
        else:
            if me['position'] == popcorn['position'] and not destroyed_popcorn:
                taked_popcorn = True
                eating_popcorn = True
                print('Finalmente! Peguei a pipoca')
            else:
                print('Ainda não achei a pipoca')

        if not exited:
            y1, x1, y2, x2 = me['position'][0], me['position'][1], cambista['position'][0], cambista['position'][1]

            distance = ((y1 - y2) ** 2 + (x1 - x2) ** 2) ** 0.5

            if distance <= 3:
                print('Preciso acelerar, o cambista tá na minha cola!\n')
            elif distance <= 4:
                print('Consigo ver lá longe o cambista, mas é melhor acelerar!\n')
            else:
                print('O cambista está longe, mas não posso ficar parado\n')
