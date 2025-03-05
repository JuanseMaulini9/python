# Las funciones en python son ciudadans de primera clase
# First class citizens

# Definimos la funcion 
def sumar(a,b):
  return a + b

# 1. Asignar una funcion a una variable (no se usan parentesis)
mi_funcion = sumar

# Verificar el tipo de la variable
print(type(mi_funcion))

# Llamamos la funcion a traves de la variable
resultado = mi_funcion(5,8)
print(f"Resultado: {resultado}")

# 2. Funcion como argumento

def operacion(a,b, sumar_arg):
  print(f"Resultado sumar: {sumar_arg(a,b)}")

operacion(2,3,mi_funcion)

# 3. podemos retornar una funcion
def retornar_funcion():
  return sumar

mi_funcion_retornada = retornar_funcion()
print(f"Resultado de la funcion retornada: {mi_funcion_retornada(3,4)}")