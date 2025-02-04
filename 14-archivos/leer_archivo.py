archivo = open("prueba.txt", "r", encoding="utf8")
# print(archivo.read())

# leer algunos caracteres
# print(archivo.readline())
# print(archivo.readline())

# for linea in archivo:
#   print(linea)
# print(archivo.readlines()) 
# print(archivo.readlines()[0])

# abrimos un nuevo archivo 
# a - anexar informacion
archivo2 = open("copia.txt", "a", encoding="utf8")
archivo2.write(archivo.read())

archivo.close()
archivo2.close()