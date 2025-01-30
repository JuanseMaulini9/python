print("*** Funcion con argumentos por nombre ***")

def imprimir_persona(nombre, apellido="", edad=18):
  print(f"Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}")
  
imprimir_persona("Luffy", "Monkey D.", 19)

imprimir_persona(nombre="Zoro", apellido="Roronoa", edad=21)
imprimir_persona(apellido="Vinsmoke", edad=21, nombre="Sanji")

imprimir_persona(nombre="Luffy")
imprimir_persona(nombre="Luffy", apellido="Monkey D.")

