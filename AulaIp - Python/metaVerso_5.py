input_caracter_one = input()
input_caracter_two = input()
loved_person = input()
skill = input()
test_number_one = int(input())
test_number_two = int(input())
test_number_three = int(input())

if input_caracter_one == "Humildade" and input_caracter_two == "Bondade" and (loved_person == "Mary" or loved_person == "Ninguem") and (skill == "Dancar" or skill == "Lancar") and test_number_one >= 7 and test_number_two >= 7 and test_number_three >= 7:
    print("Siga em frente, olhe para o lado. Bem-vindo ao aranhaverso, Miranha Furacao!")
else:
    print("Ops, parece que não foi dessa vez, Miranha. Você terá que continuar na Carreta Furacao mesmo!")
    if input_caracter_one != "Humildade" or input_caracter_two != "Bondade":
        print("Infelizmente você não possui as característica necessárias!")
    elif loved_person != "Mary" and loved_person != "Ninguem":
        print("Infelizmente você não está apaixonado pela pessoa certa!")
    elif skill != "Dancar" and skill != "Lancar":
        print("Infelizmente você não possui as habilidades necessárias!")
    elif test_number_one < 7 or test_number_two < 7 or test_number_three < 7:
        print("Infelizmente você não obteve um bom desempenho escolar!")
