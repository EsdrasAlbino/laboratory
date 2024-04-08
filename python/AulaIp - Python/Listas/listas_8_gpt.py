def rotate_section(section, direction, times):
    length = len(section)
    if direction == '>':
        return section[-times % length:] + section[:-times % length]
    elif direction == '<':
        return section[times % length:] + section[:times % length]

def main():
    penteado= input().split(' - ')
    top= input().split(' - ')
    bottom= input().split(' - ')
    sapato = input().split(' - ')


    print("Triagem das peças realizada com sucesso, pronta para iniciar mesclagem!")

    while True:
        moves = input().split()
        x, y, z, w = int(moves[0]), int(moves[1]), int(moves[2]), int(moves[3])
        direction_penteado, direction_top, direction_bottom, direction_sapato = moves[4], moves[5], moves[6], moves[7]

        penteado = rotate_section(penteado, direction_penteado, x)
        top = rotate_section(top, direction_top, y)
        bottom = rotate_section(bottom, direction_bottom, z)
        sapato = rotate_section(sapato, direction_sapato, w)

        print("Iniciando mesclagem...")
        print(f"O look gerado foi:\ncabelo {penteado[0]}, {top[-1]} com {bottom[-1]} e {sapato[-1]} nos pés.")

        decision = input()
        if decision == 'Amei!!' and top[-1] == 'camisa':
            print("Essa Barbie vai torcer pela seleção feminina na copa do mundo 2023!")
            break
        elif decision == 'Amei!!':
            print("Essa Barbie vai arrasar com o look perfeito!")
            break
        elif decision == 'Acho que não combinou muito :/':
            continue
        elif decision == 'Melhor escolher eu mesma':
            print("Acho que estou precisando de ajustes, Ken :(")
            break

main()
