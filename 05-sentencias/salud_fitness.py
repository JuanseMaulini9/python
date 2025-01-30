print("*** Salud fitness ***")

META_PASOS_DIARIOS = 10000
CALORIAS_POR_PASO = 0.04

username = input("Ingrese el nombre de usuario: ")
pasos_caminados = int(input("Ingrese los pasos caminados hoy: "))

calorias_quemadas = pasos_caminados * CALORIAS_POR_PASO
if META_PASOS_DIARIOS <= pasos_caminados:
  print(f"Cumpliste con la meta de hoy, quemaste {calorias_quemadas} calorias")
else:
  print(f"No cumpliste con la meta de pasos, quemaste {calorias_quemadas} calorias")