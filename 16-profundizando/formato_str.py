# Formato de str

# nombre = "Luffy"
# edad = 19
# mensaje_con_formato = "Mi nombre es %s y tengo %d años" %(nombre, edad)
# # print(mensaje_con_formato)

# persona = ("Zoro", "Roronoa", 21)
# # mensaje_con_formato = "Mi nombre es %s %s y tengo %d años" %persona
# # print(mensaje_con_formato)
# mensaje_con_formato = "Mi nombre es %s %s y tengo %d años"

# print(mensaje_con_formato%persona)

nombre = "Luffy"
edad = 19
recompensa = 3000000
mensaje = "Nombre {} edad {} recompensa {:.2f}".format(nombre, edad, recompensa)
# print(mensaje)

# mensaje = "Nombre {0} Edad {1} recompensa {2:.2f}".format(nombre, edad, recompensa)
# print(mensaje)

# mensaje = " recompensa {2:.2f} Nombre {0} Edad {1}".format(nombre, edad, recompensa)
# print(mensaje)

mensaje = "Nombre {n} Edad {e} Recompensa {r}".format(n=nombre, e=edad, r=recompensa)
# print(mensaje)

diccionario = {"nombre": "Luffy", "edad": "19", "recompensa": 3000000}
mensaje = f"Nombre {nombre} Edad {edad} Recompensa {recompensa}"
# print(mensaje)

# Metodo print

print(nombre, edad, recompensa, sep=", ")
