print("*** Validacion password ***")

salir = False

while not salir:
  password = input("Ingrese una password (debe tener 6 caracteres): ")
  if len(password) < 6:
    print("password no valida, ingrese una password valida (6 caracteres)")
  else:
    print("Su password es valida")
    salir = True