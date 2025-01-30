from random import randint

print("*** Generador de id ***")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
año_nacimiento = input("Ingrese su año de nacimiento: ")

nombre_substring = nombre.strip().upper()[0:2]
apellido_substring = apellido.strip().upper()[0:2]
año_nacimiento_substring = año_nacimiento.strip()[2:4]

valor_aleatorio = str(randint(1000, 9999))

id = f"{nombre_substring}{apellido_substring}{año_nacimiento_substring}{valor_aleatorio}"
print(id)
