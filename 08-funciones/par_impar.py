print("*** Funcion par ***")

def es_par(numero):
  if(numero % 2 == 0):
    return True
  else:
    return False

if __name__ == "__main__":
  numero = int(input("Proporciona un valor numerico: "))
  print(f"Numero par? {es_par(numero)}")