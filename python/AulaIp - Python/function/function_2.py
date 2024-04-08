
def Situations(situation_in_race, quantify, name):
    user_disqualified = []
    disqualified = next_user = show_user = False

    if situation_in_race == "Pit-Stop Espacial":
        quantify += 1
        disqualified = False
        next_user = False
        show_user = True
    elif situation_in_race == "Um Droide apareceu do nada na pista, do nadaaa! Perdi o controle e bati em uma pedra.":
        quantify -= 1
        disqualified = False
        next_user = False
        show_user = True
        if quantify <= 0:
            print(f"BUUMM!! Infelizmente, {name} está fora da corrida.")
            user_disqualified.append(name)
            next_user = True
            disqualified = True
            show_user = False

    elif situation_in_race == "Opa esse participante tem ID de Droide, desclassificando em 3, 2, 1...":
        print(
            f"O {name} achou que não descobriríamos, tirem {name} imediatamente da pista.")
        user_disqualified.append(name)
        disqualified = True
        next_user = True
        show_user = False
    elif situation_in_race == "Próximo":
        disqualified = False
        next_user = True
        show_user = True
    else:
        disqualified = True
        next_user = False
        show_user = True
    return disqualified, quantify, next_user, user_disqualified, show_user


def Main():
    disqualifies = next_user = show_user = False
    qualifies_users = []
    disqualifies_users = []

    while not disqualifies or next_user:
        disqualifies = next_user = False
        name = ""
        name_quantify_speed = input().split(' ')

        if name_quantify_speed != ['FIM']:
            name, quantify, speed_initial = name_quantify_speed
            quantify, speed_initial = int(quantify), int(speed_initial)
            quantify_initial = quantify

            speed = speed_initial
            while not next_user and not disqualifies:
                situation_in_race = input()

                disqualifies, quantify, next_user, list_user_disqualify, show_user = Situations(
                    situation_in_race, quantify, name)
                if (len(list_user_disqualify) > 0):
                    disqualifies_users.append(list_user_disqualify)

            if show_user:
                speed_initial = quantify_initial*speed
                speed = quantify*speed
                print(
                    f"--- Partipante: {name} ---\nQtd de propulsores Final: {quantify}\nVelocidade Inicial: {speed_initial} km/ h\nVelocidade Final: {speed} km/h")
                qualifies_users.append(name)
            if situation_in_race == "FIM":
                disqualifies = True
        else:
            disqualifies = True
    if len(qualifies_users) > 0:
        x = len(qualifies_users)
        y = len(disqualifies_users)
        print(
            f"Relatório da CIn Pod Race: {x} participantes terminaram a corrida e {y} foram desclassificados.")
    else:
        print("NÃO! Esses Droides me pagam, sabotaram minha corrida!")


Main()
