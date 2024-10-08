# Variables
my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 12
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema 
print(len(my_string_variable))

# Variables en una sola linea
name, surname, alias, age = "Juanse", "Maulini", "Mauju", 23
print(name, surname, alias, age)

# Inputs
# name= input("Tu nombre es: ")
# age= input("cuantos años tenes? ")

print(name)
print(age)

# Cambio de tipo
name = 23
age = "Juanse"

print(name)
print(age)

# forzando el tipo
address: str = "direccion x"
address = 32
print(address)
