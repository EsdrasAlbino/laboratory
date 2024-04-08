def analisar_araras():
    numero_arara = 0
    while True:
        acao = input()
        if acao == "Meninas, acho que já falei demais. Vamos para o shopping?":
            break

        arara_barbie = input().split(', ')
        arara_falada = input().split(', ')

        print(f"Arara {numero_arara}:")
        numero_arara += 1

        if len(arara_barbie) != len(arara_falada):
            print("Hmm, estranho! Acho que a Barbie se confundiu na organização e nas lembranças!")
        else:
            encontrados = [profissao for profissao in arara_falada if profissao in arara_barbie]
            nao_encontrados = [profissao for profissao in arara_barbie if profissao not in arara_falada]
            total_nao_encontrados = len(nao_encontrados)
            if total_nao_encontrados == 0:
                print("Boa, Barbie! Não bagunçou nada, pode contar todas as suas histórias!")
            else:
                nao_encontrados_str = ', '.join(nao_encontrados)
                print(f"Poxa, Barbie! Você acabou desorganizando essa arara, e {total_nao_encontrados} profissões vão ficar de fora da conversa. São elas: {nao_encontrados_str}.")


# Teste dos casos de exemplo
analisar_araras()
