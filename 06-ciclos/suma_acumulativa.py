print("*** Suma acumulativa ***")


numero = 1
acumulador_suma = 0

maximo = int(input("Ingrese las iteraciones que quiera hacer: "))

while numero <= maximo:
  print(f"Suma parcial: {acumulador_suma}")
  acumulador_suma += numero
  numero += 1
  
print(acumulador_suma)