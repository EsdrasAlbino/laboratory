items_length, ballance = input().split(' ; ')
ballance = int(ballance)
items_length = int(items_length)
exited = 0
objects_price = list()

while exited == 0:
    barbie_actions = input()

    if barbie_actions == "Quero adicionar um item":
        item, item_cost = input().split(' , ')
        item_cost = int(item_cost)
        if (ballance - item_cost) >= 0 and (len(objects_price) <= items_length):
            ballance -= item_cost
            items_length -= 1
            print(f'Vá em frente, Ken! Você ainda tem {ballance} barbieCoins disponíveis')
            objects_price.append([item, item_cost])
        else:
            print('Avise a Barbie que isso não será possível.')
    elif barbie_actions == "Quero remover um item":
        object = input()
        founded = 0
        new_objects_price = list()
        for items in objects_price:
            if founded == 0 and object == items[0].split(' - ')[0]:
                print('Ok, Barbie!')
                ballance += items[1]
                founded = 1
                items_length += 1
                print(f"Ken, você ainda tem {ballance} barbieCoins disponíveis")
            else:
                new_objects_price.append(items)
        objects_price = new_objects_price

        if founded == 0:
            print("Barbie, infelizmente não consegui fazer isso.")
    elif barbie_actions == "Poderia me lembrar os itens que estão até então e de qual filme eles foram recuperados?":
        if len(objects_price) == 0:
            print("Por enquanto seu museu está vazio, Barbie. Vamos trabalhar nisso!")
        else:
            print('Claro!')
            for objects in objects_price:
                print(objects[0])
    else:
        print("Por nada! Estou sempre à disposição!")
        exited=1