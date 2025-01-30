condicion1, condicion2 = True, True

resultado = condicion1 and condicion2
print(f"resultado {condicion1} and {condicion1}: {resultado}")

# Ejemplo
print("\nSistema de descuento vip")
NO_PRODUCTOS_DESCUENTOS = 10
cantidad_productos = int(input("Cuantos productor compraste: "))
tiene_membresia = input("Tienes membresia de la tienda (Si/No)? ")

es_elejible_descuento = cantidad_productos >= NO_PRODUCTOS_DESCUENTOS and tiene_membresia.lower().strip() == "si"
print(f"Tienes acceso al descunto vip? {es_elejible_descuento}")