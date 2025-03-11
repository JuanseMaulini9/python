# Simulacion de sobrecaga de constructores en python
# Otras formas de crear objetos en python

class Persona:
  
  def __init__(self, nombre, apellido):
    self.nombre = nombre
    self.apellido = apellido
  
  @classmethod
  def crear_persona_vacia(cls):
    return cls(None, None)
  
  @classmethod
  def crear_persona_con_valores(cls, nombre, apellido):
    return cls(nombre, apellido)
  
  def __str__(self):
    return f"Nombre: {self.nombre}, Apellido: {self.apellido}"

persona1 = Persona("Luffy", "Monkey D.")
persona_vacia = Persona.crear_persona_vacia()
persona2 = Persona.crear_persona_con_valores("Zoro", "Roronoa")

print(persona_vacia)
print(persona1)
print(persona2)
