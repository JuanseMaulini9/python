#alinear cadenas

#centrar - centrar un string
titulo = "One Piece"
# print(len(titulo))
# print(titulo.center(10, "*"))
# print(len(titulo))

#centro
print(titulo.center(len(titulo)+10, "-"))
#izquierda
print(titulo.ljust(len(titulo) + 10, "-"))
#derecha
print(titulo.rjust(len(titulo) + 10, "-"))

