print("*** Listas y Diccionarios ***")
personas = [
  {
    "nombre": "Luffy",
    "apellido": "Monkey D.",
    "edad": 19
  },
  {
    "nombre": "Zoro",
    "apellido": "Roronoa",
    "edad": 21
  }
]

for i in personas:
  print(f"- Persona: {i}")
  
print(f"""Detalle del primer elemento de la lista: 
  Nombre: {personas[0].get("nombre")}
  Apellido: {personas[0].get("apellido")}
  Edad: {personas[0].get("edad")}
      """)

print()
for contador, persona in enumerate(personas):
  print(f"{contador + 1} - Persona: {persona}")
  # print(f"Detalle: Nombre: {persona.get("nombre")} Apellido: {persona.get("apellido")}")