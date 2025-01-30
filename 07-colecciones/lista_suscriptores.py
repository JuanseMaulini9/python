print("*** Lista suscriptores ***")

suscriptores = set()

numero_suscriptores = int(input("Proporciona el numeor de suscriptores iniciales: "))
for _ in range(numero_suscriptores):
  suscriptores.add(input("Nuevo suscriptor (email): "))

nuevo_suscriptor = input("Proporciona el nuevo suscripto: ")
if(nuevo_suscriptor in suscriptores):
  print(f"El nuevo suscriptor ya esta en la lista {nuevo_suscriptor}")
else:
  suscriptores.add(nuevo_suscriptor)
  print(f"El nuevo suscriptor se ha agregado a la lista de suscriptores {nuevo_suscriptor}")
  
print(f"Lista de suscriptores actualizada: {suscriptores}")

suscriptor_eliminar = input("Proporciona el suscriptor a eliminar: ")
suscriptores.remove(suscriptor_eliminar)
print(f"El suscriptor {suscriptor_eliminar} ha sido eliminado de la lista")
print(f"Lista de suscriptores actualizada: {suscriptores}")