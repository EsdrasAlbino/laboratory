
funcionalidade_one = input()
funcionalidade_ponto_one = int(input())
funcionalidade_two = input()
funcionalidade_ponto_two = int(input())
funcionalidade_three = input()
funcionalidade_ponto_three = int(input())
funcionalidade_four = input()
funcionalidade_ponto_four = int(input())
funcionalidade_five = input()
funcionalidade_ponto_five = int(input())


soma_funcionalidade = funcionalidade_ponto_five+funcionalidade_ponto_four + \
    funcionalidade_ponto_three+funcionalidade_ponto_two+funcionalidade_ponto_one

if funcionalidade_one == "novo lançador de teias" and funcionalidade_two != "NADA":
    print("Com calma, aranha")
if funcionalidade_one == "novo lançador de teias" and funcionalidade_two == "lentes de visão avançada":
    print("Lembre de desativar as lentes depois, e cuidado ao usar as teias no escuro")
if funcionalidade_one == "novo lançador de teias" and funcionalidade_two == "lentes de visão avançada" and funcionalidade_three == "traje à prova de balas":
    print("UOU, só tente sair dessa vivo, vou otimizar a energia aqui")
if funcionalidade_one == "ativação de inteligência artificial" or funcionalidade_two == "ativação de inteligência artificial" or funcionalidade_three == "ativação de inteligência artificial" or funcionalidade_four == "ativação de inteligência artificial" or funcionalidade_five == "ativação de inteligência artificial":
    print("Espero que não esteja ativando isso para usar nas provas")
if soma_funcionalidade >= 80:
    print("Vou descarregar em questão de minutos, pare AGORA")


planador = False
lanca_teia = False
ia = False

if funcionalidade_one == "novo lançador de teias":
    lanca_teia = True
elif funcionalidade_one == "membranas planadoras":
    planador = True
elif funcionalidade_one == "ativação de inteligência artificial":
    ia = True

if funcionalidade_two == "novo lançador de teias":
    lanca_teia = True
elif funcionalidade_two == "membranas planadoras":
    planador = True
elif funcionalidade_two == "ativação de inteligência artificial":
    ia = True

if funcionalidade_three == "novo lançador de teias":
    lanca_teia = True
elif funcionalidade_three == "membranas planadoras":
    planador = True
elif funcionalidade_three == "ativação de inteligência artificial":
    ia = True

if funcionalidade_four == "novo lançador de teias":
    lanca_teia = True
elif funcionalidade_four == "membranas planadoras":
    planador = True
elif funcionalidade_four == "ativação de inteligência artificial":
    ia = True

if funcionalidade_five == "novo lançador de teias":
    lanca_teia = True
elif funcionalidade_five == "membranas planadoras":
    planador = True
elif funcionalidade_five == "ativação de inteligência artificial":
    ia = True


if planador and lanca_teia and ia:
    print("Tudo certo, mas cuidado ao ficar conversando com IA enquanto voa")

print(f"Aranha, nessa sequência você usou {soma_funcionalidade} de energia!")
