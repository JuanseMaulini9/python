### Functions ###

def my_function():
  print("Hola function")

my_function()
my_function()
my_function()

def sum_two_values(val1, val2):
  print(val1 + val2) 
  
sum_two_values(5,2)
sum_two_values("5","2")

def sum_two_values_whith_return(val1, val2):
  return val1 + val2 

my_result = sum_two_values_whith_return(1,2)
print(my_result)

def print_name(name, surname):
  print(f"{name} {surname}")
  
print_name(surname="Maulini", name="Juanse")

def print_name_with_default(name, surname, alias = "Sin alias"):
  print(f"{name} {surname} {alias}")
  
print_name_with_default("Juanse", "Maulini")
print_name_with_default("Juanse", "Maulini", "Mauju")

def print_upper_texts(*texts):
  for text in texts:
    print(text.upper())
  
print_upper_texts("hola", "mundo", "como", "kf")