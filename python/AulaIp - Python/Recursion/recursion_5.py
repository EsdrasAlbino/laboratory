def home_passed(number_homes):
    elements = []
    for i in range(number_homes):
        element = input().replace(" ", "").split("-")
        elements.append(element)
    return elements


def rescue_princess(homes, home_current, sword, visited):
    rupees_acumulated = 0
    recue = False
    princess = False
    next_home = 0

    home = homes[home_current]

    rupees_acumulated = sum([1 for i in home if i == '◇'])
    sword = sword or any("espada" in i for i in home)
    princess = any("Zelda" in i for i in home)

    if princess:
        enime = any("Agahnim" in i for i in home)
        if not enime or sword:
            recue = True
            return rupees_acumulated, recue

    next_home = next((i for i in home if i.isdigit()), None)
    if next_home is not None:
        next_home = int(next_home)
        if next_home < len(homes) and next_home not in visited:
            visited.add(home_current)
            rupees, recue = rescue_princess(homes, next_home, sword, visited)
            rupees_acumulated += rupees

    return rupees_acumulated, recue


def main():
    quantifed_home = int(input())
    elements = home_passed(quantifed_home)
    current_home = int(input())
    visited = set()  # Conjunto para acompanhar as salas visitadas
    visited.add(current_home)  # Adicionar a sala inicial ao conjunto
    rupees, rescue = rescue_princess(elements, current_home, False, visited)

    if rescue:
        print(
            f"A princesa Zelda está a salvo e ainda conseguimos coletar {rupees} rupees")
    else:
        print(
            f"Infelizmente a princesa ainda corre perigo, mas temos {rupees} rupees para nos ajudar nas buscas")


main()
