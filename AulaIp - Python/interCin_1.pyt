

jogos = 0
vitoria_1 = 0
vitoria_2 = 0
vencendo_partida = ""
time_1 = input()
time_2 = input()

while jogos < 5:

    pontuação_do_time_1 = int(input())
    pontuação_do_time_2 = int(input())

    if pontuação_do_time_1 > pontuação_do_time_2:
        vitoria_1 += 1
        print(f"O vencedor da {jogos+1}ª rodada foi: {time_1}")
    else:
        vitoria_2 += 1
        print(f"O vencedor da {jogos+1}ª rodada foi: {time_2}")

    if vitoria_1 == 3:
        vencedor_partida = time_1
        jogos = 10
    elif vitoria_2 == 3:
        vencedor_partida = time_2
        jogos = 10

    jogos += 1

print(f"O time {vencedor_partida} ganhou a partida final!")
