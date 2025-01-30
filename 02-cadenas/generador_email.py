nombre = "juanse maulini"
empresa = "g mail"
dominio = "com"

nombre_formateado = nombre.replace(" ", ".")
empresa_formateada = empresa.replace(" ", "")

email = f"{nombre_formateado}@{empresa_formateada}.{dominio}"
print(email)