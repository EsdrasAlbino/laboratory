

# OBS 1: Você deve usar uma função para decodificar os códigos.
# OBS 2: Você não poderá utilizar o método count() nem o método find().
# OBS 3: Nessa questão, saiba que o eixo X será referente às linhas da matriz e o eixo Y será referente às colunas da matriz.

# Nos códigos, podem aparecer letras minúsculas e/ou letras maiúsculas do alfabeto da língua portuguesa.
# Além disso, números naturais também podem aparecer


# função para decodificar os códigos para retornar a posição x
def decoficator_position_x_and_y(code):
    vowels_in_code = 0
    consonant_in_code = 0
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    all_not_multiply = False
    code = code.lower()

    numbers = [int(s) for s in code if s.isdigit()]
    code = [s for s in code if not s.isdigit()]
    for number in numbers:
        if not number % numbers[0] == 0:
            all_not_multiply = True
            break
    if all_not_multiply or len(numbers) == 0:
        for x in code:
            if x in vowels_list:
                vowels_in_code += 1
            else:
                consonant_in_code += 1

        if (consonant_in_code == 0):
            position_star_x_or_y = 0
            return position_star_x_or_y
        else:
            divider_operation = vowels_in_code/consonant_in_code

        value_processed = bottom_value(divider_operation)

        position_star_x_or_y = value_processed % 7

    else:
        position_star_x_or_y = 3

    return position_star_x_or_y


# função piso
def bottom_value(value):
    return int(value)


def main():
    input_reference_x = input()
    input_reference_y = input()
    matrix = []

    star_in_y = decoficator_position_x_and_y(input_reference_y)
    star_in_x = decoficator_position_x_and_y(input_reference_x)

    for row in range(7):
        a = []
        # A for loop for column entries
        for column in range(7):
            if row == star_in_x and column == star_in_y:
                a.append('☆')
            else:
                a.append('.')
        matrix.append(a)

    for i in matrix:
        print(" ".join(i))

    if star_in_x == 3 and star_in_y == 3:
        print('Ótimo, a estrela vai ficar exatamente no meio da fotografia! Posição melhor não existe!')
        print('Obrigado pela ajuda! A foto ficou ótima!')
    elif (star_in_x == 6 or star_in_x == 0) or (star_in_y == 6 or star_in_y == 0):
        print('Ihhh, vou ter que relocalizar a câmera, uma fotografia com a estrela na borda não dá! Infelizmente demora um pouco para criar outro código...')
        print('Mesmo que eu não tenha conseguido uma matriz boa para tirar a foto, obrigado pelo seu tempo.')
    else:
        print('Ok, agora é só enviar a matriz!')
        print('Obrigado pela ajuda! A foto ficou ótima!')


main()
