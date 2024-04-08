integrantes = int(input())
posicao_loop = 0

ultimo=1
penultimo=1
sequencia = "1, 1, "

if (integrantes==1) or (integrantes==1):
  #sequencia = "{sequencia},"
else:
  count=3
  while count <= integrantes:
      termo = ultimo + penultimo
      penultimo = ultimo
      ultimo = termo
      count += 1
      if(count > integrantes):
        sequencia += str(termo)
      else:
        sequencia += str(termo) + ", "
      
print(f"A sequência de número das camisas do seu time será: {sequencia}")

