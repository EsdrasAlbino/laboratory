
# Init values get input
polynomial_degree = int(input())
derivated_order = int(input())
coefficients_no_null = int(input())
coefficients = [0] * (polynomial_degree + 1)

for i in range(coefficients_no_null):
    # Here the split work: Coeficiente do 2 : 4 -> [2 : 4] -> [2][4]
    coefficient_exponent = input().split(" do ")[1].split(" : ")

    E, C = int(coefficient_exponent[0]), int(coefficient_exponent[1])

    # List of coefficients in indice represented expoent
    coefficients[E] = C


def derivative(order, coefficients):
    if order == 0:
        return coefficients

    derivation = [0] * len(coefficients)

    for idx, coeff in enumerate(coefficients):
        # I know is derivative will heave degree = expoent - 1, so derivation add new coefficient after idx 0
        if coeff != 0 and idx > 0:
            derivation[idx - 1] = idx * coeff

    if sum([i for i in derivation if i]) == 0:
        return derivation

    return derivative(order-1, derivation)


def format_polynomial(coefficients):
    polynomial_terms = []
    size_coefficientes = len(coefficients)-1

    while size_coefficientes >= 0:
        if coefficients[size_coefficientes] != 0:
            if size_coefficientes == 0:
                polynomial_terms.append(str(coefficients[size_coefficientes]))
            elif size_coefficientes == 1:
                if coefficients[size_coefficientes] != 0:
                    if (coefficients[size_coefficientes] == 1):
                        polynomial_terms.append("x")
                    elif (coefficients[size_coefficientes] == -1):
                        polynomial_terms.append("-x")
                    else:
                        polynomial_terms.append(
                            f"{coefficients[size_coefficientes]}x")

            else:
                if coefficients[size_coefficientes] != 0:
                    if (coefficients[size_coefficientes] == 1):
                        polynomial_terms.append(
                            f"x^{size_coefficientes}")
                    elif (coefficients[size_coefficientes] == -1):
                        polynomial_terms.append(
                            f"-x^{size_coefficientes}")
                    else:
                        polynomial_terms.append(
                            f"{coefficients[size_coefficientes]}x^{size_coefficientes}")

        size_coefficientes -= 1
    polynomial_terms.reverse()

    outup_functions = ''
    if not polynomial_terms:
        outup_functions = '0'

    for i, term in enumerate(polynomial_terms):
        if term:
            if term[0] != '-' and i != 0:
                outup_functions += "+"
            outup_functions += term

    # outup_functions += ''.join([('' if c in string.punctuation else ' ')+c for c in wordlist]).strip()
    # outup_functions = '+'.join(polynomial_terms)

    return outup_functions


# called function to calculate derivatives
derivative_coefficients = derivative(derivated_order, coefficients)

# Format output
original_polynomial = format_polynomial(coefficients)
derivative_polynomial = format_polynomial(derivative_coefficients)


print(f"A derivada {derivated_order} do polinômio {original_polynomial} é")
print(derivative_polynomial)
