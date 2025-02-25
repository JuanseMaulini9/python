# Profundizando en el tipo str

# import math
# from mi_clase import MiClase

# Concatenacion automatica en python 
# variable = "Adios"
# mensaje = "Hola" "Mundo" + variable
# mensaje += "Dios" "Sol"
# print(mensaje)


# help(math.isnan)
# help(str.capitalize)

# help(MiClase)
# print(MiClase.__doc__)
# print(MiClase.__init__.__doc__)
# print(MiClase.mi_metodo.__doc__)

# help(str.capitalize)
# mensaje1 = "hola mundo"
# mensaje2 = mensaje1.capitalize()

# print(f"mensaje1: {mensaje1}, id: {hex(id(mensaje1))}")
# print(f"mensaje2: {mensaje2}, id: {hex(id(mensaje2))}")

# mensaje1 += "adios"
# print(f"mensaje1: {mensaje1}, id: {hex(id(mensaje1))}")

# help(str.join)

# tupla_str = ("Hola", "Mundo", "One", "Piece")
# mensaje = " ".join(tupla_str)
# print(f"mensaje: {mensaje}")

# lista_personajes = ["Luffy", "Zoro", "Usopp", "Sanji", "Nami"]
# mensaje = ", ".join(lista_personajes)
# print(f"mensaje: {mensaje}")

# cadena = "HolaMundo"
# mensaje = ".".join(cadena)
# print(f"mensaje: {mensaje}")

# diccionario = {
#   "nombre": "Luffy",
#   "apellido": "Monkey D.",
#   "edad": "19"  
# }
# llaves = "-".join(diccionario.keys())
# valores = "-".join(diccionario.values())
# print(f"llaves: {llaves}, type: {type(llaves)}")
# print(f"valores: {valores}, type: {type(valores)}")

# help(str.split)

personajes = "Luffy Zoro Nami Usopp Sanji"
list_personajes = personajes.split()
# print(f"lista personajes: {list_personajes}")
# print(f"Tipo: {type(list_personajes)}")

personajes_separados_coma = "Luffy, Zoro, Nami, Usopp, Sanji"
list_personajes = personajes_separados_coma.split(", ")
# print(f"lista personajes: {list_personajes}")

list_personajes  =personajes_separados_coma.split(", ", 3)
print(f"lista personajes: {list_personajes}")