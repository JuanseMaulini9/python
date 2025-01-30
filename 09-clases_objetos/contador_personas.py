class Persona:
  contador_personas = 0
  
  def __init__(self, nombre, apellido):
    Persona.contador_personas += 1
    self.id = Persona.contador_personas
    self.nombre = nombre
    self.apellido = apellido
  
  def mostrar_persona(self):
    print(f"Persona: {self.id}, {self.nombre}, {self.apellido}")
    
  @staticmethod
  def get_contador_personas_statico():
    print("Metodo estatico")
    return Persona.contador_personas
  
  @classmethod
  def get_contador_personas_class(cls):
    print("metodo clase")
    return cls.contador_personas  
    
if __name__ == "__main__":
  print("ejemplo contador de personas")
  persona1 = Persona("Luffy", "Monkey D.")
  persona1.mostrar_persona()
  
  persona2 = Persona("Zoro", "Roronoa")
  persona2.mostrar_persona()
  
  print(f"Contador de objetos persona: {Persona.contador_personas}")
  print(f"Contador onjetos Persona (persona1): {persona1.contador_personas}")
  print(f"Contador de objeto persona (static): {Persona.get_contador_personas_statico()}")
  print(f"Contador objetos Persona (clase): {Persona.get_contador_personas_class()}")