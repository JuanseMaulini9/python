print("*** Receta de cocina ***")

nombre = input("Ingrese el nombre de la receta: ")
ingredientes = input("ingrese los ingredientes de la receta (separados por ,): ")
tiempo_preparacion = int(input("ingrese el tiempo de preparacion en minutos: "))
dificultad = input("Ingrese la dificultad (Facil/Media/Alta): ")

print("\nReceta: ")
print(f"Nombre: {nombre}")
print(f"Ingredientes: {ingredientes}")
print(f"tiempo de preparacion (minutos): {tiempo_preparacion}")
print(f"dificultad: {dificultad}")
