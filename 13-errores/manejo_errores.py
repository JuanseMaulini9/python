from numeros_identicos_error import NumerosIdenticosError

result = None

try:
  a = int(input("Primer numero: "))
  b = int(input("Segundo numero: "))
  if a == b:
    raise NumerosIdenticosError("numeros identicos")
  result = a/b
except ZeroDivisionError as e:
  print(f"Ocurrio un error: {e}, {type(e)}")
except TypeError as e:
  print(f"Ocurrio un error: {e}, {type(e)}") 
except ValueError as e:
  print(f"Ocurrio un error: {e}, {type(e)}") 
except Exception as e:
  print(f"Ocurrio un error: {e}, {type(e)}")
else: 
  print("No se arrojo ninguna excepcion")
finally:
  print("Ejecucion del bloque finally")

print(f"Resultado: {result}")
print("Continua")    