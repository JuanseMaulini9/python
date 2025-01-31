import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mundo_pc.dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
  controlador_teclado = 0
  
  def __init__(self, marca, tipo_entrada):
    Teclado.controlador_teclado += 1
    self.id_teclado = Teclado.controlador_teclado
    super().__init__(marca, tipo_entrada)
    
  def __str__(self):
    return f"Id: {self.id_teclado}, Marca: {self.marca}, Tipo entrada: {self.tipo_entrada}"
  
if __name__ == "__main__":
  teclado1 = Teclado("HP", "USB")
  print(teclado1)
  teclado2 = Teclado("Dell", "USB")
  print(teclado2)