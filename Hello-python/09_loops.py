### Loops ###

# While

my_condition = 0

while my_condition < 10: 
  print(my_condition)
  my_condition += 2
else:
  print("Mi condicion es mayor o igual que 10")
  
print("la ejecucion continua")

while my_condition < 20: 
  my_condition += 1
  if my_condition == 15:
    print("se detiene la ejecucion")
    break 
  print(my_condition)
  
print("la ejecucion continua")

# For

my_list = [12,14,567,23,4,57,2]

for element in my_list:
  print(element)

my_tuple = (24, 179, "Juanse", "Maulini", "Maulini")

for element in my_tuple:
  print(element)
  
my_set = {
  "Javascript",
  "Typescript",
  "Pyhton"
}

for element in my_set:
  print(element)

my_dict = {
  "Nombre": "Juanse",
  "Apellido": "Maulini",
  "Edad": 24, 
  "Lenguajes": {"Python", "Javascript", "Java"},
  1: 1.79 
  }

for element in my_dict:
  print(element)
  if element == "Edad": 
    break
  print("Se ejecuta")
else: 
  print("El bucle for para mi diccionario ha finalizado")
  
for element in my_dict:
  print(element)
  if element == "Edad": 
    continue
  print("Se ejecuta")
else: 
  print("El bucle for para mi diccionario ha finalizado")

