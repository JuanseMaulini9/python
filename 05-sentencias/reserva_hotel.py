print("*** Reserva hotel ***")

nombre_cliente = input("Ingrese el nombre del cliente: ")
dias_hotel = int(input("Ingrese cuantos dias se quedara en el hotel: "))
vista_mar = input("Quiere vista al mar (Si/No)? ")

VISTA_AL_MAR = 190.50
SIN_VISTA_AL_MAR = 150.50

if vista_mar.strip().lower() == "si":
  costo_total = VISTA_AL_MAR * dias_hotel
  print(f"El costo de su reserva es de: {costo_total}")
else:
  costo_total = SIN_VISTA_AL_MAR * dias_hotel
  print(f"El costo de su reserva es de: {costo_total}")