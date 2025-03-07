# Generador de numeros del 1 al 5
def generador_numeros():
  for numero in range(1,6):
    yield numero
    print("Se reanuda la ejecucion")
    
# Utilizar el generador 
generador = generador_numeros()
print(f"Objeto generador: {generador}")
print(type(generador))

# Consumimos los valores del generador 
for valor in generador:
  print(f"Numero producido: {valor}")
  
# Consumir a demanda
generador = generador_numeros()
try:
  print(f"Consumir a demanda: {next(generador)}")
  print(f"Consumir a demanda: {next(generador)}")
  print(f"Consumir a demanda: {next(generador)}")
  print(f"Consumir a demanda: {next(generador)}")
  print(f"Consumir a demanda: {next(generador)}")
  print(f"Consumir a demanda: {next(generador)}")
except StopIteration as e:
  print(f"Error al consumir el generador: {e}")
  
# Otra forma de consumir un generador 
generador = generador_numeros()
while True:
  try:
    valor = next(generador)
    print(f"impresion del valor generado: {valor}")
  except StopIteration as e:
    print("Se termino de iterar  el generador")
    break