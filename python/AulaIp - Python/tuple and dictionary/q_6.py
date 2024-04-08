# Função para criar tri-gramas de uma linha de texto
def create_tri_grams(line):
    tri_grams = set()
    line = line.lower()  # Converter para minúsculas
    for i in range(len(line) - 2):
        tri_gram = line[i:i+3]
        tri_grams.add(tri_gram)
    return tri_grams

def search_term(quantify_loop,):


# Lê as frases do texto e cria um dicionário de tri-gramas
tri_grams_dict = {}
line_number = 0
while True:
    linha_atual = input()
    if linha_atual == "END_OF_FILE":
        break
    tri_grams = create_tri_grams(linha_atual)
    for tri_gram in tri_grams:
        if tri_gram in tri_grams_dict:
            tri_grams_dict[tri_gram].append(line_number)
        else:
            tri_grams_dict[tri_gram] = [line_number]
    line_number += 1

# Lê a quantidade de trechos a serem buscados
qtd_buscas = int(input())

# Realiza as buscas
for _ in range(qtd_buscas):
    trecho = input().lower()
    trecho_tri_gram = trecho[:3]  # Pega o primeiro tri-gram do trecho
    if trecho_tri_gram in tri_grams_dict:
        possible_lines = tri_grams_dict[trecho_tri_gram]
        found = False
        for line in possible_lines:
            if trecho in linha_atual.lower():
                print(line)
                found = True
                break
        if not found:
            print(-1)
    else:
        print(-1)
