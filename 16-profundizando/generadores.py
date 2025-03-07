# Generadores 
# Es una funcion especial, retorna una secuencia de valores
# suspende la ejecuciond e la funcion yield (no se usa return)

def generador():
  yield 1
  print("Se reanuda la ejecucion")
  yield 2
  print("Se reanuda la ejecucion")
  yield 3
  
# Consumimos el generador a demanda
gen = generador()

# Con cada llamada consumimos un valor
print(next(gen))
print(next(gen))
print(next(gen))

# Si tratamos de consumir mas valores de los que produce tira un error
#print(next(gen))

# Consumiendo los valores del generador con un ciclo for

for valor in generador():
  print(f"Numero generado: {valor}")