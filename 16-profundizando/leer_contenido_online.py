# Leer contenido online
from urllib.request import urlopen

with urlopen("http://globalmentoring.com.mx/recursos/GlobalMentoring.txt") as mensaje:
  contenido = mensaje.read().decode("utf-8")

# Contar ocurrencias de una cadena
print("Numero de veces de la palbra Universidad: ",contenido.count("Universidad"))

# upper convierte a mayusculas un str
print(contenido.upper())

print(contenido)

#lower convierte a minusculas una cadena
print(contenido.lower())

# buscamos la cadena python en el contenido
print("Existe python?: ","python" in contenido.lower())
print("Existe python?: ","python".upper() in contenido.upper())

# starswith - inicia con 

print("Inicia con x texto",contenido.startswith("En GlobalMentoring.com.mx"))

# endswith - termina con 

print("Termina con x cadena", contenido.lower().endswith("GlobalMentoring.com.mx".lower()))

mensaje = "Hola Mundo"
print("contiene todos sus caracteres en minusculas?", mensaje.lower().islower())
print("contiene todos sus caracteres en mayusculas?", mensaje.upper().isupper())

#reemplazar contenido 
print(contenido.replace(" ","-"))

# Eliminar caracteres al inicio y final de una cadena -strip
titulo = " *** One Piece *** "
print("cadena original", titulo)
print("cadena stripeada", titulo.strip())

titulo = "***One Piece***".strip("*")
print(titulo)
titulo = "***One Piece***".rstrip("*")
print(titulo)
titulo = "***One Piece***".lstrip("*")
print(titulo)

titulo = " *** One Piece *** ".strip().strip("*").strip()
print(titulo)

