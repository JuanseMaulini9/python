# Ejemplo de herencia simple 
class ListaSimple:
  def __init__(self, elementos):
    self._elementos = list(elementos)
  
  def agregar(self, elemento):
    self._elementos.append(elemento)
    
  def __getitem__(self, index):
    return self._elementos[index]
  
  def ordenar(self):
    self._elementos.sort()
  
  def __len__(self):
    return len(self._elementos)
  
  def __repr__(self):
    return f"{self.__class__.__name__}({self._elementos!r})"
  
class ListaOrdenada(ListaSimple):
  def __init__(self, elementos=[]):
    super().__init__(elementos)
    # Ordenamos siempre los elementos una vez inicializados
    self.ordenar()

  def agregar(self, elemento):
    super().agregar(elemento)
    # Ordenar el nuevo elemento
    super().ordenar()
  
# Solo acepta numeros  
class ListaEnteros(ListaSimple):
  def __init__(self, elementos=[]):
    for elemento in elementos:
      self._validar(elemento)
    # Una vez validados los elementos los agregamos
    super().__init__(elementos)
    
  def _validar(self, elemento):
    # Validamos si el elemento es de tipo entero
    if not isinstance(elemento, int):
      raise ValueError(f"No es un valor entero: {elemento}")
    
  # Sobreescribimos el metodo agregar de la clase padre
  def agregar(self, elemento):
    self._validar(elemento)
    super().agregar(elemento)

# Lista de Enteros ordenada 
class ListaEnterosOrdenada(ListaEnteros, ListaOrdenada):
  pass


# Lista simple
lista_simple = ListaSimple([5,3,6,8])
print(lista_simple)

# Lista ordenada
lista_ordenada = ListaOrdenada([3,6,1,4,2,3,567,8])
print(lista_ordenada)

lista_ordenada.agregar(-14)
print(lista_ordenada)

print(len(lista_ordenada))

# Lista de enteros
lista_enteros = ListaEnteros([1,2,3,-14])
lista_enteros.agregar(13)
print(lista_enteros)

# Lista enteros ordenada
lista_enteros_ordenada = ListaEnterosOrdenada([4,5,6,7,-1,14,-3])
print(lista_enteros_ordenada)
lista_enteros_ordenada.agregar(8)
print(lista_enteros_ordenada)

# Saber las clases padre y su orden 
print(ListaEnterosOrdenada.__bases__)
# MRO (method resolution order)
print(ListaEnterosOrdenada.__mro__)

# isinstance
print("Es entero?", isinstance(10, int))
print("Es una cadena?", isinstance("hola", str))
print("Es una lista de enteros ordenada?", isinstance(lista_enteros_ordenada, ListaEnterosOrdenada))

print("Es lista ent?", isinstance(lista_enteros_ordenada, ListaEnteros))
print("Es una lista ordenada?", isinstance(lista_enteros_ordenada, ListaOrdenada))
print("Es una lista simple?", isinstance(lista_enteros_ordenada, ListaSimple))

print("Es object?", isinstance(lista_enteros_ordenada, object))

print("Es de varios tipos?", isinstance(lista_enteros_ordenada, (ListaEnteros, ListaSimple)) )