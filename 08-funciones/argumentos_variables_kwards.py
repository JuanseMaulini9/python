# args - argumentos - tupla
# **kwargs - keywords arguments (key, value) como un dict

print("Argumentos variables en forma de diccionario")

def superheroe_superpoderes (nombre, *args, **kwargs):
  print(f"Superheroe: {nombre} - {args} - Mas info: {kwargs}")

superheroe_superpoderes("spiderman", "Instinto Aracnido", edad=17, empresa="Marvel")
superheroe_superpoderes("Iron Man", "Armadura", "Millonario", edad=45)