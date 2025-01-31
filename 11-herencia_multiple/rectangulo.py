from figura_geometrica import FiguraGeometrica
from color import Color

class Rectangulo(FiguraGeometrica, Color):
  def __init__(self, ancho, alto, color):
    # super.__init__(lado)
    FiguraGeometrica.__init__(self, ancho, alto)
    Color.__init__(self, color)
    
  def calcular_area(self):
    return self.alto * self.ancho
  
  def __str__(self):
    return f"""Rectangulo:
    Calculo area rectangulo: {self.calcular_area()}
    {FiguraGeometrica.__str__(self)}
    {Color.__str__(self)}
  """
  