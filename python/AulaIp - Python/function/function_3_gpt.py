def is_palindrome(input_string):
    # Remover espaços em branco e transformar tudo em letras minúsculas
    clean_string = input_string.replace(" ", "").lower()
    # Verificar se a string é igual à sua reversa (palíndromo)
    return clean_string == clean_string[::-1]


def count_distinct_elements(input_string):
    # Remover espaços em branco e transformar tudo em letras minúsculas
    clean_string = input_string.replace(" ", "").lower()
    # Usar um conjunto para obter os elementos distintos (letras ou números)
    distinct_elements = set(clean_string)
    # Contar a quantidade de elementos distintos
    return len(distinct_elements)


def main():
    n = int(input())  # Ler o número de frases/números que serão gerados

    for _ in range(n):
        input_string = input()  # Ler a próxima frase ou número
        is_number = input_string.isdigit()  # Verificar se é um número

        if is_number:
            if is_palindrome(input_string):
                print(f'O número "{input_string}" é um palíndromo!')
            else:
                print('A frase ou o número não é um palíndromo.')

            distinct_count = count_distinct_elements(input_string)
            print(
                f'Há {distinct_count} número(s) distinto(s) na sequência de números.')

        else:  # É uma frase
            if is_palindrome(input_string):
                print(f'A frase "{input_string}" é um palíndromo!')
            else:
                print('A frase ou o número não é um palíndromo.')

            distinct_count = count_distinct_elements(input_string)
            print(f'Há {distinct_count} letra(s) distinta(s) na frase.')


if __name__ == "__main__":
    main()
