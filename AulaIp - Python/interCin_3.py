garrafas = 20
voluntarios = 5

rodadas = True

while rodadas:
    frase = input()

    if (frase == 'O InterCIn acabou!!! Vamos ver nosso estoque de bebidas'):
        if (garrafas > 0):
            print(
                f"Notícia boa: sobraram {garrafas} garrafas, vamos guardar na geladeira :D")
        elif (garrafas == 0):
            print('Vendemos todas as águas, fizemos uma contagem certeira!!')
        else:
            print(f'Estamos devendo {garrafas*-1} garrafas para os alunos...')
        rodadas = False
    elif (frase == "Acabou uma partida e os alunos estão com MUITA sede, segue a quantidade de jogadores"):
        quantidade_jogadores = int(input())
        if (garrafas < quantidade_jogadores):
            garrafas_faltando = quantidade_jogadores-garrafas
            garrafas = garrafas*2
            print(
                f"Não teremos água para todos os jogadores... Temos que garantir {garrafas_faltando} garrafas!!")
            garrafas -= quantidade_jogadores
            if (garrafas < 0):
                print("Por questões logísticas, teremos que acabar com os jogos...")
                rodadas = False
        else:
            garrafas -= quantidade_jogadores
    elif (frase == "Encham o cooler, vai começar um jogo!!!!"):
        garrafas += 15
        print("Geladeira cheia!")
    elif (frase == "Timeout da partida, vamos ver quantas garrafas pediram a cada voluntário"):
        quantidade_1 = int(input())
        quantidade_2 = int(input())
        quantidade_3 = int(input())
        quantidade_4 = int(input())
        quantidade_5 = int(input())

        total_garrafas_solicitadas = quantidade_1 + \
            quantidade_2 + quantidade_3 + quantidade_4+quantidade_5
        garrafas -= total_garrafas_solicitadas
        if (garrafas < 0):
            print(f"Prometemos distribuir {garrafas*-1} garrafas e zeramos")
            print("Por questões logísticas, teremos que acabar com os jogos...")
            rodadas = False
