N = int(input())
M = int(input())
somaExata = False
lista_tempo = []
matriz = []

for i in range(M):
    posicao_e_minutos_realizados = []
    entrada = input().split(' ')
    posicao = entrada[0]
    minutos_realizados = entrada[1]
    posicao_e_minutos_realizados.append(posicao)
    posicao_e_minutos_realizados.append(minutos_realizados)
    matriz.append(posicao_e_minutos_realizados)
    lista_tempo.append(minutos_realizados)


int_minutos_realizados = [int(elemento) for elemento in lista_tempo]


for i in range(len(int_minutos_realizados)):
    posicoes_Soma = []
    soma = 0
    for j in range(i, len(int_minutos_realizados)):
        soma += int_minutos_realizados[j]
        posicoes_Soma.append(matriz[j][0])

        if soma == N:
            somaExata = True
            break
    if somaExata:
        break

if somaExata:
    posicoes_Print = ' '.join(posicoes_Soma)
    print(
        f'Conquistamos nossa primeira estrela! Barbie e Chelsea arrasaram nos treinos das {posicoes_Print}!')
else:
    print('Não treinamos na dose certa e infelizmente a estrela vai ter que ficar para a próxima')
