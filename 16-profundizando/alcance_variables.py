# scope
var_global = "Variable global"

def imprimir():
  # Acceder a una variable global
  global var_global
  print(f"Variable global desde funcion: {var_global}")
  # Definicion de variable local
  var_local = "Variable local"
  print(f"Variable local desde funcion: {var_local}")
  var_global = "Nuevo valor"
  def funcion_anidada():
    print(f"Variable local dentro de la funcion anidada: {var_local}")
  
  funcion_anidada()

  
imprimir()

print(f"Variable global fuera de la funcion: {var_global}")
# No es posible acceder a variables locales fuera del bloque donde se definen
# print(f"Var local fuera de la duncion: {var_local}")



