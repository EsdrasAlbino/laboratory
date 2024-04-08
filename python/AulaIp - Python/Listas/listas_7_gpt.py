def check_items(profissao_do_dia, bolsa):
    for item in bolsa:
        if item not in profissao_do_dia:
            return item
    return None

def main():
    profissao_prevista = input()
    profissao_do_dia = input()

    bolsa = []
    profissao_prevista_itens = {
        "Medica": ["Estetoscopio", "Esfigmomanometro", "Jaleco", "Caneta", "Celular"],
        "Assistente de Informatica": ["Calculadora", "Oculos", "Notebook", "Camisa Social", "Caderno"],
        "Padeira": ["Rolo", "Caneta", "Avental", "Colher de Pau", "Caderno"],
        "Economista": ["Calculadora", "Caneta", "Camisa Social", "Agenda", "Celular"],
        "Personal Trainer": ["Halter", "Agenda", "Celular", "Legging", "Corda"]
    }

    profissao_do_dia_itens = profissao_prevista_itens.get(profissao_do_dia, [])
    profissao_prevista_itens_copy = profissao_prevista_itens[profissao_prevista].copy()

    while True:
        acao = input()
        if acao == "Sair":
            bolsa.sort()
            items_na_bolsa = ", ".join(bolsa)
            if len(bolsa) == len(profissao_do_dia_itens) and all(item in profissao_do_dia_itens for item in bolsa):
                print("Itens na bolsa:", items_na_bolsa)
                print("Boa Barbie, foi na correria mas tudo deu certo!")
            else:
                item_esquecido = check_items(profissao_do_dia_itens, bolsa)
                if item_esquecido:
                    print(f"Oh não!! Barbie, você esqueceu de pegar {item_esquecido}!!")
                else:
                    item_errado = check_items(bolsa, profissao_do_dia_itens_copy)
                    print(f"Barbie, você esqueceu de tirar {item_errado}, você não usa ele trabalhando de {profissao_do_dia}")
            break
        elif acao.startswith("Adicionar"):
            item = acao.split()[1]
            if item in profissao_do_dia_itens:
                print(f"{item} adicionado à bolsa")
                bolsa.append(item)
            else:
                print(f"Barbie, {item} não esta na lista de itens de {profissao_do_dia}")
        elif acao.startswith("Retirar"):
            item = acao.split()[1]
            if item in bolsa:
                if item in profissao_do_dia_itens:
                    print(f"Não faca isso Barbie, você precisa de {item} para trabalhar de {profissao_do_dia}")
                else:
                    print(f"{item} retirado da bolsa")
                    bolsa.remove(item)
            else:
                print("Barbie, como você vai retirar algo que já não esta ai?")

if __name__ == "__main__":
    main()
