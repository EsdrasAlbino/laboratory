# Letras em maiúsculo e em minúsculos devem ser consideradas como iguais pelo seu programa.

def __palindrome__(term):
    is_palindrome = True
    term = term.replace(" ", "").lower()
    size_term = len(term)

    position_left = 0
    position_right = size_term-1
    term_by_term = list(term)

    if size_term % 2 == 0:
        while size_term/2 >= position_left:
            if term_by_term[position_left] != term_by_term[position_right]:
                return False

            position_left += 1
            position_right -= 1
    else:
        while size_term//2 >= position_left:
            if term_by_term[position_left] != term_by_term[position_right]:
                return False

            position_left += 1
            position_right -= 1

    return True


def count_distinct(term):
    term = term.replace(" ", "").lower()
    distinct_caracther = set(term)
    return len(distinct_caracther)


def main():
    N = int(input())
    number_terms = 0
    while N > number_terms:
        terms = input()

        if __palindrome__(terms):
            if not terms.isdigit():
                print(f'A frase "{terms}" é um palíndromo!')
                print(
                    f'Há {count_distinct(terms)} letra(s) distinta(s) na frase.')
            else:
                print(f'O número "{terms}" é um palíndromo!')
                print(
                    f'Há {count_distinct(terms)} número(s) distinto(s) na sequência de números.')

        else:
            print('A frase ou o número não é um palíndromo.')

        number_terms += 1


main()
