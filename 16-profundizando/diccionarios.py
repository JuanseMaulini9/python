# Profundizando en diccionarios

# Los diccionarios guardan un orden (a diferencia de un set)

diccionario = {"Nombre": "Luffy", "Apellido": "Monkey D.", "Edad": 19}

print(diccionario)

# Los diccionarios son mutables, pero las llaves deben ser inmutables

# diccionario = {[1,2]: "Valor1"}

# diccionario = {(1,2): "Valor1"}
# print(diccionario)

# Se agrega una llave con su valor si no se encuentra 
diccionario["Posicion"] = "Capitan"
print(diccionario)

# No hay valores duplicados en las llaves de un diccionario (si ya existe se reemplaza)
diccionario["Nombre"]  = "Law"
print(diccionario)

# Recuperar un valor indicando una llave
print(diccionario["Nombre"])
# Si no encuentra la llave lanza una excepcion
# print(diccionario["nombre"])

# Metodo Get recupera una llave y si no existe no lanza excepcion
# Ademas podemos regresar un valor en caso de que no exista la llave
print(diccionario.get("Nombres", "No se encontro la llave"))
print(diccionario)

# setdefault si modifica el diccionario, ademas se puede agregar un valor por default
nombre = diccionario.setdefault("Nombres", "Valor por default")
print(nombre)
print(diccionario)

# Imprimir con pprint
from pprint import pprint as pp
# help(pp)

pp(diccionario, sort_dicts=False)