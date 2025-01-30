print("*** Costo de envio ***")

TARIFA_NACIONAL = 10
TARIFA_INTERNACIONAL = 20

destino = input("Ingrese el destino (Nacional/Internacional): ")
peso = float(input("Indique el peso del paquete (kg): "))

costo = None

if destino.strip().lower() == "nacional": 
  costo = TARIFA_NACIONAL * peso
  print(f"El costo de su paquete es de: {costo}")
elif destino.strip().lower() == "internacional": 
  costo = TARIFA_INTERNACIONAL * peso
  print(f"El costo de su paquete es de: {costo}")
else:
  print("destino invalido")  

