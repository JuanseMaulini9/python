print("*** Sistema de administracion de cuentas ***")

salir = False


while not salir:
  opcion = int(input("""
  Menu:
    1. Crear cuenta
    2. Eliminar cuenta
    3. Salir
  Escoje una opcion: """))
  
  if opcion == 1:
    print("Creando cuenta...")
  elif opcion == 2: 
    print("Eliminando cuenta...")
  elif opcion == 3:
    salir = True
    print("Saliendo del sistema")
  else:
    print("Seleccione una opcion valida")