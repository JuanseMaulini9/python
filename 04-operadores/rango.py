print("*** Valor dentro de rango ***")

VALOR_MINIMO = 0
VALOR_MAXIMO = 5

valor = int(input("Ingrese el valor a evaluar (entre 0 y 5): "))
resultado = VALOR_MINIMO <= valor <= VALOR_MAXIMO
print(f"Su valor se encuentra dentro del rango? {resultado}")