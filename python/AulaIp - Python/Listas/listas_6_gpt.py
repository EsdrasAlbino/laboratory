def main():
    # Inicialização das variáveis
    max_items, max_cost = map(int, input().split(';'))
    barbie_coins = max_cost
    museum = []

    while True:
        action = input().strip()

        if action == "Quero adicionar um item":
            item_data = input().strip().split(' - ')
            item_name, item_film, item_cost = item_data[0], item_data[1], int(item_data[2])

            if len(museum) < max_items and barbie_coins >= item_cost:
                museum.append((item_name, item_film, item_cost))
                barbie_coins -= item_cost
                print(f"Vá em frente, Ken! Você ainda tem {barbie_coins} barbieCoins disponíveis")
            else:
                print("Avise a Barbie que isso não será possível.")

        elif action == "Quero remover um item":
            item_to_remove = input().strip()

            found = False
            for item in museum:
                if item[0] == item_to_remove:
                    barbie_coins += item[2]
                    museum.remove(item)
                    found = True
                    break

            if found:
                print(f"Ok, Barbie!\nKen, você ainda tem {barbie_coins} barbieCoins disponíveis")
            else:
                print("Barbie, infelizmente não consegui fazer isso.")

        elif action == "Poderia me lembrar os itens que estão até então e de qual filme eles foram recuperados?":
            if museum:
                print("Claro!")
                for i, item in enumerate(museum):
                    print(f"item {i} - {item[1]}")
            else:
                print("Por enquanto seu museu está vazio, Barbie. Vamos trabalhar nisso!")

        elif action == "Fim! Muito obrigada pela ajuda!!":
            print("Por nada! Estou sempre à disposição!")
            break

if __name__ == "__main__":
    main()
