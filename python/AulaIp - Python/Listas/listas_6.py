object_spending = input()
objects = []
N_objects = int(object_spending.split(" ; ")[0])
spending_object_limit = int(object_spending.split(" ; ")[1])

while True:
    barbie_action = input()
    
    if barbie_action == "Quero adicionar um item":
        more_object = input()
        object_add = more_object.split(" - ")[0]
        spending_object_add = int(more_object.split(" , ")[1])

        if (spending_object_limit-spending_object_add) >=0 and len(objects)<=N_objects:
            spending_object_limit -= spending_object_add

            print(f"Vá em frente, Ken! Você ainda tem {spending_object_limit} barbieCoins disponíveis")
            objects.append(more_object)
            N_objects -= 1

          
        else:
            print("Avise a Barbie que isso não será possível.")

    elif barbie_action == "Quero remover um item":
        remove_object = input()
        getItem = 0
        for idx, i in enumerate(objects):
            objectt = i.split(" - ")[0]
            spending = int(i.split(" , ")[1])
            if objectt == remove_object and getItem ==0:
                objects.pop(idx)
                spending_object_limit += spending
                N_objects += 1
                getItem=1
                print("Ok, Barbie!")
                print(f"Ken, você ainda tem {spending_object_limit} barbieCoins disponíveis")
                break
        if getItem == 0:
                print("Barbie, infelizmente não consegui fazer isso.")

    elif barbie_action == "Poderia me lembrar os itens que estão até então e de qual filme eles foram recuperados?":
        if len(objects) == 0:
            print("Por enquanto seu museu está vazio, Barbie. Vamos trabalhar nisso!")
        else:
            print("Claro!")
            for i in objects:
                item = i.split(" - ")[0]
                filme = i.split(" - ")[1].split(" , ")[0]
                print(f"{item} - {filme}")
    else:
        print("Por nada! Estou sempre à disposição!")
        break

