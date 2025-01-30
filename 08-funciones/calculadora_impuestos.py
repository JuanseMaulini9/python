print("*** Calcular impuestos ***")

def calcular_impuesto(pago, porcentaje_impuesto):
  impuesto = pago * (porcentaje_impuesto / 100)
  return pago + impuesto

pago = int(input("ingrese el pago in impuesto: "))
porcentaje_impuesto = int(input("Ingrese el monto del impuesto "))
total = calcular_impuesto(pago, porcentaje_impuesto)
print(f"Pago con impuesto: {total}")