from figura_geometrica import FiguraGeometrica
from color import Color

class Cuadrado(FiguraGeometrica, Color):
  def __init__(self, lado, color):
    # super.__init__(lado)
    FiguraGeometrica.__init__(self, lado, lado)
    Color.__init__(self, color)
    
  def calcular_area(self):
    return self.alto * self.ancho
  
  def __str__(self):
    return f"""Cuadrado:
    Calculo de area cuadrado: {self.calcular_area()}
    {FiguraGeometrica.__str__(self)}
    {Color.__str__(self)}
  """
  