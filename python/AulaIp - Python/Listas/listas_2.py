itens_list_date = input().split(', ')
itens_list_comparation = input().split(', ')
number_itens_list = 0
number_itens_in_home = 0
itens_in_home = []


for item_list in itens_list_date:
  number_itens_list += 1
  for item_comparation in itens_list_comparation:
    if(item_list == item_comparation):
      itens_in_home.append(item_list)
      number_itens_in_home += 1
      

if(number_itens_in_home == 0):
  print(f"Nossa, irei ao shopping agora mesmo! Não tenho nenhum dos {number_itens_list} itens em casa.")
elif (number_itens_list == number_itens_in_home):
  print("Esses são os itens que já tenho em casa:")
  for index,item_home in enumerate(itens_in_home):
    print(f"{index+1}º item: {item_home}")
  print(f"Que ótimo, consegui encontrar cada um dos {number_itens_list} itens!")
else:
  print("Esses são os itens que já tenho em casa:")
  for index,item_home in enumerate(itens_in_home):
    print(f"{index+1}º item: {item_home}")
  print(f"Irei precisar comprar {number_itens_list-number_itens_in_home} itens antes do meu encontro!")
  

print("Isso é tudo! Hora de me preparar!")