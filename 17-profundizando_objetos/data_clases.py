from dataclasses import dataclass
from typing import ClassVar

@dataclass(eq=True, frozen=True)
class Domicilio:
  calle:str
  numero:int = 0
  

@dataclass(eq=True, frozen=True)
class Persona: 
  nombre: str
  apellido: str
  domicilio: Domicilio
  contador_personas: ClassVar[int] = 0
  
  def __post_init__(self):
    if not self.nombre:
      raise ValueError(f"Valor de nombre vacio: {self.nombre}")
    if not self.apellido:
      raise ValueError(f"Valor de apellido vacio: {self.apellido}")

domicilio1 = Domicilio("Alemania", 114)
persona1 = Persona("Luffy", "Monkey D.", domicilio1)
print(persona1)

# variable de clase
print(f"Variable de clase: {Persona.contador_personas}")
# variables de instancia
print(f"Variables de instancia: {persona1.__dict__}")

# variable con valores vacios
persona_vacia = Persona("Zoro", "Roronoa", None)
print(persona_vacia)

# Revisar igualdad entre objetos (__eq__)
persona2 = Persona("Luffy", "Monkey D.", Domicilio("Alemania", 114))
print(f"Objetos iguales? {persona1 == persona2}")

# Agregar esta clase a una coleccion
coleccion = {persona1, persona2}
print(coleccion)
# frozen = True
# coleccion[0].nombre = "Ace"
# persona1.nombre = "Ace"