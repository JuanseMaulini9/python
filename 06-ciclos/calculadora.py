print("*** Calculadora ***")

salir = False

while not salir:
  opcion = int(input("""
  Menu:
    1.suma
    2.resta
    3.multiplicacion
    4.division
    5.salir
  Ingrese el numero de la operacion que desea realizar: """))
  
  if opcion == 1: 
    print("\n*** Suma ***")
    valor1 = int(input("Ingrese el valor 1: "))
    valor2 = int(input("Ingrese el valor 2: "))
    resultado = valor1 + valor2
    print(f"resultado: {resultado}")
  elif opcion == 2:
    print("\n*** Resta ***")
    valor1 = int(input("Ingrese el valor 1: "))
    valor2 = int(input("Ingrese el valor 2: "))
    resultado = valor1 - valor2
    print(f"resultado: {resultado}")
  elif opcion == 3:
    print("\n*** Multiplicacion ***")
    valor1 = int(input("Ingrese el valor 1: "))
    valor2 = int(input("Ingrese el valor 2: "))
    resultado = valor1 * valor2
    print(f"resultado: {resultado}")
  elif opcion == 4:
    print("\n*** Division ***")
    valor1 = int(input("Ingrese el valor 1: "))
    valor2 = int(input("Ingrese el valor 2: "))
    if(valor2 == 0):
      print("No se puede dividir por 0")
    else:  
      resultado = valor1 / valor2
      print(f"resultado: {resultado}")
  elif opcion == 5:
    salir = True
  else:
    print("Seleccione una opcion valida")