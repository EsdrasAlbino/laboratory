def postfix_to_infix(expression):
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


def is_perfect_number(num):
    divisors_sum = sum([i for i in range(1, num) if num % i == 0])
    return divisors_sum == num


def decode_expression_set(expressions):
    binary_result = ""
    for expression in expressions:
        result = eval(postfix_to_infix(expression))
        result = int(result)
        binary_result += str(int(is_perfect_number(result)))

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
            expression_sets.append(expression_set)
            break
        else:
            expression_set.append(line)

    decoded_word = ""
    for idx, expression_set in enumerate(expression_sets, start=1):
        binary_result, character = decode_expression_set(expression_set)
        print(
            f"O {idx}º conjunto de expressoes resultou no binario {binary_result} que em ASCII eh: {character}")
        decoded_word += character

    print("\nA decodificacao final resultou em:")
    print(decoded_word)


if __name__ == "__main__":
    main()
