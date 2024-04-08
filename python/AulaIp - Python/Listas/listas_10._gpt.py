


def cinema_game(voceY, voceX, cambistaY, cambistaX, pipocaY, pipocaX, barbieY, barbieX, oppenheimerY, oppenheimerX, directions):

    cinema = [['-' for _ in range(8)] for _ in range(8)]
    cinema[barbieY][barbieX] = 'B'
    cinema[oppenheimerY][oppenheimerX] = 'O'

    xV, yV = voceX, voceY
    xC, yC = cambistaX, cambistaY
    xP, yP = pipocaX, pipocaY

    pipoca_picked_up = False

    for direction in directions:
        cinema[yV][xV] = '-'
        if not pipoca_picked_up and (xV, yV) == (xP, yP):
            pipoca_picked_up = True

        if direction == 'cima':
            yV = max(yV - 1, 0)
        elif direction == 'baixo':
            yV = min(yV + 1, 7)
        elif direction == 'esquerda':
            xV = max(xV - 1, 0)
        elif direction == 'direita':
            xV = min(xV + 1, 7)

        cinema[yV][xV] = 'V'

        if not pipoca_picked_up and (xV, yV) == (xP, yP):
            pipoca_picked_up = True

        # Cambista movement
        if xC != xV:
            xC += 1 if xC < xV else -1
        elif yC != yV:
            yC += 1 if yC < yV else -1

        cinema[yC][xC] = 'C'
        distance = (xV - xC) ** 2 + (yV - yC) ** 2

        for row in cinema:
            print(' '.join(row))
        if pipoca_picked_up:
            print('Já peguei a pipoca')
        else:
            print('Ainda não achei a pipoca')

        if distance <= 3:
            print('Preciso acelerar, o cambista tá na minha cola!')
        elif 3 < distance <= 4:
            print('Consigo ver lá longe o cambista, mas é melhor acelerar!')
        else:
            print('O cambista está longe, mas não posso ficar parado')        print()

    if (xV, yV) == (barbieX, barbieY):
        print("A Margot Robbie está incrível, mas que barulho é esse vindo da sala do lado?")
    elif (xV, yV) == (oppenheimerX, oppenheimerY):
        print("Aí sim, que filmaço! Christopher Nolan nunca erra!")
    elif distance <= 0:
        print("Droga! Agora volto pra casa sem filme e sem dinheiro.")
    else:
        print("Ah não, vou passar fome! Não tem nem graça assistir filme sem uma pipoquinha.")
