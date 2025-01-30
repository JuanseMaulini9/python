print("*** Diccionarios en python ***")

persona = {
  "nombre" : "Juanse",
  "edad" : 24,
  "ciudad" : "Junin"
}

print(f"Diccionario de persona: {persona}")

print(f"Nombre: {persona["nombre"]}")
print(f"Edad: {persona.get("edad")}")
print(f"Ciudad: {persona["ciudad"]}")

persona["edad"] = 25

print(f"Diccionario de persona modificado: {persona}")

persona["profesion"] = "Developer"

print(f"Diccionario de persona modificado: {persona}")

del persona["ciudad"]

print(f"Diccionario de persona modificado: {persona}")

persona.pop("profesion")

print(f"Diccionario de persona modificado: {persona}")

for llave, valor in persona.items():
  print(f"Llave: {llave}, Valor: {valor}")
  
for valor in persona.values():
  print(f"Valor: {valor}")

for llaves in persona.keys():
  print(f"Llaves: {llaves}")