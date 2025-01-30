from random import randint

print("*** Adivinar numero ***")

salir = False
numero = randint(1, 50)
intentos = 1

while not salir: 
  intento = int(input("Ingrese un numero entre 1 y 50: "))
  if(intento == numero): 
    print(f"Ganaste! en {intentos} intentos")
    salir = True
  elif intento > numero:
    print("Proba un numero mas bajo")
    intentos += 1
  elif intento < numero:
    print("Proba un numeor mas alto")  
    intentos += 1