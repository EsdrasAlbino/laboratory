
#
number_verification = 0
contain_prefession = False
profession_not_speaking = 0
profession_out_list = ""
while True:
  barbie_options=input()
  contain_prefession=False
  profession_not_speaking=0

  if( barbie_options == "Meninas, acho que já falei demais. Vamos para o shopping?"):
     break
  
  profession_out_list=""
  print(f"Arara {number_verification}:")


  number_verification +=1
  list_profession_barbie = input().split(", ")
  list_profession_speaking = input().split(", ")

  if(len(list_profession_barbie) != len(list_profession_speaking)):
      print("Hmm, estranho! Acho que a Barbie se confundiu na organização e nas lembranças!")
  else:
    list_profession_barbie.sort()
    list_profession_speaking.sort()

    not_found = [profession_not_found for profession_not_found in list_profession_barbie if profession_not_found not in list_profession_speaking]
    number_not_found = len(not_found)

    if(number_not_found==0):
        print("Boa, Barbie! Não bagunçou nada, pode contar todas as suas histórias!")
    else:
        string_not_found = ', '.join(not_found)
        print(f"Poxa, Barbie! Você acabou desorganizando essa arara, e {number_not_found} profissões vão ficar de fora da conversa. São elas: {string_not_found}.")

  