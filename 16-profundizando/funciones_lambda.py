# Funciones lambda
# Funciones anonimas y pequeñas

# def sumar (a,b):
#   return a + b

# Con una funcion lambda la funcion es anonima y una sola linea de codigo
# No se necesita agregar parentesis para los parametros
# No se necesita la palabra return, pero si debe regresar una expresion valida

mi_funcion_lambda = lambda a,b: a + b

resultado = mi_funcion_lambda(4,3)

print(f"Resultado de sumar con funcion lambda: {resultado}")

# Funciones lambda que no recibe argumentos (debemos regresar una expresion valida)
mi_funcion_lambda = lambda: "Funcion sin argumentos"
print(f"llamar funcion lambda sin argumentos: {mi_funcion_lambda()}")

# Funcion lambda con parametros por default
mi_funcion_lambda = lambda a=2,b=3: a + b

resultado = mi_funcion_lambda()
print(f"Resultado de la funcion lambda con valores por default: {resultado}")

# Funcion lambda con argumentos variables *args y **kwargs
mi_funcion_lambda = lambda *args, **kwargs: len(args) + len(kwargs)
print(f"Resultado de argumentos variables: {mi_funcion_lambda(1,2,3, a=1,b=2)}")


# funciones lambda con argumentos, argumentos variables y valores por default
mi_funcion_lambda = lambda a,b,c=3, *args, **kwargs: a+b+c+len(args)+len(kwargs)
print(f"Resultado funcion lamba: {mi_funcion_lambda(1,2,4, 5,6,7, e=5,f=7)}")
