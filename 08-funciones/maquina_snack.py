print("*** Maquina de snack ***")

stock = [
  {"id": 1, "nombre": "Lays", "precio": 30},
  {"id": 2, "nombre": "Coca-cola", "precio": 50},
  {"id": 3, "nombre": "Sanguche", "precio": 120}
]

carrito = []

def mostrar_stock():
  print("--- Snacks disponibles ---")
  for producto in stock:
    print(f"Id: {producto.get("id")} -> {producto.get("nombre")} - ${producto.get("precio")}")
  
def comprar_snack():
  print("--- Comprar snack ---")
  id = int(input("Ingrese el id del producto que quiera comprar: "))
  for producto in stock:
    if id == producto.get("id"):
      carrito.append(producto)
      break 

def mostrar_ticket():
  total = 0
  print("Ticket")
  for producto in carrito:
    total += producto.get("precio")
    print(f"{producto.get("nombre")} - ${producto.get("precio")}")
  print(f"Total: {total}")

def mostrar_menu():
  salir = False
  while not salir:
    print("""
    Menu: 
      1. Mostrar Snacks
      2. Comprar Snacks
      3. Mostrar ticket
      4. Salir
    """)
    opcion = int(input("Escoge una opcion: "))
    if opcion == 1:
      mostrar_stock()
    elif opcion == 2:
      comprar_snack()
    elif opcion == 3:
      mostrar_ticket()
    elif opcion == 4:
      salir = True
    else: 
      print("Seleccione una opcion valida")
      
      
mostrar_menu()