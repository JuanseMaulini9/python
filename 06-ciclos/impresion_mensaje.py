print("*** Repeticion de un mensaje ***")

mensaje = input("Proporciona un mensaje a repetir: ")
numero_de_repeticiones = int(input("Proporciona el numero de repeticiones: "))

for _ in range(numero_de_repeticiones): 
  print(mensaje)