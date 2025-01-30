class Aritmetica():
  def __init__(self, operando1=None, operando2=None):
    self._operando1 = operando1
    self._operando2 = operando2
    
  def sumar(self):
    return self._operando1 + self._operando2
  
  def restar(self):
    return self._operando1 - self._operando2

  def multiplicar(self):
    return self._operando1 * self._operando2
  
  def dividir(self):
    if(self._operando2 != 0):
      return self._operando1 / self._operando2
    else: return "No se puede divir por 0"
    
  @property
  def operando1(self):
    return self._operando1
  
  @operando1.setter
  def operando1(self, operando1):
    self._operando1 = operando1
    
  @property
  def operando2(self):
    return self._operando2
  
  @operando2.setter
  def operando2(self, operando2):
    self._operando2 = operando2  
    
aritmetica1 = Aritmetica(9, 5)
print("Aritmetica 1:")
print(f"Valor operando1 del objeto aritmetica1: {aritmetica1.operando1}")
print(f"Valor operando2 del objeto aritmetica1: {aritmetica1.operando2}")
print(f"suma: {aritmetica1.sumar()}")
print(f"resta: {aritmetica1.restar()}")
print(f"multiplicacion: {aritmetica1.multiplicar()}")
print(f"division: {aritmetica1.dividir()}")


aritmetica2 = Aritmetica(3, 0)
print("Aritmetica 2:")
print(f"Valor operando1 del objeto aritmetica2: {aritmetica2.operando1}")
print(f"Valor operando2 del objeto aritmetica2: {aritmetica2.operando2}")
print(f"suma: {aritmetica2.sumar()}")
print(f"resta: {aritmetica2.restar()}")
print(f"multiplicacion: {aritmetica2.multiplicar()}")
print(f"division: {aritmetica2.dividir()}")

aritmetica3 = Aritmetica(7)
aritmetica3.operando2 = 9
print("Aritmetica 3:")
print(aritmetica3.sumar())

aritmetica4 = Aritmetica()
print("Aritmetica 4:")
aritmetica4.operando1 = 2
aritmetica4.operando2 = 3
print(aritmetica4.sumar())