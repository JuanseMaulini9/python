print("*** Factorial de un numero ***")

def factorial_recursiva(numero): 
  #caso base 0! = 1, 1! = 1
  if(numero == 0 or numero == 1):
    print(f"Resultado factorial parcial {numero} es: 1")
    return 1
  else:
    factorial_parcial = numero * factorial_recursiva(numero - 1)
    print(f"Resultado factorial parcial {numero} es: {factorial_parcial}")
    return factorial_parcial
  
numero = int(input("Ingrese el numero para sacar el factorial: "))  
resultado = factorial_recursiva(numero)
print(f"El factorial de {numero} es: {resultado}")