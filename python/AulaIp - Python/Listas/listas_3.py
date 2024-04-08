number_colection = int(input())
colection_listed=0
sum_pointings = 0
eliminated = False
while number_colection> colection_listed:
  sum_pointings= 0
  average_poitings = 0
  n_colections = input().split(", ")
  n_pointings = input().split(", ")
  
  for index, coletion in enumerate(n_colections):
    sum_pointings += int(n_pointings[index])
    if coletion == "colete preto" or coletion == "coturno":
      print(f"{coletion} é uma peça muito gótica, não faz o estilo da Glimmer.")
      eliminated = True
      break;
    elif coletion == "vestido com babados" or coletion =="blusa bufante":
      print(f"{coletion} é uma peça muito antiquada, infelizmente essa coleção não vai servir...")
      eliminated = True
      break;
    if index+1 == len(n_colections):
      average_poitings = sum_pointings/len(n_colections)
      if(average_poitings<6):
        print("Até que as peças são bonitinhas, mas não o bastante. Essa coleção não vai servir.")
      else:
        print("Que coleção linda! Com certeza vai ajudar Glimmer a se inspirar.")

     
  
  colection_listed+=1
