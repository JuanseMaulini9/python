print("*** Promedio de calificaciones ***")

calificaciones = []

cantidad_calificaciones = int(input("Ingrese la cantidad de calificaciones: "))

contador = 0

for index in range(cantidad_calificaciones):
  calificacion = float(input(f"Ingrese la calificacion {index + 1}: "))
  calificaciones.append(calificacion)
  contador += calificacion

promedio = contador / cantidad_calificaciones

print(f"lista de calificaciones: {calificaciones}")
print(f"promedio de calificiones: {promedio}")