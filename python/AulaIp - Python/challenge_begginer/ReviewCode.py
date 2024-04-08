nome = input()
total_pessoas = int(input())
coeficiente = float(input())
fumantesArredondado = 0

if (total_pessoas % 2 == 0):
    fumantes = coeficiente * (total_pessoas - 1) + 1

else:
    fumantes = coeficiente * (total_pessoas - 1) / 2
# vendo se o nr de pessoas é par ou ímpar e utilizando a formula adequada
fumantesDecimal = fumantes - int(fumantes)
# extraindo toda parte decimal do numero float de fumantes
umaCasaDecimalFumantes = int(((fumantesDecimal % 1) * 10) // 1)
# extraindo apenas a primeira casa decimal para arredondar
if (umaCasaDecimalFumantes >= 0 and umaCasaDecimalFumantes <= 5):
    fumantesArredondado = int(fumantes - umaCasaDecimalFumantes)
elif (umaCasaDecimalFumantes > 5 and umaCasaDecimalFumantes < 10):
    diferenca = 1 - umaCasaDecimalFumantes
    fumantesArredondado = int(fumantes + diferenca)
# arredondando o nr de fumantes
proporcao = int(fumantesArredondado * 100 / total_pessoas)
# proporcao de fumantes / nr pessoas *100 para porcentagem
print(f'Vamos verificar se {nome} vai fumar singaro!')
print(f'{proporcao}% dos seus amigos fumam singaro')
if (proporcao < 25):
    print('Você tem poucas chances de fumar singaro, fuma não pow, cuide da sua saúde')
elif (proporcao > 25 and proporcao < 50):
    print('Cuidado pra não fumar ein, fuma não pow, cuide da sua saúde')
else:
    print('TIRA ESSE SINGARO DA BOCA. FUMA NÃO POW, CUIDE DA SUA SAÚDE!')
# outputs
print(umaCasaDecimalFumantes)
