nome_aluno = input()
nome_professor = input()
vencedor_conhecido = False
partidas_aluno = 0
partidas_professor = 0
vencedor = ""
pontos_aluno = 0
pontos_professor = 0
partidas_jogadas = 0

print(f'E agora, só pela resenha:\nMelhor de 3 entre: {nome_aluno} e {nome_professor}!\nCOMEÇOU!')

while partidas_jogadas<=3 or not vencedor_conhecido:
  num = int(input())
  
  if(num % 2 == 0):
    pontos_professor +=1
  else:
    pontos_aluno +=1
    
  print(f'{pontos_aluno} - {pontos_professor}')
  
  if pontos_professor >= 11 and pontos_professor >= pontos_aluno+2:
    vencedor = nome_professor
    partidas_professor += 1
    print(f'{vencedor} ganhou esta partida!')
    print(f'Placar: {nome_aluno} [{partidas_aluno}-{partidas_professor}] {nome_professor}')
    pontos_aluno = 0
    pontos_professor = 0

    if partidas_professor ==2:
      vencedor_conhecido = True
      print('FIM DA SÉRIE!')
      print(f'{nome_professor} ganhou a série! A experiência ganhou!')
  elif pontos_aluno>= 11 and pontos_aluno >= pontos_professor+2:
    vencedor = nome_aluno
    partidas_aluno +=1
    print(f'{vencedor} ganhou esta partida!')
    print(f'Placar: {nome_aluno} [{partidas_aluno}-{partidas_professor}] {nome_professor}')
    pontos_aluno = 0
    pontos_professor = 0
    if partidas_aluno == 2:
      vencedor_conhecido = True
      print('FIM DA SÉRIE!')
      print(f'{nome_aluno} ganhou a série! Puro talento!')
    

    
  partidas_jogadas+=1


    
