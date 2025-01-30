print("*** Playlist ***")

lista_reproduccion = []

numero_canciones = int(input("Cuantas canciones deseas agregar? "))

for indice in range(numero_canciones):
  cancion = input(f"Proporciona la cancion {indice + 1}: ")
  lista_reproduccion.append(cancion)

lista_reproduccion.sort()

print(f"\nLista de reporduccion en orden alfabetido")
print(lista_reproduccion)

print()
for cancion in lista_reproduccion:
  print(f"- {cancion}")