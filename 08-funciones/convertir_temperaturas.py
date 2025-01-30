print("*** convertidor temperatura ***")

def celsius_fahrenheit(celcius):
  return (celcius * (9/5)) + 32

def fahrenheit_celsius(fahrenheit):
  return (fahrenheit - 32) * 5/9

salir = False

while(not salir): 
  
  print("""Listado de opciones:
        1. convertir de Celsius a Fahrenheit
        2. convertir de Farenheit a Celsius
        3. Salir
      """)
  opcion = int(input("Seleccione una opcion: "))

  if(opcion == 1):
    celcius = int(input("Ingrese los grados celsius que quiera convertir: "))
    fahrenheit = celsius_fahrenheit(celcius)
    print(fahrenheit)
  elif(opcion == 2):
    celcius = int(input("Ingrese los grados celsius que quiera convertir: "))
    fahrenheit = celsius_fahrenheit(celcius)
    print(fahrenheit)
  elif(opcion == 3):
    salir == True  
  else:
    print("Seleccione una opcion valida")




