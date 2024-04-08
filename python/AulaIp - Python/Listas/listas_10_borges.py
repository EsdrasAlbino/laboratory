me_Y = int(input())
me_X = int(input())
cambista_Y = int(input())
cambista_X = int(input())
popcorn_Y = int(input())
popcorn_X = int(input())
barbie_Y = int(input())
barbie_X = int(input())
oppenheimer_Y = int(input())
oppenheimer_X = int(input())

destroyed_popcorn = 0
taked_popcorn = 0
eating_popcorn = 0

exited = 0
position_matrix = []
matrix_size = 8
while exited == 0:

    if cambista_X == me_X:
        if cambista_Y > me_Y:
            cambista_Y -= 1
        elif cambista_Y < me_Y:
            cambista_Y += 1
    else:
        if cambista_X > me_X:
            cambista_X -= 1
        elif cambista_X < me_X:
            cambista_X += 1
    
    if cambista_Y == popcorn_Y and cambista_X == popcorn_X and destroyed_popcorn == 0:
        destroyed_popcorn = 1
    
    if me_Y == cambista_Y and me_X == cambista_X:
        exited = 1
        position_matrix = [['-' for i in range(matrix_size)] for j in range(matrix_size)]
        if taked_popcorn == 0 and destroyed_popcorn == 0:
            position_matrix[popcorn_Y][popcorn_X] = 'P'
        position_matrix[barbie_Y][barbie_X] = 'B'
        position_matrix[oppenheimer_Y][oppenheimer_X] = 'O'
        position_matrix[me_Y][me_X] = 'V'
        position_matrix[cambista_Y][cambista_X] = 'C'

        for row in position_matrix:
            print(' '.join(row))
        print('Droga! Agora volto pra casa sem filme e sem dinheiro.')
        
    else:
        move_direction = input()
        if eating_popcorn != 1:
            if move_direction == 'esquerda':
                me_X -= 1
            elif move_direction == 'cima':
                me_Y -= 1
            elif move_direction == 'direita':
                me_X += 1
            else:
                me_Y += 1

        position_matrix = [['-' for i in range(matrix_size)] for j in range(matrix_size)]
        if taked_popcorn == 0 and destroyed_popcorn == 0:
            position_matrix[popcorn_Y][popcorn_X] = 'P'
        position_matrix[barbie_Y][barbie_X] = 'B'
        position_matrix[oppenheimer_Y][oppenheimer_X] = 'O'
        position_matrix[me_Y][me_X] = 'V'
        position_matrix[cambista_Y][cambista_X] = 'C'

        for row in position_matrix:
            print(' '.join(row))
        
        if me_Y == barbie_Y and me_X == barbie_X:
            exited = 1
            if taked_popcorn == 0:
                print('Ah não, vou passar fome! Não tem nem graça assistir filme sem uma pipoquinha.')
            else:
                print('A Margot Robbie está incrível, mas que barulho é esse vindo da sala do lado?')
        elif me_Y == oppenheimer_Y and me_X == oppenheimer_X:
            exited = 1
            if taked_popcorn == 0:
                print('Ah não, vou passar fome! Não tem nem graça assistir filme sem uma pipoquinha.')
            else:
                print('Aí sim, que filmaço! Christopher Nolan nunca erra!')
        elif me_Y == cambista_Y and me_X == cambista_X:
            exited = 1
            print('Droga! Agora volto pra casa sem filme e sem dinheiro.')
        elif taked_popcorn == 1:
            print('Já peguei a pipoca')
            eating_popcorn = 0
        else:
            if me_Y == popcorn_Y and me_X == popcorn_X and destroyed_popcorn == 0:
                taked_popcorn = 1
                eating_popcorn = 1
                print('Finalmente! Peguei a pipoca')
            else:
                print('Ainda não achei a pipoca')

        if exited == 0:
            distance = ((me_Y - cambista_Y)**2 + (me_X - cambista_X)**2)**0.5
            if distance <= 3:
                print(f'Preciso acelerar, o cambista tá na minha cola!\n')
            elif distance <= 4:
                print(f'Consigo ver lá longe o cambista, mas é melhor acelerar!\n')
            else:
                print(f'O cambista está longe, mas não posso ficar parado\n')