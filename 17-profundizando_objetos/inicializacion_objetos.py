# Orden de inicializacion de objetos
class Padre:
  def __init__(self):
    print("Inicializador de la clase padre")
  def metodo(self):
    print("Metodo padre")
    
class Hijo(Padre):
  # Se manda a llamar el metodo init de la clase padre siempre y cuando la clase hija no defina su propio init

  # Definimos metodo init
  def __init__(self):
    # De manera opcional podemos llamar al metodo init de la clase padre
    print("Inicializador clase hijo")
    super().__init__()
    
  # Sobreescribimos el emtodo heredado de la clase padre
  def metodo(self):
    print("Metodo sobreescrito hijo")
    super().metodo()
    
# padre = Padre()
# padre.metodo()

hijo = Hijo()
hijo.metodo()
