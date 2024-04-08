
def main():
    integers = input().split(' ')
    life_total = int(integers[0])
    steps = int(integers[1])
    steps_passed = 0

    def fibonacci_in_sequence(k, term_one=0, term_two=1):
        first_term = (term_one == 0 and k == term_one)
        fibonacci = term_one + term_two
        if (fibonacci == k or fibonacci > k or first_term):
            if (fibonacci == k or first_term):
                return True
            else:
                return False
        else:
            return fibonacci_in_sequence(k, term_two, fibonacci)

    while steps_passed < steps and life_total > 0:
        number_step = int(input())
        is_next_step = fibonacci_in_sequence(number_step)

        if (is_next_step):
            steps_passed += 1
            if (steps_passed == steps):
                print(
                    "Voce Adicionou A Master Sword ao seu inventario\nLink Salve Hyrule!!!")
        else:
            steps_passed = 0
            life_total -= 1
            print(
                "Oh nao Link! Voce nao pode parar ainda, voce e a ultima esperanca de Hyrule!")
            if (life_total == 0):
                print(
                    "A ultima defesa de hyrule caiu, nao sobrou ninguem capaz de se opor a Ganondorf")


main()
