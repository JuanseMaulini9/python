# Profundizando en funciones

# Funciones anidadas
def calculadora(a,b, operacion = "sumar"):
  # Funcion anidada
  def sumar(a,b):
    return a + b
  
  def restar(a,b):
    return a - b 
  
  if operacion == "sumar":
    print(f"Resultado de sumar: {sumar(a,b)}")
  elif operacion == "restar":
    print(f"Resultado de restar: {restar(a,b)}")
   
calculadora(5,6)
calculadora(3,2, operacion="restar")