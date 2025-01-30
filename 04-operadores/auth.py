print("*** Sistema de autenticacion ***")

username = input("Ingrese su username: ")
password = input("Ingrese su password: ")

USERNAME_REGISTRED = "admin"
PASSWORD_REGISTRED = "123456"

print(f"ingresa correctamente? {username == USERNAME_REGISTRED and password == PASSWORD_REGISTRED}")