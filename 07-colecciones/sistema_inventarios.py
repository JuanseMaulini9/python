print("*** Inventario ***")

cantidad = int(input("Cuantos productos desea agregar? "))

lista = []

for i in range(cantidad):
  print(f"\nIngrese los datos del producto {i + 1}")
  nombre = input(f"Ingrese el nombre del producto {i+1}: ")
  precio = float(input(f"Ingrese el precio del producto {i+1}: "))
  cantidad = int(input(f"Ingrese la cantidad del producto {i+1}: "))
  lista.append({
    "id": i,
    "nombre": nombre,
    "precio": precio,
    "cantidad": cantidad
  }) 

print(lista)

id_buscar = int(input("\nIngrese el Id del producto a buscar: "))
producto_encontrado = None
for producto in lista:
  if producto.get("id") == id_buscar:
    producto_encontrado = producto
    break
  
if producto_encontrado is not None:
  print("Informacion del producto encontrado:")
  print(f"""
        ID: {producto_encontrado.get("id")}
        Nombre: {producto_encontrado.get("nombre")}
        Precio: {producto_encontrado.get("precio")}
        Cantidad: {producto_encontrado.get("cantidad")}""")
else:
  print(f"Producto con id {id_buscar} no encontrado")

print(f"\n --- Inventario detallado ---")
for producto in lista:
  print(f"""
        ID: {producto.get("id")}
        Nombre: {producto.get("nombre")}
        Precio: {producto.get("precio")}
        Cantidad: {producto.get("cantidad")}""")