# Operador de asignacion
numero = 10
print(f"valor de la variable numero: {numero}")
numero = 5
print(f"valor de la variable numero: {numero}")

cadena = "Saludos desde python"
print(f"valor de la cadena: {cadena}")

# Asignacion multiples

x,y,z = 5, "Hola", -9.15
print(f"valor de x: {x}")
print(f"valor de y: {y}")
print(f"valor de z: {z}")

# Asignacion encadenada
a = b = c = 10
print(f"Valor de a = {a}, b = {b}, c = {c}")

# Intercambio de valores de variables sin utilizar variables temporales
x, y = 5, 10
print(f"valor de x: {x}, valor de y: {y}")
# Aplicando el concepto de asignacion multiple intercambiamos valores
x, y = y, x
print(f"valor de x: {x}, valor de y: {y}")

# Recibir multiples valores de la entrada del usuario
nombre, apellido = input("ingresa tu nombre y apellido separado por coma: ").split(",")
print(f"nombre: {nombre}, apellido: {apellido.strip()}")

