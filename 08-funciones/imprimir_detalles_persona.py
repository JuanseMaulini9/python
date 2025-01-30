print("*** Imprimir detalles de una persona usando kwargs ***")

def imprimir_detalle_persona(**kwargs):
  print("\nValores recibidos: ")
  for llave, valor in kwargs.items():
    print(f"{llave}:{valor}")
    

imprimir_detalle_persona(nombre="Juanse", edad=24, ciudad="Buenos Aires")
imprimir_detalle_persona(nombre="Luffy", edad=19, ciudad="villa foosha", puesto="capitan")