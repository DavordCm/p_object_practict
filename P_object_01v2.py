#input
numero = input("añadir: ")
digito_buscar = input("añadir: ")
#process
def contar(numero, digito):
  
  return str(numero).count(str(digito))

resultado = contar(numero, digito_buscar)
#output
print("El dígito se repite: ", resultado ," veces")