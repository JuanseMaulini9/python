from cuadrado import Cuadrado
from rectangulo import Rectangulo
# from figura_geometrica import FiguraGeometrica

# No se puede inicializar una clase abstracta
# figura1 = FiguraGeometrica()

print("Creacion objeto cuadrado".center(50, "-"))
cuadrado1 = Cuadrado(19, "rojo")
print(cuadrado1)

print("Creacion objeto rectangulo".center(50, "-"))
rectangulo1 = Rectangulo(5, 38, "azul")
print(rectangulo1)

