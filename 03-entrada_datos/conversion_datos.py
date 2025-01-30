# Conversion de tipo de datos

# Convertir de cadena a numero
numero_cadena = "10"
numero_entero = int(numero_cadena)

print(f"Valor numerico en cadena: {numero_cadena}")
print(f"Cadena a entero: {numero_entero}")

# Convertir de cadena a flotante
numero_cadena = "3.14"
numero_flotante = float(numero_cadena)
print(f"cadena a flotante {numero_flotante}")

# Convertir de numero a cadena
numero_entero = 25
numero_cadena = str(numero_entero)
print(f"numero a cadena {numero_cadena}")

# Convertir a booleano
# Tipo bool es False en los siguientes casos
# Si el valor es 0, cadena vacia, o none, entonces regresa false
# Regresa true, si el valor es distinto de 0, si es distinto a cadena vacia y si es distinto de none

numero_bool = 5
booleano = bool(numero_bool)
print(f"valor booleano de 5: {booleano}")

cadena = ''
booleano = bool(cadena)
print(f"Valor booleano de cadena vacia: {booleano}")

cadena = "cadena con valor"
booleano = bool(cadena)
print(f"Valor booleano de cadena no vacia: {booleano}")

variable = None
booleano = bool(variable)
print(f"Valor booleano de tipo none: {booleano}")