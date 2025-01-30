print("*** Calculadora ***")

salir = False

def sumar(a, b):
  return a + b

def restar(a, b):
  return a - b

def multiplicar(a, b):
  return a * b

def dividir(a, b):
  if b == 0:
    return "No es posible dividir por 0"
  else: 
    return a / b
  
def menu():
  print("""Operaciones que puedes realizar: 
              1. Suma
              2. Resta
              3. Multiplicacion
              4. Division
              5: Salir
        """) 
    
def eval(opcion, a, b):
  if(opcion == 1): 
    return sumar(a,b)
  elif(opcion == 2):
    return restar(a, b)
  elif(opcion == 3):
    return multiplicar(a,b)
  elif(opcion == 4):
    return dividir(a,b)
  elif(opcion == 5):
    salir == True  
  else:
    return "Seleccione una opcion valida"
  
while(not salir):
  menu()
  opcion = int(input("Seleccione una opcion: "))
  num1 = int(input("Indique el numero 1: "))
  num2 = int(input("Indique el numero 2: "))
  print(eval(opcion, num1, num2))
  