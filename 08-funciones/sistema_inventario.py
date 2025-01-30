print("*** Sistema de inventario ***")

inventario = [
  {"id": 1, "nombre": "playstation 5", "precio": 450, "cantidad": 3},
  {"id": 2, "nombre": "nintendo switch", "precio": 300, "cantidad": 6},
  {"id": 3, "nombre": "xbox series x", "precio": 400, "cantidad": 10},
]

def mostar_inventario():
  print("--- inventario del almacen ---")
  for producto in inventario:
    print(f"id: {producto.get("id")}, Nombre: {producto.get("nombre")}, Precio: ${producto.get("precio")}, Cantidad: {producto.get("cantidad")}")
           
def agregar_producto():
  print("Agregar producto")
  id = len(inventario) + 1
  nombre = input("Ingrese el nombre del producto: ")
  precio = float(input("Ingrese el precio del producto: "))
  cantidad = int(input("Ingrese la cantidad de productos: "))
  
  producto = {
    "id": id,
    "nombre": nombre,
    "precio": precio,
    "cantidad": cantidad
  }
  
  inventario.append(producto)
  
def buscar_producto():
  id = int(input("Ingrese el id a buscar: "))
  for producto in inventario:
    if producto.get("id") == id:
      print("Informacion del producto encontrado: ")
      print(f"id: {producto.get("id")}, nombre: {producto.get("nombre")}, precio: {producto.get("precio")}, cantidad: {producto.get("cantidad")}")

def mostrar_menu():
  salir = False
  while not salir:
    opcion = int(input("""
              Seleccione una opcion:
                1. Mostrar inventario
                2. Agregar nuevo producto
                3. Buscar producto por Id
                4. Salir
              """))
    if opcion == 1:
      mostar_inventario()
    elif opcion == 2:
      agregar_producto()
    elif opcion == 3:
      buscar_producto()
    elif opcion == 4:
      salir = True
      
mostrar_menu()