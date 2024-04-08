profession_prevision = input()
profession_daily = input()
profession_list = ["Medica - Estetoscopio,Esfigmomanometro,Jaleco,Caneta,Celular", "Assistente de Informatica - Calculadora,Oculos,Notebook,Camisa Social,Caderno",
                   "Padeira - Rolo,Caneta,Avental,Colher de Pau,Caderno", "Economista - Calculadora,Caneta,Camisa Social,Agenda,Celular", "Personal Trainer - Halter,Agenda,Celular,Legging,Corda"]
item_daily = []
barbie_bag = []

item_profession_daily = False
in_bag = False

for i in profession_list:
    profession_item = i.split(" - ")
    if profession_prevision == profession_item[0]:
        barbie_bag = profession_item[1].split(",")

    if profession_item[0] == profession_daily:
        item_daily = profession_item[1].split(",")

while True:
    action_input = input()
    in_bag = False
    item_profession_daily = False

    if action_input == "Adicionar":
        add_item = input()
        in_bag = add_item in barbie_bag
        item_profession_daily = add_item in item_daily

        if not in_bag and item_profession_daily:
            print(f"{add_item} adicionado à bolsa")
            barbie_bag.append(add_item)
        elif not item_profession_daily:
            print(
                f"Barbie, {add_item} não esta na lista de itens de {profession_daily}")
        elif in_bag:
            print(f"Barbie, você já colocou {add_item} na bolsa")

    elif action_input == "Retirar":
        remove_item = input()
        index_remove_item = 0
        in_bag = False
        item_profession_daily = False

        in_bag = remove_item in barbie_bag
        item_profession_daily = remove_item in item_daily

        if in_bag and not item_profession_daily:
            print(f"{remove_item} retirado da bolsa")
            barbie_bag.remove(remove_item)
        elif in_bag and item_profession_daily:
            print(
                f"Não faca isso Barbie, você precisa de {remove_item} para trabalhar de {profession_daily}")
        else:
            print("Barbie, como você vai retirar algo que já não esta ai?")

    elif action_input == "Sair":
        itens_in_order = sorted(barbie_bag)
        item_list_print = ", ".join(itens_in_order)
        print(f"Itens na bolsa: {item_list_print}")
        break


wrong_profission_bag_items = [
    item for item in barbie_bag if item not in item_daily]

# wrong_profission_bag_items = []
# for item i

correct_profission_bag_items = [
    item for item in item_daily if item in barbie_bag]

forgotten_item = [item for item in item_daily if item not in barbie_bag]

item_forgotten = False
if len(wrong_profission_bag_items) == 0:
    item_forgotten = len(barbie_bag) != len(item_daily)

if len(wrong_profission_bag_items) > 0 and not item_forgotten:
    print(
        f"Barbie, você esqueceu de tirar {', '.join(wrong_profission_bag_items)}, você não usa ele trabalhando de {profession_daily}")
elif item_forgotten:
    print(
        f"Oh não!! Barbie, você esqueceu de pegar {', '.join(forgotten_item)}!!")
else:
    print("Boa Barbie, foi na correria mas tudo deu certo!")
