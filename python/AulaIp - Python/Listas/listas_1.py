# leia um número inteiro N > 0
# Em seguida, leia N linhas contendo os nomes das criaturas. 
# O seu código deve imprimir os nomes das criaturas na ordem que apareceram, garantindo que cada nome de criatura apareça apenas uma vez na lista
# Caso sejam encontradas criaturas repetidas, uma mensagem deverá ser impressa para cada uma das criaturas repetidas

N_criaturas = int(input())
n_nomes = []
criaturas_registradas = 0
repitidos_nomes = 0
while N_criaturas>criaturas_registradas:
  nome_atual = input()
  n_nomes.append(nome_atual)
  criaturas_registradas+=1
  
  for nome in n_nomes:    
    if(nome_atual == nome):
      repitidos_nomes += 1

  if(repitidos_nomes>1):
    print("Criatura repetida")
    n_nomes.pop()
  repitidos_nomes = 0
    
for nome in n_nomes:
   print(nome)
