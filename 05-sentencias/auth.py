print("*** Auth ***")

USUARIO_ALMACENADO = "admin"
CONTRASENA_ALMACENADA = "123"

username = input("Ingrese el nombre de usuario: ")
password = input("Ingrese la contraseña: ")

if username == USUARIO_ALMACENADO and password == CONTRASENA_ALMACENADA:
  print(F"Bienvenido al sistema")
elif username != USUARIO_ALMACENADO and CONTRASENA_ALMACENADA == password:
  print("El nombre de usuario no es valido")
elif password != CONTRASENA_ALMACENADA and username == USUARIO_ALMACENADO:
  print("La contraseña es invalida")
else:
  print("Usuario y contraseña invalidos")