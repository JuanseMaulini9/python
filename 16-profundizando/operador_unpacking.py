# * desempaquetar

numeros = [1,2,3]

print(numeros)

print(*numeros)

print(*numeros, sep=" - ")

def sumar(a,b,c):
  print(f"resultado de la suma: {a+b+c}")

sumar(*numeros)

# Extraer algunas partes de una lista

mi_lista = [1,2,3,4,5,6]
a,*b,c,d = mi_lista
print(a,b,c,d)

# Unir listas
lista1 = [1,2,3]
lista2 = [4,5,6]

lista3 = [*lista1, *lista2]

print(lista3)

# unir diccionarios
dic1 = {"a": 1, "b":2, "c":3}
dic2 = {"d": 4, "e":5}
dic3 = {**dic1, **dic2}
print(f"Unir dicts: {dic3}")

# Construir una lista a partir de un str
lista = [*"HolaMundo"]
print(lista)
print(*lista, sep="")