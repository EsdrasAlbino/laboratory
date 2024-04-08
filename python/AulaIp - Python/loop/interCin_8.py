equipe1_nome1 = input()
equipe1_nome2 = input()
equipe2_nome1 = input()
equipe2_nome2 = input()
quantidade_partidas = int(input())
partidas_jogadas = 0
pontos_totais_equipe1 = 0
pontos_totais_equipe2 = 0
pontos_totais_da_disputa = 0
vitoria_equipe1 = 0
vitoria_equipe2 = 0
desistencia = False

nome_vencedor1 = ""
nome_vencedor2 = ""
quantidade_total_de_pontos_da_dupla = 0
quantidade_de_vitorias = 0

print(f"VAMO VER QUEM VAI COMER GRAMA! TEREMOS {quantidade_partidas} PARTIDAS ENTRE:")
print(f"{equipe1_nome1} e {equipe1_nome2} X {equipe2_nome1} e {equipe2_nome2}")

while quantidade_partidas>partidas_jogadas:
  pontos_equipe1 = int(input())
  pontos_equipe2 = int(input())
  
  pontos_totais_equipe1 += pontos_equipe1
  pontos_totais_equipe2 += pontos_equipe2
  
  pontos_totais_da_disputa = pontos_totais_equipe1+pontos_totais_equipe2
  
  if pontos_equipe1>=pontos_equipe2:
    vitoria_equipe1 += 1
  else:
    vitoria_equipe2 += 1
    
  
  if pontos_equipe1 == 0:
    print("JOGO ENCERRADO POR DESISTÊNCIA DA EQUIPE 1, QUE VERGONHA")
    partidas_jogadas = quantidade_partidas +1
    desistencia = True
  elif pontos_equipe2 == 0:
    print("JOGO ENCERRADO POR DESISTÊNCIA DA EQUIPE 2, QUE VERGONHA")
    partidas_jogadas = quantidade_partidas+1
    desistencia = True

  
  
  partidas_jogadas += 1
if not desistencia:
   coeficiente_dupla1 = pontos_totais_equipe1*(vitoria_equipe1/quantidade_partidas) 
   coeficiente_dupla2 = pontos_totais_equipe2*(vitoria_equipe2/quantidade_partidas)
   
   if coeficiente_dupla1>= coeficiente_dupla2:
     nome_vencedor1 = equipe1_nome1
     nome_vencedor2 = equipe1_nome2
     quantidade_total_de_pontos_da_dupla = pontos_totais_equipe1
     quantidade_de_vitorias = vitoria_equipe1
   else:
     nome_vencedor1 = equipe2_nome1
     nome_vencedor2 = equipe2_nome2
     quantidade_total_de_pontos_da_dupla = pontos_totais_equipe2
     quantidade_de_vitorias = vitoria_equipe2
   print(f"CARAMBA! Tivemos um total de {pontos_totais_da_disputa} bolas ao chão ao longo dessa disputa.\n{nome_vencedor1} e {nome_vencedor2} são os grandes vencedores!\nMataram {quantidade_total_de_pontos_da_dupla} bolas, ganhando {quantidade_de_vitorias} partidas")