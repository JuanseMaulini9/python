# Listas 

my_list = list()
my_other_list = []

print(len(my_list))

my_list=[23,62,45,12,34, 23]

print(my_list)
print(len(my_list))

my_other_list = [24, 1.79, "Juanse", "Maulini"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list.count("Juanse"))
print(my_list.count(23))

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

print(my_list + my_other_list)

my_other_list.append("Mauju")
print(my_other_list)

my_other_list.insert(1, "purple")
print(my_other_list)

my_other_list.remove("purple")
print(my_other_list)

my_list.remove(23)
print(my_list)

pop = my_list.pop()
print(pop)
print(my_list)

pop = my_list.pop(2)
print(pop)
print(my_list)

del my_list[2]
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

my_list = "Hola Python"

print(my_list)
print(type(my_list))
