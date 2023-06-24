
nomeAranha = input()
ataqueAranha = int(input())
defesaAranha = int(input())
nomeAliado = input()
ataqueAliado = int(input())
defesaAliado = int(input())

nomeVilao = input()
ataqueVilao = int(input())
defesaVilao = int(input())
nomeCapanga = input()
ataqueCapanga = int(input())
defesaCapanga = int(input())


fatorSorte_1 = int(input())
fatorSorte_2 = int(input())
fatorSorte_3 = int(input())

vitoriaAliados = 0
vitoriaInimigos = 0

if (fatorSorte_1 == 0):
    ataqueTotalAliado = ataqueAranha
    defesaTotalAliado = defesaAranha
    ataqueTotalInimigo = ataqueVilao
    defesaTotalInimigo = defesaVilao
elif (fatorSorte_1 == 1):
    ataqueTotalAliado = ataqueAranha+ataqueAliado
    defesaTotalAliado = defesaAranha
    ataqueTotalInimigo = ataqueVilao+ataqueCapanga
    defesaTotalInimigo = defesaVilao
elif (fatorSorte_1 == 2):
    ataqueTotalAliado = ataqueAranha
    defesaTotalAliado = defesaAranha+defesaAliado
    ataqueTotalInimigo = ataqueVilao
    defesaTotalInimigo = defesaVilao+defesaCapanga
else:
    ataqueTotalAliado = ataqueAranha+ataqueAliado
    defesaTotalAliado = defesaAranha+defesaAliado
    ataqueTotalInimigo = ataqueVilao+ataqueCapanga
    defesaTotalInimigo = defesaVilao+defesaCapanga

print("1° confronto:")

if (ataqueTotalAliado > defesaTotalInimigo):
    print(f"O {nomeAranha} acertou vários golpes no {nomeVilao}")
    vitoriaAliados = vitoriaAliados+1
elif (ataqueTotalAliado == defesaTotalInimigo):
    if (fatorSorte_1 == 0 or fatorSorte_1 == 3):
        print(f"O {nomeAranha} acertou vários golpes no {nomeVilao}")
        vitoriaAliados = vitoriaAliados+1
    else:
        if fatorSorte_1 == 1:
            print(f"O {nomeAranha} acertou vários golpes no {nomeVilao}")
            vitoriaAliados = vitoriaAliados+1
        else:
            print(f"O {nomeVilao} está dificultando a vida do {nomeAranha}")
            vitoriaInimigos = vitoriaInimigos+1
else:
    print(f"O {nomeVilao} está dificultando a vida do {nomeAranha}")
    vitoriaInimigos = vitoriaInimigos+1


if (fatorSorte_2 == 0):
    ataqueTotalAliado = ataqueAranha
    defesaTotalAliado = defesaAranha
    ataqueTotalInimigo = ataqueVilao
    defesaTotalInimigo = defesaVilao
elif (fatorSorte_2 == 1):
    ataqueTotalAliado = ataqueAranha+ataqueAliado
    defesaTotalAliado = defesaAranha
    ataqueTotalInimigo = ataqueVilao+ataqueCapanga
    defesaTotalInimigo = defesaVilao
elif (fatorSorte_2 == 2):
    ataqueTotalAliado = ataqueAranha
    defesaTotalAliado = defesaAranha+defesaAliado
    ataqueTotalInimigo = ataqueVilao
    defesaTotalInimigo = defesaVilao+defesaCapanga
else:
    ataqueTotalAliado = ataqueAranha+ataqueAliado
    defesaTotalAliado = defesaAranha+defesaAliado
    ataqueTotalInimigo = ataqueVilao+ataqueCapanga
    defesaTotalInimigo = defesaVilao+defesaCapanga

print("2° confronto:")

if (defesaTotalAliado > ataqueTotalInimigo):
    print(f"O {nomeAranha} contra-atacou o {nomeVilao}")
    vitoriaAliados = vitoriaAliados+1

elif (defesaTotalAliado == ataqueTotalInimigo):
    if (fatorSorte_2 == 0 or fatorSorte_2 == 3):
        print(f"O {nomeAranha} contra-atacou o {nomeVilao}")
        vitoriaAliados = vitoriaAliados+1
    else:
        if fatorSorte_2 == 2:
            print(f"O {nomeAranha} contra-atacou o {nomeVilao}")
            vitoriaAliados = vitoriaAliados+1

        else:
            print(f"O {nomeAranha} não consegue se defender contra o {nomeVilao}")
            vitoriaInimigos = vitoriaInimigos+1

else:
    print(f"O {nomeAranha} não consegue se defender contra o {nomeVilao}")
    vitoriaInimigos = vitoriaInimigos+1


if (fatorSorte_3 == 0):
    ataqueTotalAliado = ataqueAranha
    defesaTotalAliado = defesaAranha
    ataqueTotalInimigo = ataqueVilao
    defesaTotalInimigo = defesaVilao
elif (fatorSorte_3 == 1):
    ataqueTotalAliado = ataqueAranha+ataqueAliado
    defesaTotalAliado = defesaAranha
    ataqueTotalInimigo = ataqueVilao+ataqueCapanga
    defesaTotalInimigo = defesaVilao
elif (fatorSorte_3 == 2):
    ataqueTotalAliado = ataqueAranha
    defesaTotalAliado = defesaAranha+defesaAliado
    ataqueTotalInimigo = ataqueVilao
    defesaTotalInimigo = defesaVilao+defesaCapanga
else:
    ataqueTotalAliado = ataqueAranha+ataqueAliado
    defesaTotalAliado = defesaAranha+defesaAliado
    ataqueTotalInimigo = ataqueVilao+ataqueCapanga
    defesaTotalInimigo = defesaVilao+defesaCapanga

print("3° confronto:")

if (ataqueTotalAliado > defesaTotalInimigo):
    print(f"O {nomeAranha} acertou vários golpes no {nomeVilao}")
    vitoriaAliados = vitoriaAliados+1

elif (ataqueTotalAliado == defesaTotalInimigo):
    if (fatorSorte_3 == 0 or fatorSorte_3 == 3):
        print(f"O {nomeAranha} acertou vários golpes no {nomeVilao}")
        vitoriaAliados = vitoriaAliados+1

    else:
        if fatorSorte_3 == 1:
            print(f"O {nomeAranha} acertou vários golpes no {nomeVilao}")
            vitoriaAliados = vitoriaAliados+1

        else:
            print(f"O {nomeVilao} está dificultando a vida do {nomeAranha}")
            vitoriaInimigos = vitoriaInimigos+1

else:
    print(f"O {nomeVilao} está dificultando a vida do {nomeAranha}")
    vitoriaInimigos = vitoriaInimigos+1

if (vitoriaAliados > vitoriaInimigos):
    print(f"O {nomeAranha} e {nomeAliado} conseguiram derrotar o {nomeVilao} e recuperar o multiverso!")
else:
    print(f"O {nomeVilao} e {nomeCapanga} invadiram Nova York, onde estão os outros aranhas??")
