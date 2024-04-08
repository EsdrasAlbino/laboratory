supposed_profission = input()
correct_profission = input()
profission_items_index = 0
supposed_profission_items_index = 0

if correct_profission == 'Medica':
    profission_items_index = 0
elif correct_profission == 'Assistente de Informatica':
    profission_items_index = 1
elif correct_profission == 'Padeira':
    profission_items_index = 2
elif correct_profission == 'Economista':
    profission_items_index = 3
else:
    profission_items_index = 4

if supposed_profission == 'Medica':
    supposed_profission_items_index = 0
elif supposed_profission == 'Assistente de Informatica':
    supposed_profission_items_index = 1
elif supposed_profission == 'Padeira':
    supposed_profission_items_index = 2
elif supposed_profission == 'Economista':
    supposed_profission_items_index = 3
else:
    supposed_profission_items_index = 4

doctor_items = ["Estetoscopio", "Esfigmomanometro", "Jaleco", "Caneta" , "Celular"]
it_items = ["Calculadora", "Oculos", "Notebook", "Camisa Social", "Caderno"]
baker_items = ["Rolo", "Caneta", "Avental", "Colher de Pau", "Caderno"]
economist_items = ["Calculadora", "Caneta", "Camisa Social", "Agenda", "Celular"]
personal_trainer_items = ["Halter", "Agenda", "Celular", "Legging", "Corda"]

profissions_items = [doctor_items, it_items, baker_items, economist_items, personal_trainer_items]
in_bag_items = profissions_items[supposed_profission_items_index]
exited = 0

while exited == 0:
    action = input()
    if action == 'Adicionar':
        to_add_item = input()
        if to_add_item in in_bag_items:
            print(f"Barbie, você já colocou {to_add_item} na bolsa")
        elif to_add_item in profissions_items[profission_items_index]:
            in_bag_items.append(to_add_item)
            print(f"{to_add_item} adicionado à bolsa")
        else:
            print(f"Barbie, {to_add_item} não esta na lista de itens de {correct_profission}")
    elif action == 'Retirar':
        to_remove_item = input()
        item_in_bag = to_remove_item in in_bag_items

        item_notin_profission = to_remove_item not in profissions_items[profission_items_index]
        if item_in_bag and item_notin_profission:
            print(f"{to_remove_item} retirado da bolsa")
            in_bag_items.pop(in_bag_items.index(to_remove_item))
        elif item_in_bag:
            print(f"Não faca isso Barbie, você precisa de {to_remove_item} para trabalhar de {correct_profission}")
        else:
            print('Barbie, como você vai retirar algo que já não esta ai?')

    else:
        exited = 1
        in_bag_items.sort()
        print(f"Itens na bolsa: {', '.join(in_bag_items)}")

wrong_profission_bag_items = list()
correct_profission_bag_items = list()

for item in in_bag_items:
    if item in profissions_items[profission_items_index]:
        correct_profission_bag_items.append(item)
    else:
        wrong_profission_bag_items.append(item)

missing_items = list()

for item in profissions_items[profission_items_index]:
    if item not in correct_profission_bag_items:
        missing_items.append(item)


only_correct_items = len(correct_profission_bag_items) == len(in_bag_items)
if len(missing_items) == 0 and only_correct_items:
    print("Boa Barbie, foi na correria mas tudo deu certo!")
elif only_correct_items:
    print(f"Oh não!! Barbie, você esqueceu de pegar {', '.join(missing_items)}!!")
else:
    print(f"Barbie, você esqueceu de tirar {', '.join(wrong_profission_bag_items)}, você não usa ele trabalhando de {correct_profission}")