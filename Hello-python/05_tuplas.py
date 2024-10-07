### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (24, 179, "Juanse", "Maulini", "Maulini")
my_other_tuple=(12, 25, 67, 34)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count("luffy"))
print(my_tuple.index("Juanse"))
print(my_tuple.index("Maulini"))

# my_tuple[1] = 180 es inmutable

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Mauju"
my_tuple.insert(1, "Negro")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined