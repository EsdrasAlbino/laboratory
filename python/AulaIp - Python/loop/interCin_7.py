qnt_partidas = int(input())
partidas_jogadas = 0
rodadas_jogadas = 0
rodadas_ganhas_ip = 0
rodadas_ganhas_adver = 0
perdeu = False
goleada = False
final = False

while qnt_partidas>partidas_jogadas:
  rodadas_ganhas_ip = 0
  rodadas_ganhas_adver = 0
  rodadas_jogadas = 0
  qnt_rodadas = int(input())
  if(partidas_jogadas+1<qnt_partidas):
    print(f"Vai começar a {partidas_jogadas+1}º partida. Esse jogo terá {qnt_rodadas} rodada(s).")
  else:
    print(f"Tá na hora da grande final! Esse jogo terá {qnt_rodadas} rodada(s).")
    final = True
  while qnt_rodadas>rodadas_jogadas:
    habilidade_ip = int(input())
    habilidade_adver = int(input())
    
    if(habilidade_ip == habilidade_adver or habilidade_ip>habilidade_adver):
      rodadas_ganhas_ip += 1
    else:
      rodadas_ganhas_adver+=1
      
    rodadas_jogadas+=1
  print(f"Fim de jogo! O placar foi {rodadas_ganhas_ip}x{rodadas_ganhas_adver}")
  
  if((rodadas_ganhas_ip == rodadas_ganhas_adver or rodadas_ganhas_ip<rodadas_ganhas_adver) and not final):
    print("Não foi dessa vez! Treinar pro ano que vem!")
    partidas_jogadas=qnt_partidas+1
    perdeu = True
  elif (partidas_jogadas<qnt_partidas and rodadas_ganhas_ip>=rodadas_ganhas_adver+5) and not final:
    print("QUE GOLEADAAAA!!! Essa vitória fez os outros times desistirem e a equipe de IP/P1 é a campeã!")
    goleada = True
    partidas_jogadas=qnt_partidas+1
  elif not final:
    print("Vamos para próxima fase!")
  if not goleada:
    if(not perdeu and final):
      if(rodadas_ganhas_ip == rodadas_ganhas_adver or rodadas_ganhas_ip<rodadas_ganhas_adver):
        print("Ah não!! Chegaram tão longe mas não foi dessa vez. :(")
      else:
        print("É CAMPEÃO! O TIME DE IP/P1 GARANTIU A TAÇA!")
  
  partidas_jogadas+=1