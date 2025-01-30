print("*** Combinacion de listas y tuplas ***")

productos = [
  ("P001", "Remera", 20.00),
  ("P002", "Jeans", 30.00),
  ("P003", "Buzo", 40.00)
]

precio_total = 0

print("Informacion de los productos: ")
for producto in productos:
  #print(producto)
  id, descripcion, precio = producto
  print(f"Producto: id = {id}, descripcion = {descripcion}, precio = {precio}")
  precio_total += precio
  
print(f"Precio total de los productos: {precio_total}")