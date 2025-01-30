print("*** Comprension de listas ***")

numeros = [1,2,3,4,5]
cuadrados = [x**2 for x in numeros]

print(cuadrados)

numero = range(10+1)
pares = [x for x in numero if x % 2 == 0]

print(pares)

nombres = ["Luffy", "Zoro", "Nami"]
saludando = [f"Hola {nombre}" for nombre in nombres]
print(saludando)