print("*** Manejo de listas ***")

mi_lista = [1,2,3,4,5]

print(f"{mi_lista} -> Esta es la lista original")

print(f"Largo de la lista: {len(mi_lista)}")

print(f"Accedemos al valor almacenado en el indicie 4: {mi_lista[4]}")
print(f"Accedemos al ultimo indice de la lista: {mi_lista[-1]}")

mi_lista[1] = 10
print(f"{mi_lista} -> Esta es la lista modificada")

mi_lista.append(6)
print(f"{mi_lista} -> Se agrego el elemento 6")

mi_lista.insert(2,  15)
print(f"{mi_lista} -> se añadio el texto 15 en el indice 2")

mi_lista.remove(5)
print(f"{mi_lista} -> Se elimino el valor 5")

mi_lista.pop(1)
print(f"{mi_lista} -> Se elimino el indice 1")

del mi_lista[2]
print(f"{mi_lista} -> Se elimino el indice 1 usando del")

sublista = mi_lista[1:3]
print(f"{sublista} -> Se genero una sublista del indice 1 al indice 3 (sin incluir)")