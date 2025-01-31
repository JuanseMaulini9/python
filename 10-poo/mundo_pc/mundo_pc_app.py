import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mundo_pc.computadora import Computadora
from mundo_pc.teclado import Teclado
from mundo_pc.monitor import Monitor
from mundo_pc.raton import Raton
from mundo_pc.orden import Orden

print("*** Mundo PC ***")

teclado1 = Teclado("Hp", "Usb")
raton1 = Raton("Hp", "Usb")
monitor1 = Monitor("Samsung", "27")
computadora1 = Computadora("pavilion", monitor1, teclado1, raton1)
  
teclado2 = Teclado("Dell", "BlueToo")
raton2 = Raton("Dell", "BlueToo")
monitor2 = Monitor("Lg", "27")
computadora2 = Computadora("gamer", monitor2, teclado2, raton2)

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)

teclado3 = Teclado("Corsair", "USB")
raton3 = Raton("Corsair", "USB")
monitor3 = Monitor("Corsair", "USB")
computadora3= Computadora("coirsair", monitor3, teclado3, raton3)
orden1.agregar_computadora(computadora3)
print(orden1)