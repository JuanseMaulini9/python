### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {
  "Juanse",
  "Maulini",
  24
}

print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Mauju")

print(my_other_set) # No es una estructura ordenada

my_other_set.add("Mauju") # Un set no admite repetidos

print(my_other_set)

print("Juanse" in my_other_set)
print("Juansu" in my_other_set)

my_other_set.remove("Juanse")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

my_set = {
  "Juanse",
  "Maulini",
  24
}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {
  "Javascript",
  "Typescript",
  "Pyhton"
}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set))

print(my_new_set.difference(my_set))
