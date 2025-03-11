# decoradores de clase
# Permiten transformar de manera programatica nuestra clase
# Es similar a los decoradores de funciones (metaprogramacion)

import inspect

def decorador_repr(cls):
  print("1. Se ejecuta decorador")
  print(f"Recibimos el objeto de la clase: {cls.__name__}")
  
  # Revisamos los atributos de la clase con el metodo vars
  atributos = vars(cls)
  # Iteramos cada atributo
  # for nombre, atributo in atributos.items():
  #   print(nombre, atributo)
  
  # Revisamos si se ha sobreescrito el metodo __init__
  if "__init__" not in atributos:
    raise TypeError(f"{cls.__name__} no ha reescrito el metodo __init__")

  firma_init = inspect.signature(cls.__init__)
  print(f"Firma del metodo init: {firma_init}")
  
  # Recuperamos los parametros excepto el primeroque es self
  parametros_init = list(firma_init.parameters)[1:]
  print(parametros_init)
  
  # Revisar si por cada parametro tiene un metodo property asociado
  for parametro in parametros_init:
    # property es un valor de tipo built-in para preguntar si se esta utilizando el decorador de property
    es_metodo_property = isinstance(atributos.get(parametro), property)
    if not es_metodo_property:
      raise TypeError(f"No existe un metodo property para el parametro: {parametro}")

  # Crear el metodo repr dinamicamente
  def metodo_repr(self):
    # Obtenemos el nombre de la clase dinamicamente
    nombre_clase = self.__class__.__name__
    print(f"Nombre clase: {nombre_clase}")
    
    #Obtenemos los nombres de la propiedades y sus valores dinamicamente
    # Expresion generadora, crear nombre_atributo=valor_atributo
    generador_argumentos = (f"{nombre}={getattr(self, nombre)!r}" for nombre in parametros_init)
    
    # Lista del generador
    lista_arg = list(generador_argumentos)
    print(f"Lista del generador: {lista_arg}")
    
    # Creamos la cadena a partir de la lista de argumentos
    argumentos = ", ".join(lista_arg)
    print(f"Argumentos del metodo repr: {argumentos}")
    
    # Creamos la forma del metodo __repr__
    resultado_metodo_repr = f"{nombre_clase}({argumentos})"
    print(f"Resultado metodo repr: {resultado_metodo_repr}")  
    return resultado_metodo_repr
  
  # Agregar dinamicamente el metodo repr a nuestra clase 
  setattr(cls, "__repr__", metodo_repr)
    
  return cls
  
@decorador_repr
class Persona:
  def __init__(self, nombre, apellido, edad):
    print("2. Se ejecuta el inicializador")
    self._nombre = nombre
    self._apellido = apellido
    self._edad = edad
  
  @property
  def nombre(self):
    return self._nombre
  
  @property
  def apellido(self):
    return self._apellido
  
  @property
  def edad(self):
    return self._edad

  
persona1 = Persona("Luffy", "Monkey D.", 19)
print(persona1)
persona2 = Persona("Zoro", "Roronoa", 21)
print(persona2)

# Tiene los metodos de property nombre, apellido, repr
print(dir(Persona))
# Tiene el metodo repr sobreescrito
codigo_repr = inspect.getsource(persona1.__repr__)
print(codigo_repr)

  
  