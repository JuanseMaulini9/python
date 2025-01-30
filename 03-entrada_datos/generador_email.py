print("*** Generador emails ***")
nombre = input("ingrese su nombre: ")
apllidos = input("ingrese sus apellidos: ")
nombre_empresa = input("ingrese el nombre de su empresa: ")
dominio = input("ingrese su dominio: ")

nombre_formateado = nombre.strip().lower().replace(" ", ".")
apellidos_formateado = apllidos.strip().lower().replace(" ", ".")
nombre_empresa_formateado = nombre_empresa.strip().lower().replace(" ", "")
dominio_formateado = dominio.strip().lower().replace(" ", "")

resultado = f"{nombre_formateado}.{apellidos_formateado}@{nombre_empresa_formateado}{dominio_formateado}"
print(resultado)