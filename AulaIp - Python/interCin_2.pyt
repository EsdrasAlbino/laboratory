n = int(input())
condicao_loop = 0
pontuacao_vencedor = 0
vencedor = ""

while condicao_loop < n:
    nome_jogador = input()
    pontuacao_total = int(input())
    penalidades_recebidas = int(input())
    pontuacao_final = pontuacao_total - penalidades_recebidas

    if (condicao_loop == 0):
        vencedor = nome_jogador
        pontuacao_vencedor = pontuacao_final
    else:
        if pontuacao_vencedor < pontuacao_final:
            vencedor = nome_jogador
            pontuacao_vencedor = pontuacao_final

    condicao_loop += 1


print(
    f"O grande vencedor do torneio foi {vencedor} com um total de {pontuacao_vencedor} pontos!")
