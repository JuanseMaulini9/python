condicion1 = False
condicion2 = True

resultado = condicion1 or condicion2
print(f"Resultado {condicion1} or {condicion2}: {resultado}")

# Ejemplo

DISTANCIA_PERMITIDA_KM = 3

print("Sistema de prestamo de libros")

tiene_credencial = input("cuentas con credencial de estudiante (si/no)? ")
distancia_biblioteca_km = int(input("A cuantos km vives de la biblioteca? "))

es_elegible_prestamo = tiene_credencial.strip().lower() == "si" or distancia_biblioteca_km <= DISTANCIA_PERMITIDA_KM
print(f"Puedes llevarte el libro? {es_elegible_prestamo}")