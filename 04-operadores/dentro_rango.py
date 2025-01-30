dato = int(input("Proporciona un dato entero: "))

# esta_dentro_rango = 1 <= dato <= 10
# print(f"Variable esta dentro de rango (entre 1 y 10)? : {esta_dentro_rango}")

# Revisar la logica inversa para saber si eesta fuera de rango
esta_fuera_rango = not(1 <= dato <= 10)
print(f"Variable esta fuera de rango (entre 1 y 10)?: {esta_fuera_rango}")