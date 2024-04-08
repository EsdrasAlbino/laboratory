# Recebo 4 input que seguem o seguinte formato: opcao_1 - opcao_2 - ... - opcao_n
# Elas contém as opções que vamos considerar para cada uma das seções (penteado, top, bottom e sapatos)
# após receber as opções -> print("Triagem das peças realizada com sucesso, pronta para iniciar mesclagem!")

# Em seguida você receberá a quantidade de vezes e a direção em que cada seção irá girar, da seguinte forma: 
# x> y< z< w> (se > gira para direita | se < gira para esquerda)
# Depois de receber as informações para a mesclagem -> print("Iniciando mesclagem...")

  #o meio de cada seção pode ser diferente um dos outros e para as seções com um número par de opções, considerar a posição à direita (a posição com maior índice) mais próxima ao meio como a área de foco inicial
  #você deve simular o movimento circular das seções, logo, considere o 1° elemento como o sucessor do último e o último como o antecessor do 1°.

# Ao final da mesclagem -> print print("O look gerado foi: cabelo {opcao_penteado}, {opcao_top} com {opcao_bottom} e {opcao_sapato} nos pés.")
# Quando parar de girar será recebido uma das strings 
# Amei!! ou 
# Acho que não combinou muito :/ ou 
# Melhor escolher eu mesma

# Para o código quando a barbie gostar de um look ou desistir da máquina

# Quando a máquina não estiver sendo mais usada e se Barbie tenha gostado do look e o top seja a camisa da seleção -> print ("Essa Barbie vai torcer pela seleção feminina na copa do mundo 2023!")
# Caso ela tenha gostado do look e esteja vestindo qualquer outro top -> print("Essa Barbie vai arrasar com o look perfeito!")
# Caso ela tenha desistido -> print("Acho que estou precisando de ajustes, Ken :(")

item_option_hairstyle = input().split(" - ")
item_option_top = input().split(" - ")
item_option_bottom = input().split(" - ")
item_option_sneakers = input().split(" - ")
print("Triagem das peças realizada com sucesso, pronta para iniciar mesclagem!")
all_item = [item_option_hairstyle]+[item_option_top]+[item_option_bottom]+[item_option_sneakers]
index_in_focus = ["","","",""]

while True:
  wheel_quantificator = input().split(" ")
  print("Iniciando mesclagem...")
  itens_select=[]

  for idx, i in enumerate(wheel_quantificator):
    not_match_item=True
    index_select = 0
    right = False
    left = False
    quantify_whell = 0
    wheeling = 0
    direction = wheel_quantificator[idx].partition(">")[1]
    
    if direction == ">":
      right=True
      quantify_whell = int(wheel_quantificator[idx].partition(">")[0])

    else:
      left= True
      quantify_whell = int(wheel_quantificator[idx].partition("<")[0])
      quantify_whell *= -1

    item_of_idx = all_item[idx]
    if str(index_in_focus[idx]) == "":
      index_in_focus[idx] = (len(item_of_idx))
      if index_in_focus[idx] % 2 ==0:
        index_in_focus[idx] = int(index_in_focus[idx]/2)
      else:
        index_in_focus[idx] = int(index_in_focus[idx]//2)
    
    index_in_focus[idx] += quantify_whell

    index_in_focus[idx] = index_in_focus[idx]%len(item_of_idx)

    itens_select.append(item_of_idx[index_in_focus[idx]])
    
  print(f"O look gerado foi: cabelo {itens_select[0]}, {itens_select[1]} com {itens_select[2]} e {itens_select[3]} nos pés.")

  decisition_end_barbie = input()
  
  if decisition_end_barbie == "Acho que não combinou muito :/" or decisition_end_barbie == "Amei!!":
      if decisition_end_barbie == "Amei!!":
          if itens_select[1] =="camisa da seleção":
              print ("Essa Barbie vai torcer pela seleção feminina na copa do mundo 2023!")
          else:
              print("Essa Barbie vai arrasar com o look perfeito!")
          break;
        #continue
  else:
    print("Acho que estou precisando de ajustes, Ken :(")
    break;

  
  