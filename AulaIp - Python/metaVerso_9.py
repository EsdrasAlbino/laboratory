#Venom não morre caso ele e o druida morrer

vida_venom = int(input())
ataque_venom = int(input())
pocao_venom = int(input())
vida_creeper = int(input())
vida_druida = int(input())
ataque_druida = int(input())
ataque_creeper = ataque_venom

vida_maxima_venom = vida_venom
venceu_turno_um = False


morte_venom = 0 

# Turno 1
print(f"SENHORAS E SENHORES! AGORA O VENOM ENFRENTARÁ O CREEPER!")
vida_venom = vida_venom-ataque_creeper
vida_creeper = vida_creeper-ataque_venom

venom_morto = vida_venom<=0
creeper_morto = vida_creeper<=0

if(venom_morto or creeper_morto):
  if(venom_morto and not creeper_morto):
      print("O venom não tankou e foi de base...")
      print("AH NÃO! O VENOM PEGOU EM BOMBA!")
      morte_venom=morte_venom+1
      venceu_turno_um = False

  elif(creeper_morto and not venom_morto):
    print("O creeper não tankou e foi de base...")
    print("Isso aí! Ele é todo esquentadinho, mas no final deu tudo certo!")
    venceu_turno_um = True
  else:
    print("O venom não tankou e foi de base...")
    print("O creeper não tankou e foi de base...")
    print("AH NÃO! O VENOM PEGOU EM BOMBA!")

    morte_venom=morte_venom+1
    venceu_turno_um = False
    
elif (not creeper_morto and not venom_morto):
  print(f"Vida atual do Venom: {vida_venom}\nDano sofrido pelo Venom: {ataque_creeper}\nVida atual do creeper: {vida_creeper}\nDano sofrido pelo creeper: {ataque_venom}")
  if(ataque_creeper>ataque_venom):
    print("AH NÃO! O VENOM PEGOU EM BOMBA!")
    morte_venom=morte_venom+1
    venceu_turno_um = False
  elif(ataque_venom>ataque_creeper):
    print("Isso aí! Ele é todo esquentadinho, mas no final deu tudo certo!")
    venceu_turno_um = True
  elif(ataque_creeper == ataque_venom):
    if(vida_creeper>vida_venom):
        print("AH NÃO! O VENOM PEGOU EM BOMBA!")
        morte_venom=morte_venom+1

        venceu_turno_um = False

    elif (vida_venom>vida_creeper):
        print("Isso aí! Ele é todo esquentadinho, mas no final deu tudo certo!")
        venceu_turno_um = True
    elif(vida_venom==vida_creeper):
        print("AH NÃO! O VENOM PEGOU EM BOMBA!")
        morte_venom=morte_venom+1

        venceu_turno_um = False

vida_com_pocao = vida_venom+pocao_venom
if(vida_maxima_venom>=vida_com_pocao and not venom_morto and venceu_turno_um):
  print("Ah! Essa poção é da boa!")
  vida_venom=vida_venom+pocao_venom


  

#Turno 2
if venceu_turno_um:
    print(f"SENHORAS E SENHORES! AGORA O VENOM ENFRENTARÁ O DRUIDA!")
    if(vida_maxima_venom>=vida_venom+pocao_venom):
      vida_venom=vida_venom+pocao_venom
    else:
      envenenamento = (vida_venom+pocao_venom)-vida_maxima_venom
      ataque_druida = ataque_druida + envenenamento
      vida_venom=vida_maxima_venom

    vida_venom = vida_venom-ataque_druida
    vida_druida = vida_druida-ataque_venom

    venom_morto = vida_venom<=0
    druida_morto = vida_druida<=0



    if(venom_morto or druida_morto):
      if(venom_morto and not druida_morto):
          print("O venom não tankou e foi de base...")
          print("Pelo visto a poção tava fora do prazo de validade :(")
          morte_venom=morte_venom+1
          venceu_turno_um = False
 
      elif(druida_morto and not venom_morto):
        print("O druida não tankou e foi de base...")
        print("Quase me dei mal, nunca mais aceito nada de estranho...")
        venceu_turno_um = True
      else:
          print("O venom não tankou e foi de base...")
          print("O druida não tankou e foi de base...")
          print("Pelo visto a poção tava fora do prazo de validade :(")

          morte_venom=morte_venom+1
          venceu_turno_um = False
      

    if (not druida_morto and not venom_morto):
       print(f"Vida atual do Venom: {vida_venom}\nDano sofrido pelo Venom: {ataque_druida}\nVida atual do druida: {vida_druida}\nDano sofrido pelo druida: {ataque_venom}")
       if(ataque_druida>ataque_venom):
          print("Pelo visto a poção tava fora do prazo de validade :(")
          morte_venom=morte_venom+1

          venceu_turno_um = False
       elif(ataque_venom>ataque_druida):
            print("Quase me dei mal, nunca mais aceito nada de estranho...")
       elif(ataque_druida == ataque_venom):
            if(vida_druida>vida_venom):
                print("Pelo visto a poção tava fora do prazo de validade :(")
                morte_venom=morte_venom+1
                venceu_turno_um = False
            elif (vida_venom>vida_druida):
                print("Quase me dei mal, nunca mais aceito nada de estranho...")
                venceu_turno_um = True
            elif(vida_venom==vida_druida):
                print("Pelo visto a poção tava fora do prazo de validade :(")
                venceu_turno_um = False
                morte_venom=morte_venom+1

if venceu_turno_um:
   print("Essa aventura foi epicamente épica, meu amigo! Boa viagem aí! * Começa a tocar saxofone *")
else:
   print("Pelo visto as aventuras do Miles terminaram por aqui...")
