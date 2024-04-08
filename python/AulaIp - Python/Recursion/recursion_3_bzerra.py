def isCulpado(nome_suspeito, string_concatenada):
    nome_suspeito = nome_suspeito.lower()
    string_concatenada = string_concatenada.lower()
    tamanho_nome = len(nome_suspeito)

    posicao = string_concatenada.find(nome_suspeito[0])
    if posicao != -1:

        nome = string_concatenada[posicao: (posicao + len(nome_suspeito))]
        if nome == nome_suspeito:
            return True
        else:
            string_concatenada = string_concatenada.replace(
                string_concatenada[posicao], '')
            return isCulpado(nome_suspeito, string_concatenada)
    else:
        return False


suspeito = input()
str_concat = input()

if isCulpado(suspeito, str_concat):
    print(f'Encontrei, o culpado é o {suspeito}!')
else:
    print(f'Não era o {suspeito}, tenho que continuar procurando.')
