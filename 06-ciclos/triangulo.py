print("*** Dibujar un triangulo ***")

numero_filas = int(input("Proporciona el numero de filas: "))

for fila in range(1, numero_filas + 1):
  espacios_blancos = " " * (numero_filas - fila)
  asteriscos = "*" * (2 * fila - 1)
  print(espacios_blancos + asteriscos)