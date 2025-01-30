print("*** Retornar tupla desde funcion ***")

def persona_mayusculas(nombre:str, apellido:str, edad:int):
  print(f"Esta funcion retorna varios valores")
  return (nombre.upper(), apellido.upper(), edad)

nombre, apellido, edad = persona_mayusculas("Juanse", "Maulini", 24)
print(nombre, apellido, edad)