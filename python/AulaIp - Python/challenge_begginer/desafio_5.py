jogos = int(input())
jogos_realizados = 0
soma_pontos_spicin = 0
soma_pontos_manchester= 0
porcentagem = 0
vencedor = ""

while jogos_realizados<jogos:
  nome_time = input()
  numeros_gols = int(input())
  numeros_chute_gol = int(input())
  numeros_cartao_amarelo = int(input())
  numeros_cartao_vermelho = int(input())
  
  pontos_gol = numeros_gols*10
  pontos_chute_gol = numeros_chute_gol*3
  pontos_cartao_amarelo = numeros_cartao_amarelo*2
  pontos_cartao_vermelho = numeros_cartao_vermelho*4
  
  soma_pontos = pontos_gol+pontos_chute_gol-(pontos_cartao_amarelo+pontos_cartao_vermelho)
  
  if(numeros_gols>=(numeros_chute_gol*0.3)):
    soma_pontos+=3
    
  if(numeros_cartao_vermelho>=numeros_cartao_amarelo):
    soma_pontos-=3
    
  if(soma_pontos<0):
    jogos_realizados = jogos+1
    print(f"O time {nome_time} ficou com pontuação negativa. A aposta não é segura, podemos perder nosso dinheiro.")
  
  if(nome_time == "Manchester CIn"):
    soma_pontos_manchester+=soma_pontos
  else:
    soma_pontos_spicin+=soma_pontos
  
  if(soma_pontos_spicin>soma_pontos_manchester):
    vencedor = "SpiCIn Girls"
    if soma_pontos_manchester != 0:
       porcentagem = (soma_pontos_manchester/(soma_pontos_manchester+soma_pontos_spicin))
  else:
    vencedor = "Manchester CIn"
    if soma_pontos_spicin != 0:
       porcentagem = (soma_pontos_spicin/(soma_pontos_manchester+soma_pontos_spicin))
  
  jogos_realizados +=1
    
  

print(f"Com {porcentagem:.2f}% dos pontos, o time {vencedor} pode garantir nosso dinheiro na CInBet, é uma das grandes apostas do InterCIn.")