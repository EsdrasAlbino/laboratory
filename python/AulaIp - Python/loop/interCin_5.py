jogos = int(input())
jogos_realizados = 0
soma_pontos_spicin = 0
soma_pontos_manchester= 0
pontos_totais = 0
porcentagem = 0
vencedor = ""
aposta_segura = True

while jogos_realizados<jogos:
  soma_pontos=0
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
  
  pontos_totais += soma_pontos
  
  
  if(nome_time == "Manchester CIn"):
    soma_pontos_manchester+=soma_pontos
  else:
    soma_pontos_spicin+=soma_pontos
    
  if(soma_pontos_spicin>soma_pontos_manchester):
    vencedor = "SpiCIn Girls"
    divisao_porcentagem = soma_pontos_spicin/pontos_totais
    porcentagem = divisao_porcentagem*100
  else:
    vencedor = "Manchester CIn"
    divisao_porcentagem = soma_pontos_manchester/pontos_totais
    porcentagem = divisao_porcentagem*100
  
  if(soma_pontos_manchester<0):
    jogos_realizados = jogos+1
    aposta_segura = False
    print(f"O time Manchester CIn ficou com pontuação negativa. A aposta não é segura, podemos perder nosso dinheiro.")
  elif(soma_pontos_spicin<0):
    jogos_realizados = jogos+1
    aposta_segura = False
    print(f"O time SpiCIn Girls ficou com pontuação negativa. A aposta não é segura, podemos perder nosso dinheiro.")
    
  jogos_realizados +=1
    
  
if aposta_segura:
  print(f"Com {porcentagem:.2f}% dos pontos, o time {vencedor} pode garantir nosso dinheiro na CInBet, é uma das grandes apostas do InterCIn.")