# return shape (disqualified, end_condition, next_condition, thrusters)
def character_race_processing(character_name, thrusters, situation):
    end_boolean = False
    next_boolean = False
    disqualified = False

    pit_stop_situation = "Pit-Stop Espacial"
    droide_trouble_situation = "Um Droide apareceu do nada na pista, do nadaaa! Perdi o controle e bati em uma pedra."
    droide_character_situation = "Opa esse participante tem ID de Droide, desclassificando em 3, 2, 1..."
    next_character_situation = "Próximo"

    if situation == pit_stop_situation:
        thrusters += 1
    elif situation == droide_trouble_situation:
        thrusters -= 1
    elif situation == droide_character_situation:
        print(
            f"O {character_name} achou que não descobriríamos, tirem {character_name} imediatamente da pista.")
        next_boolean = True
        disqualified = True
    elif situation == next_character_situation:
        next_boolean = True
    else:
        end_boolean = True

    if thrusters <= 0:
        print(f"BUUMM!! Infelizmente, {character_name} está fora da corrida.")
        disqualified = True
        next_boolean = True

    return disqualified, end_boolean, next_boolean, thrusters


qualified = disqualified = 0
end_condition = next_condition = character_disqualified = False

while not end_condition:
    next_condition = character_disqualified = False
    inputed = input().split(' ')
    if inputed != ['FIM']:
        character_name, thrusters, thruster_velocity = inputed
        thrusters = int(thrusters)
        initial_thrusters = thrusters
        thruster_velocity = int(thruster_velocity)
        while not next_condition and not end_condition:
            situation = input()
            character_disqualified, end_condition, next_condition, thrusters = character_race_processing(character_name,
                                                                                                         thrusters,
                                                                                                         situation)
        if not character_disqualified:
            print(f"--- Participante: {character_name} ---")
            print(f"Qtd de propulsores Final: {thrusters}")
            print(
                f"Velocidade Inicial: {initial_thrusters * thruster_velocity} km/h")
            print(f"Velocidade Final: {thrusters * thruster_velocity} km/h")
            qualified += 1
        else:
            disqualified += 1
    else:
        end_condition = True

if qualified >= 1:
    print(
        f"Relatório da CIn Pod Race: {qualified} participantes terminaram a corrida e {disqualified} foram desclassificados.")
else:
    print("NÃO! Esses Droides me pagam, sabotaram minha corrida!")
