print("*** descuentos de tienda ***")

valor_compra = float(input("Ingrese el valor de su compra: "))
es_mimebro = input("Es miembro de la tienda (Si/No)?: ")

if valor_compra > 1000 and es_mimebro.strip().lower() == "si":
  descuento = valor_compra * 0.10
  total_con_descuento = valor_compra - descuento
  print(f"el valor de su compra con el descuento es de: {total_con_descuento}")
elif es_mimebro.strip().lower() == "si":
  descuento = valor_compra * 0.05
  total_con_descuento = valor_compra - descuento
  print(f"el valor de su compra con el descuento es de: {total_con_descuento}")
else:
  print(f"no se le aplica descuento, total: {valor_compra}")