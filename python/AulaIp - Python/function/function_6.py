
def infax_value(expression):
    stack = []
    operators = set(['+', '-', '*', '/'])

    for token in expression.split():
        if token not in operators:
            stack.append(token)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            expression = f"({operand1} {token} {operand2})"
            stack.append(expression)

    return stack[0]


def perfect_number(number):
    Sum = 0
    into_loop = False
    for i in range(1, number):
        into_loop = True
        if number % i == 0:
            Sum += i
    if into_loop:
        return Sum == number
    else:
        return 0


def decode_expression_set(expressions):
    binary_result = ""
    for expression in expressions:
        result = eval(infax_value(expression))
        result = int(result)
        binary_result += str(int(perfect_number(result)))

    character = chr(int(binary_result, 2))
    return binary_result, character


def main():
    expression_sets = []
    expression_set = []
    while True:
        line = input()
        if line == "":
            expression_sets.append(expression_set)
            expression_set = []
        elif line == "Todas as expressoes foram enviadas!":
            break
        else:
            expression_set.append(line)

    decoded_word = ""
    for idx, expression_set in enumerate(expression_sets, start=1):
        binary_result, character = decode_expression_set(expression_set)
        print(
            f"O {idx}º conjunto de expressoes resultou no binario {binary_result} que em ASCII eh: {character}")
        decoded_word += character
        if len(expression_sets) == idx:
            break

    print("\nA decodificacao final resultou em:")
    print(decoded_word)


main()
