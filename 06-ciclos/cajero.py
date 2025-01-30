print("*** Cajero automatico ***")

salir = False
saldo = 1000

while not salir:
  opcion = int(input("""
Menu:
  1.depositar
  2.retirar
  3.consultar saldo
  4.salir
Seleccione una opcion: """))
  
  if opcion == 1:
    deposito = float(input("Cantidad a depositar: "))
    saldo += deposito
    print(f"Su nuevo saldo es de: {saldo}")
  elif opcion == 2:
    retiro = float(input("Cantidad a retirar: "))
    if retiro > saldo:
      print(f"No tiene el suficiente saldo, su saldo es de: {saldo}")
    else:
      saldo = saldo - retiro
      print(f"Retirando saldo, su nuevo saldo es de: {saldo}")
  elif opcion == 3: 
    print(f"Su saldo es de: {saldo}")
  elif opcion == 4:
    salir = True
    print("Saliendo...")
  else:
    print("Seleccione una opcion valida")