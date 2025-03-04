# Profundizando en tuplas

# Declarar variables
a, b = "Hola", "Adios"
print(f"a: {a}, b: {b}")

# swap (intercambio)
a, b = b, a
print(f"a: {a}, b: {b}")

# Regresar multiples valores
def minmax(elementos):
  return min(elementos), max(elementos)

min, max = minmax([1,2,3,4,5])
print(f"min: {min}, max: {max}")

# Regresar la suma de una tupla
resultado = sum((1,2,3,4,5))
print(f"resultado: {resultado}")

def sumar(*args):
  return sum(*args)

resultado = sumar((1,2,3,4,5))
print(resultado)