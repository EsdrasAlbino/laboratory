name_id = input()
number_person_arround = int(input())
number_random = float(input())

if number_person_arround % 2 == 0:
    result = number_random*(number_person_arround-1)+1
else:
    result = number_random*(number_person_arround-1)/2

first_number_float = int(((result % 1) * 10) // 1)

if first_number_float >= 0 and first_number_float <= 5:
    proportion_int = int(result)
else:
    proportion_int = int(result)+1

percentual_smoker = int((proportion_int/number_person_arround)*100)
print(f"Vamos verificar se {name_id} vai fumar singaro!")
print(f"{percentual_smoker}% dos seus amigos fumam singaro")

if percentual_smoker > 50:
    print("TIRA ESSE SINGARO DA BOCA. FUMA NÃO POW, CUIDE DA SUA SAÚDE!")
elif percentual_smoker < 50 and percentual_smoker > 25:
    print("Cuidado pra não fumar ein, fuma não pow, cuide da sua saúde")
else:
    print("Você tem poucas chances de fumar singaro, fuma não pow, cuide da sua saúde")
