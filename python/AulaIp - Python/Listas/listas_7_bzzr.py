prifissao_prevista = input()
if prifissao_prevista == 'Medica':
    objetos_previstos = ['Estetoscopio', 'Esfigmomanometro', 'Jaleco', 'Caneta' , 'Celular']
elif prifissao_prevista == 'Assistente de Informatica':
    objetos_previstos = ['Calculadora', 'Oculos', 'Notebook', 'Camisa Social', 'Caderno']
elif prifissao_prevista == 'Padeira':
    objetos_previstos = ['Rolo', 'Caneta', 'Avental', 'Colher de Pau', 'Caderno']
elif prifissao_prevista == 'Economista':
    objetos_previstos = ['Calculadora', 'Caneta', 'Camisa Social', 'Agenda', 'Celular']
elif prifissao_prevista == 'Personal Trainer':
    objetos_previstos = ['Halter', 'Agenda', 'Celular', 'Legging', 'Corda']

profissao_do_dia = input()
if profissao_do_dia == 'Medica':
    objetos_do_dia = ['Estetoscopio', 'Esfigmomanometro', 'Jaleco', 'Caneta' , 'Celular']
elif profissao_do_dia == 'Assistente de Informatica':
    objetos_do_dia = ['Calculadora', 'Oculos', 'Notebook', 'Camisa Social', 'Caderno']
elif profissao_do_dia == 'Padeira':
    objetos_do_dia = ['Rolo', 'Caneta', 'Avental', 'Colher de Pau', 'Caderno']
elif profissao_do_dia == 'Economista':
    objetos_do_dia = ['Calculadora', 'Caneta', 'Camisa Social', 'Agenda', 'Celular']
elif profissao_do_dia == 'Personal Trainer':
    objetos_do_dia = ['Halter', 'Agenda', 'Celular', 'Legging', 'Corda']

continua = True
bolsa = objetos_previstos.copy()

while continua:
  objetoNaBolsa = False
  pertenceAoDia = False
  estaNaLista = False
  acao = input()

  if acao == 'Sair':
    break
  
  item = input()

  if acao == 'Adicionar':
    cont = 0
    for c in bolsa:
       if item == c:
          objetoNaBolsa = True
          print(f'Barbie, você já colocou {item} na bolsa')
    if objetoNaBolsa == False:
      for i in objetos_do_dia:
        
        cont +=1
        if i == item:
          print(f'{item} adicionado à bolsa')
          bolsa.append(item)
          estaNaLista = True
          break
        if estaNaLista == False and cont == len(objetos_do_dia) :
          print(f'Barbie, {item} não esta na lista de itens de {profissao_do_dia}')
  
  elif acao == 'Retirar':
    for c in bolsa:
      if item == c:
        objetoNaBolsa = True
    for i in objetos_do_dia:
      if i == item:
        pertenceAoDia = True
        break
    if objetoNaBolsa and pertenceAoDia == False:
       print(f'{item} retirado da bolsa')
       bolsa.remove(item)
    elif objetoNaBolsa and pertenceAoDia:
       print(f'Não faca isso Barbie, você precisa de {item} para trabalhar de {profissao_do_dia}')
    elif objetoNaBolsa == False:
       print('Barbie, como você vai retirar algo que já não esta ai?')
#barbie saiu de casa

bolsaOrganizada = bolsa.copy()
bolsaOrganizada.sort()
itensNaBolsa = ', '.join(bolsaOrganizada)
print(f'Itens na bolsa: {itensNaBolsa}') #printando itens da bolsa ao sair de casa com ', '

objetos_do_dia_Organizados = objetos_do_dia.copy()
objetos_do_dia_Organizados.sort() #organizando listas para comparação da primeira possibilidade de output final

listaOutput2 = objetos_do_dia_Organizados.copy() #lista para manipular a segunda possibilidade de output final
for v in bolsaOrganizada:
   for t in listaOutput2:
      if v == t:
         posicao = listaOutput2.index(t,0)
         listaOutput2.pop(posicao)
for c in listaOutput2:
   item_esquecido = c

#terceira possibilidade de output final
listaOutput3 = bolsaOrganizada.copy()
for i in objetos_do_dia_Organizados:
  for w in listaOutput3:
    if i == w:
      posicao = listaOutput3.index(w,0)
      listaOutput3.pop(posicao)
for p in listaOutput3:
    item_errado = p

#prints finais
if objetos_do_dia_Organizados == bolsaOrganizada:
   print('Boa Barbie, foi na correria mas tudo deu certo!')
elif len(listaOutput2) == 1:
    print(f'Oh não!! Barbie, você esqueceu de pegar {item_esquecido}!!')
elif len(listaOutput3) == 1:
    print(f'Barbie, você esqueceu de tirar {item_errado}, você não usa ele trabalhando de {profissao_do_dia}')