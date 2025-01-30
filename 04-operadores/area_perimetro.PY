print("*** Area y perimetro de un resctangulo ***")

altura = float(input("Ingrese la altura del rectangulo: "))
base = float(input("Ingrese la base del rectangulo: "))

area = base * altura
perimetro = 2 * (base + altura)

print(f"""
      area: {area:.2f}
      perimetro: {perimetro:.2f}      
      """)