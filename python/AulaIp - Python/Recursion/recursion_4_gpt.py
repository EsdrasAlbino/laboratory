G = int(input())
K = int(input())
Q = int(input())

# Inicializa uma lista de coeficientes com tamanho G + 1
coefficients = [0] * (G + 1)

for _ in range(Q):
    coefficient_exponent = input().split(" do ")[1].split(" : ")
    E, C = int(coefficient_exponent[0]), int(coefficient_exponent[1])
    # Armazena o coeficiente no índice correspondente ao expoente
    coefficients[E] = C


def calculate_derivative(coefficients, K):
    if K == 0:
        return coefficients

    new_coefficients = [0] * len(coefficients)

    for i in range(len(coefficients)):
        if coefficients[i] != 0:
            new_coefficients[i - 1] = i * coefficients[i]

    return calculate_derivative(new_coefficients, K - 1)


def format_polynomial(coefficients):
    polynomial_terms = []

    for i in range(len(coefficients) - 1, -1, -1):
        if coefficients[i] != 0:
            if i == 0:
                polynomial_terms.append(str(coefficients[i]))
            elif i == 1:
                if coefficients[i] > 0:
                    polynomial_terms.append(f"{coefficients[i]}x")
                else:
                    polynomial_terms.append(f"-{-coefficients[i]}x")
            else:
                if coefficients[i] > 0:
                    polynomial_terms.append(f"{coefficients[i]}x^{i}")
                else:
                    polynomial_terms.append(f"-{-coefficients[i]}x^{i}")

    return '+'.join(polynomial_terms)


# Chamando a função de cálculo da derivada
derivative_coefficients = calculate_derivative(coefficients, K)

# Formatando a saída
original_polynomial = format_polynomial(coefficients)
derivative_polynomial = format_polynomial(derivative_coefficients)

# Imprimindo a saída final
print(f"A derivada {K} do polinômio {original_polynomial} é")
print(derivative_polynomial)
