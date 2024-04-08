# cada astronauta é representado por uma lista com informações cruciais: suas coordenadas x e y no espaço.

# os astronautas que estavam muito próximos da explosão não sobreviveram


def astronaut_recue(bolls, explosion_position, size_impact):
    number_astornaut_survived = 0
    astronaut_survived_positions = []
    all_center_points_bolls = []
    for boll in bolls:
        astronaut_survived_positions.clear()
        for astronaut_position in boll:
            survive = astornaut_survived(
                explosion_position[0], explosion_position[1], astronaut_position[0], astronaut_position[1], size_impact)

            if survive:
                astronaut_survived_positions.append(astronaut_position)

            number_astornaut_survived += int(survive)
        if len(astronaut_survived_positions):
            result_x, result_y = center_points(astronaut_survived_positions)
            all_center_points_bolls.append([result_x, result_y])

    # all_center_points_bolls.append(center_point)
    return number_astornaut_survived, all_center_points_bolls


def astornaut_survived(explosion_x, explosion_y, astronaut_position_x, astronaut_position_y, size):
    distance = ((astronaut_position_x - explosion_x)**2 +
                (astronaut_position_y - explosion_y)**2)**(1/2)
    return distance > size


def center_points(boll):
    x_position_average = 0
    y_position_average = 0
    for astronaut_position in boll:
        x_position_average += astronaut_position[0]
        y_position_average += astronaut_position[1]

    x_position_average = x_position_average/len(boll)
    y_position_average = y_position_average/len(boll)

    return x_position_average, y_position_average


def main():
    bolls = eval(input())
    explosion_position = eval(input())
    size_impact = int(input())
    survided, center_points = astronaut_recue(
        bolls, explosion_position, size_impact)

    print([survided, center_points])


main()
