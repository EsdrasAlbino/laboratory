
dica_criptografado = int(input())

if dica_criptografado % 2 == 0:
    dica_decodificado = ((dica_criptografado/2)**0.5)+2
else:
    dica_decodificado = (dica_criptografado/3)+3

filme_one = input()
filme_two = input()
filme_three = input()
nao_achei_filme = True
achei_filme = False
cansaco = 0
tem_dc = False

if (filme_one == "Vingadores: Ultimato") and nao_achei_filme:
    cansaco += 2
    if dica_decodificado == len(filme_one):
        nao_achei_filme = False
elif nao_achei_filme:
    cansaco += 1
    if dica_decodificado == len(filme_one):
        nao_achei_filme = False

if (filme_two == "Vingadores: Ultimato") and nao_achei_filme:
    cansaco += 2
    if dica_decodificado == len(filme_two):
        nao_achei_filme = False
elif nao_achei_filme:
    cansaco += 1
    if dica_decodificado == len(filme_two):
        nao_achei_filme = False

if (filme_three == "Vingadores: Ultimato") and nao_achei_filme:
    cansaco += 2
    if dica_decodificado == len(filme_three):
        nao_achei_filme = False
elif nao_achei_filme:
    cansaco += 1
    if dica_decodificado == len(filme_three):
        nao_achei_filme = False


if filme_one == "Coringa" or filme_one == "Batman vs Superman" or filme_one == "O Cavaleiro das Trevas":
    print("Algo de errado não está certo!")
    tem_dc = True
if filme_two == "Coringa" or filme_two == "Batman vs Superman" or filme_two == "O Cavaleiro das Trevas":
    print("Algo de errado não está certo!")
    tem_dc = True
if filme_three == "Coringa" or filme_three == "Batman vs Superman" or filme_three == "O Cavaleiro das Trevas":
    print("Algo de errado não está certo!")
    tem_dc = True

if not tem_dc:
    if len(filme_one) == int(dica_decodificado):
        print("Miles: Achei o easter egg!!!")
        filme_stanLee = input()
        duracao_filme_stanLee = int(input())
        achei_filme = True
        if cansaco >= 2 and duracao_filme_stanLee >= 135:
            print("Miles: A mimir")
        elif cansaco >= 2 and duracao_filme_stanLee >= 120 and duracao_filme_stanLee < 135:
            print("Gwen: Nada que uma xícara de café não resolva!")
        elif duracao_filme_stanLee < 120 or cansaco < 2:
            print(
                f"Peter: {filme_stanLee} é o melhor filme do homem aranha, 10/10")

    else:
        print("Miles: Tou frio, melhor ir procurar nas fases mais antigas")
    if not achei_filme:
        if len(filme_two) == int(dica_decodificado):
            print("Miles: Achei o easter egg!!!")
            filme_stanLee = input()
            duracao_filme_stanLee = int(input())
            achei_filme = True
            if cansaco >= 2 and duracao_filme_stanLee >= 135:
                print("Miles: A mimir")
            elif cansaco >= 2 and duracao_filme_stanLee >= 120 and duracao_filme_stanLee < 135:
                print("Gwen: Nada que uma xícara de café não resolva!")
            elif duracao_filme_stanLee < 120 or cansaco < 2:
                print(
                    f"Peter: {filme_stanLee} é o melhor filme do homem aranha, 10/10")

        else:
            print("Gwen: Cadê o velho??? Queria um autógrafo")
    if not achei_filme:
        if len(filme_three) == int(dica_decodificado) and not achei_filme:
            print("Miles: Achei o easter egg!!!")
            filme_stanLee = input()
            duracao_filme_stanLee = int(input())
            achei_filme = True
            if cansaco >= 2 and duracao_filme_stanLee >= 135:
                print("Miles: A mimir")
            elif cansaco >= 2 and duracao_filme_stanLee >= 120 and duracao_filme_stanLee < 135:
                print("Gwen: Nada que uma xícara de café não resolva!")
            elif duracao_filme_stanLee < 120 or cansaco < 2:
                print(
                    f"Peter: {filme_stanLee} é o melhor filme do homem aranha, 10/10")

        else:
            print("Peter: Parece que o próximo filme do aranha-verso vai demorar mais do que esperado pra sair...")
