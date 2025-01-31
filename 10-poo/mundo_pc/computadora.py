import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mundo_pc.teclado import Teclado
from mundo_pc.monitor import Monitor
from mundo_pc.raton import Raton

class Computadora:
  contador_computadoras = 0
  
  def __init__(self, nombre, monitor, teclado, raton):
    Computadora.contador_computadoras += 1
    self.id_computadora = Computadora.contador_computadoras
    self.nombre = nombre
    self.monitor = monitor
    self.teclado = teclado
    self.raton = raton
  
  def __str__(self): 
    return f"""{self.nombre}: {self.id_computadora}
    Monitor: {self.monitor}
    Teclado: {self.teclado}
    Raton: {self.raton}
  """
  
if __name__ == "__main__":
  teclado1 = Teclado("Hp", "Usb")
  raton1 = Raton("Hp", "Usb")
  monitor1 = Raton("Samsung", "27")
  computadora = Computadora("pavilion", monitor1, teclado1, raton1)
  print(computadora)
  
  teclado2 = Teclado("Dell", "BlueToo")
  raton2 = Raton("Dell", "BlueToo")
  monitor2 = Raton("Lg", "27")
  computadora2 = Computadora("gamer", monitor2, teclado2, raton2)
  print(computadora2)