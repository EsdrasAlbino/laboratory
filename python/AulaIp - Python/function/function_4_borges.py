def astronaut_survive_explosion(astronaut_coordinate, explosion_coordinate, impact_radius):
    return ((astronaut_coordinate[0] - explosion_coordinate[0])**2 + (astronaut_coordinate[1] - explosion_coordinate[1])**2)**0.5 > impact_radius


def astronaut_rescue(capsule, explosion_coordinate, impact_radius):
    survived_astronaut = list()
    for astronaut in capsule:
        if astronaut_survive_explosion(astronaut, explosion_coordinate, impact_radius):
            survived_astronaut.append(astronaut)

    return survived_astronaut


def capsule_center(capsule):
    capsule_x_axis = list()
    capsule_y_axis = list()

    for astronaut in capsule:
        capsule_x_axis.append(astronaut[0])
        capsule_y_axis.append(astronaut[1])

    return [sum(capsule_x_axis)/len(capsule_x_axis), sum(capsule_y_axis)/len(capsule_y_axis)]


capsules = eval(input())
explosion_coordinate = eval(input())
impact_radius = float(input())

survived_astronauts = 0
capsule_centers = list()
for capsule in capsules:
    survived_list = astronaut_rescue(
        capsule, explosion_coordinate, impact_radius)
    if len(survived_list):
        survived_astronauts += len(survived_list)
        capsule_centers.append(capsule_center(survived_list))

print([survived_astronauts, capsule_centers])
