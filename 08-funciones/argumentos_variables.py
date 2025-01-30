print("*** Argumentos variables ***")

def superheroe_superpoderes(superheroe, nombre, *args): 
  print(f"Superheroe: {superheroe} - {nombre} - {args}")
  for superpoder in args:
    print(f"\t superpoder: {superpoder}")
  
superheroe_superpoderes("spiderman", "Peter Parker", "trepar", "Instinto aracnido", "telaraña")
superheroe_superpoderes("Iron Man", "Tony Stark", "Armadura")
superheroe_superpoderes("Mi vecino", "Perez")