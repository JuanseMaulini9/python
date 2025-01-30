# Definir la clase
class Coche:
  
  def __init__(self, marca, modelo, color):
    self._marca = marca #Atributo protegido
    self._modelo = modelo #Atributo protegido
    self._color = color #Atributo protegido
  
  def conducir(self):
    print(f"""Conduciendo el coche:
          Marca: {self._marca}
          Modelo: {self._modelo}
          Color: {self._color}
          """)
  
  # def get_marca(self):
  #   return self._marca
  
  @property 
  def marca(self):
    return self._marca
  
  @marca.setter
  def marca(self, marca):
    self._marca = marca
  
  @property   
  def modelo(self):
    return self._modelo
  
  @modelo.setter
  def modelo(self, modelo):
    self._modelo = modelo
  
  @property   
  def color(self):
    return self.color
  
  @color.setter
  def color(self, color):
    self._color = color

    
#Programa principal
if __name__ == "__main__":
  coche1 = Coche("Toyota", "Corolla", "Gris")
  coche1.conducir()
  coche1.marca = "Toyota 2"
  coche1.modelo = "Yaris 2"
  coche1.color = "Azul 2"
  setattr(coche1, "nuevo_atributo", "Valor del nuevo atributo")
  coche1.conducir()
  
  print(f"Atributo marca coche 1: {coche1.marca}")
  coche1.marca = "Peugeot"
  print(f"Atributo marca coche 1: {coche1.marca}")
  print(coche1.nuevo_atributo)
  
  coche2 = Coche("chevrolet", "trax", "blanco")
  coche2.conducir()
  # coche2.nuevo_atributo