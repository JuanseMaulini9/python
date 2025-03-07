# un closure es una funcion que define a otra y ademas la puede regresar
# la funcion anidada puede acceder a las variables locales definidas
# en la funcion principal o externas

# Funcion principal 
# def operacion(a,b):
#   # Definimos una funcion interna o anidada
#   def sumar():
#     return a + b
  
#   return sumar

# Funcion principal
def operacion(a,b):
  # 1. Definimos una funcion lambda interna o anidada y la retornamos
  return lambda: a+b

mi_funcion_closure = operacion(5,2)
print(f"Resultado de la funcion closure: {mi_funcion_closure()}")

# Llamar la funcion regresada al vuelo
print(f"Resultado de la funcion closure al vuelo: {operacion(2,3)()}")