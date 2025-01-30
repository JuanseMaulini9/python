print("*** Generacion ticket venta ***")

precio_leche = float(input("precio leche: "))
precio_pan = float(input("precio pan: "))
precio_lechuga = float(input("precio lechuga: "))
precio_bananas = float(input("precio bananas: "))
descuento_porcentaje = int(input("Aplicar algun descuento (%)? "))

# calculo del subtortal sin impuestos
subtotal = precio_bananas + precio_leche + precio_lechuga + precio_pan

descuento = subtotal * (descuento_porcentaje/100)

subtotal_con_descuento = subtotal - descuento

# calculo aplicando los impuestos
impuesto = subtotal_con_descuento * 0.21

costo_total = subtotal_con_descuento + impuesto
print(f"""
Subtotal: ${subtotal:.2f}
descuento: ${descuento:.2f} ({descuento_porcentaje}%)
Subtotal con descuento: ${subtotal_con_descuento:.2f}
Impuesto (21%): ${impuesto:.2f}
Costo total de la compra: ${costo_total:.2f} 
""") 