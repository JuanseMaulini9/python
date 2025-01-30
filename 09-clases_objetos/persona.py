# Definicion de una clase 
class Persona:
  
  def __init__(self, nombre, apellido):
    self.nombre = nombre
    self.apellido = apellido
      
  def mostrar_persona(self):
    print(f"""Persona:
          Nombre: {self.nombre}
          Apellido: {self.apellido}          
          """)
    print(f"Dir. memoria self: {id(self)}" )
    print(f"Dir. memoria hex self: {hex(id(self))}" )
    
# Creacion de objetos
if __name__ == "__main__":
  # Creacion de un primer objeto
  persona1 = Persona("Luffy", "Monkey D.")
  persona1.mostrar_persona()

  persona2 = Persona("Zoro", "Roronoa")
  persona2.mostrar_persona()