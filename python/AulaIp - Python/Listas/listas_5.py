#N que representa ao mesmo tempo quantos andares tem a mansão e quantos cômodos cabem em cada andar:
N = int(input())
tamanho_comodo_anda = []
per_N_builder = ""
list_per_N_builder = []
count = 0
count_room = 0
while N>count:
  while N>count_room:
    input_room = int(input())
    if count_room+1 == N:
       per_N_builder += str(input_room)
    else:
      per_N_builder += str(input_room)+" " 
    count_room +=1
  tamanho_comodo_anda.append(per_N_builder)
  per_N_builder = ""
  count+=1
  count_room=0


for i in tamanho_comodo_anda:
    print(i)

  