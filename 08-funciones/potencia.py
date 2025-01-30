print("*** Potencia de un numero ***")

def potencia(numero, exponente): 
  if exponente == 0: 
    return 1
  else:
    resultado = numero * potencia(numero, exponente - 1)
    return resultado

numero= int(input("Ingrese el numero: "))
exponente = int(input("Ingrese el exponente: "))

resultado = potencia(numero, exponente)
print(f"{numero} elevado a {exponente} : {resultado}")