# Cada elo tem uma pontuação, desde que o jogador tenha sido aceitado no time

# Se uma lane estiver ocupada, outro jogador n poderá entrar nela


# Se Bruna aparecer, acabou o programa
# Se Arthur aparecer, seu time perdeu
# Se Frej aparecer, seu time ganhou
# Se Frej e Arthur aparecer juntos, seus efeitos são cancelados

# Para saber se você vai ganhar do time adversário, será visto a pontuação do seu time, caso seja maior ou igual à do inimigo, você ganhar
# O inimigo sempre vai ter 18 pontos
pontuacao_time = 0
pontuacao_adversario = 18
top = False
jg = False
mid = False
adc = False
sup = False
jogadores = 0
jogador_um = ""
lane_jogador_um = ""
elo_jogador_um = ""
jogador_dois = ""
lane_jogador_dois = ""
elo_jogador_dois = ""
jogador_tres = ""
lane_jogador_tres = ""
elo_jogador_tres = ""
jogador_quatro = ""
lane_jogador_quatro = ""
elo_jogador_quatro = ""
jogador_cinco = ""
lane_jogador_cinco = ""
elo_jogador_cinco = ""
time_completo = True

while jogadores < 5:
    nome_jogador = input()
    if nome_jogador == "Bruna":
        print("LOL NÃO!!! TUDO MENOS LOL!!!")
        time_completo = False
        break

    lane_jogador = input()
    elo_jogador = input()

    if elo_jogador != "Bronze" and elo_jogador != "Prata" and elo_jogador != "Ouro" and elo_jogador != "Platina" and elo_jogador != "Diamante" and elo_jogador != "Desafiante":
        print("Não conheço esse elo, então vou considerar que é um elo ruim.")

    if lane_jogador == "Top" and top or lane_jogador == "Jungler" and jg or lane_jogador == "Mid" and mid or lane_jogador == "Adc" and adc or lane_jogador == "Suporte" and sup:
        print(f"{nome_jogador} não foi aceito, que pena.")
    else:
        print(f"{nome_jogador} entrou pro time.")
        jogadores += 1
        if nome_jogador == "Artur":
            print("Ele tá meio enferrujado...")
        elif nome_jogador == "Frej":
            print("Joga muito!")

        if elo_jogador == "Bronze":
            pontuacao_time += 1
        elif elo_jogador == "Prata":
            pontuacao_time += 2
        elif elo_jogador == "Ouro":
            pontuacao_time += 4
        elif elo_jogador == "Platina":
            pontuacao_time += 6
        elif elo_jogador == "Diamante":
            pontuacao_time += 8
        else:
            pontuacao_time += 10

        if lane_jogador == "Top":
            top = True
        elif lane_jogador == "Jungler":
            jg = True
        elif lane_jogador == "Mid":
            mid = True
        elif lane_jogador == "Adc":
            adc = True
        else:
            sup = True

        if (jogadores == 1):
            jogador_um = nome_jogador
            lane_jogador_um = lane_jogador
            elo_jogador_um = elo_jogador
        elif jogadores == 2:
            jogador_dois = nome_jogador
            lane_jogador_dois = lane_jogador
            elo_jogador_dois = elo_jogador
        elif jogadores == 3:
            jogador_tres = nome_jogador
            lane_jogador_tres = lane_jogador
            elo_jogador_tres = elo_jogador
        elif jogadores == 4:
            jogador_quatro = nome_jogador
            lane_jogador_quatro = lane_jogador
            elo_jogador_quatro = elo_jogador
        else:
            jogador_cinco = nome_jogador
            lane_jogador_cinco = lane_jogador
            elo_jogador_cinco = elo_jogador

if time_completo:

    print("O time está completo.")
    print(f"{jogador_um} - {lane_jogador_um} ({elo_jogador_um})")
    print(f"{jogador_dois} - {lane_jogador_dois} ({elo_jogador_dois})")
    print(f"{jogador_tres} - {lane_jogador_tres} ({elo_jogador_tres})")
    print(f"{jogador_quatro} - {lane_jogador_quatro} ({elo_jogador_quatro})")
    print(f"{jogador_cinco} - {lane_jogador_cinco} ({elo_jogador_cinco})")

    if (pontuacao_time < pontuacao_adversario):
        print("Vai dar ruim...")
    else:
        print("A GENTE VAI GANHAR!!!")
