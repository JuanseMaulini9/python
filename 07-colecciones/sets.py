print("*** Manejo de sets ***")

mi_set = {1, 2, 3, 4, 5, 4}
print(mi_set)

mi_set.add(6)
print(mi_set)

mi_set.add(7)
print(mi_set)

mi_set.add(3)
print(mi_set)

mi_set.remove(4)
print(mi_set)

for item in mi_set:
  print(item, end=" ")
  
print(f"\nExiste el valor de 1 dentro del del set? {1 in mi_set}")

print(f"Longitud del conjunto: {len(mi_set)}")