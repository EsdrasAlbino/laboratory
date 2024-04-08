
def contains_string(string, substring):
    return string.find(substring) != -1


def replace_value(value):
    return value.replace("R$", "").replace(".", "").replace(",", ".")

# SET CATEGORY FOR TRANSACTION


def category_type(description):
    print("description", description)
    if description == "restaurante" or description == "mercado" or description == "padaria" or description == "supermercado" or description == "Padaria Santa Rita" or description == "Glacai" or description == "Lucidario Silvestre" or description == "Reberthy Goncalves da Silva farias" or description == "REBERTHY GONCALVES DASILVA FARIAS   ME" or description == "SUPERMERCADO NOVA ERA LTDA" or description == "Reberthy Farias" or description == "Marcelo Cristian Da Silva Brito" or description == "Gleydson Fagner Bezerra da Silva" or contains_string(description, "Padaria") or description == "CRISLAYNNE KEYNE DE ALBUQUERQUE QUEIROZ" or description == "Oakberry" or description == "LUCIDARIO SILVESTRE DA SILVA":
        return "Alimentação"
    if description == "internet" or description == "serviços" or description == "serviÃ§os" or description == "charge" or description == "BRISANET SERVIÃ‡OS DETELECOMUNICAÃ‡Ã•ES" or description == "EBANX":
        return "Contas"
    if description == "uber" or description == "99" or description == "transporte" or description == "BILHETAGEM ELETRONICA" or description == "Bilhetagem Eletronica" or description == "Renan Mousinho Aquino" or description == "Filial Fiesta Shopping" or contains_string(description, "99"):
        return "Transporte"
    if description == "aluguel" or description == "condomínio" or description == "casa":
        return "Moradia"
    if description == "academia" or description == "massagem" or description == "cabeleireiro" or description == "vestuÃ¡rio" or description == "MARCOS VINICIUS SOUZA DE LIRA":
        return "Estética"
    if description == "curso" or description == "livro" or description == "material" or description == "educação" or description == "eletrÃ´nicos" or description == "educaÃ§Ã£o":
        return "Educação"
    if description == "presente" or description == "viagem" or description == "passeio" or description == "festa":
        return "Momentos Significativos"
    if description == "investimento" or description == "renda" or description == "rendimento" or description == "renda fixa" or description == "HASTECH SOLUCOES" or description == "EBCT":
        return "Investimentos"
    if description == "saúde" or description == "medicamento" or description == "plano" or description == "saÃºde" or description == "lazer" or description == "Alphafit Academia" or contains_string(description, "Farmacia") or description == "Danilo Aviamentos":
        return "Bem estar"
    if description == "DAS" or description == "SECRETARIA DA RECEITA FEDERAL DO BRASIL":
        return "Imposto"
    if description == "ADILSON SEVERIN" or description == "Claudia Vania Albino da Silva" or description == "THAYNA YSSA ALBINO DA SILVA GONCALVES" or description == "Nicoly Camilli Albino Da Silva" or description == "Matheus Borges Figueiroa" or description == "Matheus Borges FigueirÃ´a":
        return "Emprestimo"

    return description
